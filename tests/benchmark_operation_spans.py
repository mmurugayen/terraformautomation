#!/usr/bin/env python3
"""Local operation-span microbenchmark; batch averages are not request percentiles.

Optionally compare a reviewed baseline file in alternating measurement order.
No network, provider, workload payload or production service is exercised.
"""
import argparse
import asyncio
import hashlib
import importlib.util
import json
import math
import os
from pathlib import Path
import platform
import statistics
import time


def positive(value):
    value = int(value)
    if not 1 <= value <= 1000000:
        raise argparse.ArgumentTypeError('expected integer in 1..1000000')
    return value


def nonnegative(value):
    value = float(value)
    if not math.isfinite(value) or value < 0:
        raise argparse.ArgumentTypeError('expected finite nonnegative percent')
    return value


def load(path, label):
    spec = importlib.util.spec_from_file_location('span_benchmark_' + label, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    module._logger.cache_clear()
    return module


def measure(module, iterations, asynchronous):
    if asynchronous:
        async def work():
            return None
        observed = module.observe('span-benchmark')(work)
        async def run():
            with module.log_context(request_id='benchmark-request', job_id='benchmark-job'):
                for _ in range(100):
                    await observed()
                started = time.perf_counter_ns()
                for _ in range(iterations):
                    await observed()
                return (time.perf_counter_ns() - started) / iterations
        return asyncio.run(run())
    def work():
        return None
    observed = module.observe('span-benchmark')(work)
    with module.log_context(request_id='benchmark-request', job_id='benchmark-job'):
        for _ in range(100):
            observed()
        started = time.perf_counter_ns()
        for _ in range(iterations):
            observed()
        return (time.perf_counter_ns() - started) / iterations


def summarize(values):
    ordered = sorted(values)
    return {
        'samples_ns_per_call': [round(v, 2) for v in values],
        'median_ns_per_call': round(statistics.median(values), 2),
        'p95_batch_mean_ns_per_call': round(ordered[math.ceil(0.95 * len(ordered)) - 1], 2),
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--module', type=Path, default=Path(__file__).resolve().parents[1] / 'scripts/gysam_diagnostics.py')
    parser.add_argument('--baseline', type=Path, help='Execute this trusted baseline source file for comparison')
    parser.add_argument('--baseline-revision', default=None)
    parser.add_argument('--iterations', type=positive, default=20000)
    parser.add_argument('--repeats', type=positive, default=7)
    parser.add_argument('--max-regression-percent', type=nonnegative,
                        help='Fail if either median exceeds baseline by this approved budget')
    args = parser.parse_args()
    if args.repeats > 31:
        parser.error('--repeats must be at most 31')
    if args.max_regression_percent is not None and args.baseline is None:
        parser.error('--max-regression-percent requires --baseline')
    os.environ['GYSAM_LOG_LEVEL'] = 'INFO'
    paths = {'candidate': args.module}
    if args.baseline:
        paths['baseline'] = args.baseline
    modules = {name: load(path, name) for name, path in paths.items()}
    result = {
        'schema_version': 1,
        'boundary': 'Local no-op synchronous/async call with request/job context; INFO filtering, no sink I/O',
        'measurement': 'Repeated batch means; p95 is across batches, not individual request latency',
        'python': platform.python_version(), 'platform': platform.system(),
        'architecture': platform.machine(), 'logical_cpus': os.cpu_count(),
        'iterations_per_batch': args.iterations, 'repeats': args.repeats,
        'baseline_revision': args.baseline_revision,
        'source_sha256': {name: hashlib.sha256(path.read_bytes()).hexdigest() for name, path in paths.items()},
        'max_regression_percent': args.max_regression_percent,
        'workloads': {},
    }
    regressed = False
    for workload, asynchronous in (('sync', False), ('async', True)):
        samples = {name: [] for name in modules}
        for repeat in range(args.repeats):
            order = list(modules) if repeat % 2 == 0 else list(reversed(modules))
            for name in order:
                samples[name].append(measure(modules[name], args.iterations, asynchronous))
        summary = {name: summarize(values) for name, values in samples.items()}
        if 'baseline' in samples:
            change = (statistics.median(samples['candidate']) / statistics.median(samples['baseline']) - 1) * 100
            summary['median_change_percent'] = round(change, 2)
            if args.max_regression_percent is not None and change > args.max_regression_percent:
                regressed = True
        result['workloads'][workload] = summary
    result['status'] = 'failed' if regressed else 'passed' if args.max_regression_percent is not None else 'measured'
    print(json.dumps(result, indent=2))
    return 1 if regressed else 0


if __name__ == '__main__':
    raise SystemExit(main())
