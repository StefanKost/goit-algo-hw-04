import random
import timeit
from typing import Callable, List

from sorting_algorithms import insertion_sort, merge_sort


# Build in Timsort algorithm
def tim_sorted(arr: List[float]) -> List[float]:
    return sorted(arr)


def tim_sort(arr: List[float]) -> List[float]:
    arr = arr.copy()
    arr.sort()
    return arr


# Algorithms to benchmark
ALGORITHMS = {
    "Insertion Sort": insertion_sort,
    "Merge Sort": merge_sort,
    "Py (Timsort) sorted()": tim_sorted,
    "Py (Timsort) .sort()": tim_sort,
}

# Dataset sizes and benchmark parameters
SIZES = [100, 2_000, 6_000, 10_000]
ITERATIONS = 8


def generate_data(size: int) -> List[float]:
    """Generate a random list of floats."""
    return [random.uniform(0, size) for _ in range(size)]


def measure_time(func: Callable, data: List[float], iterations: int) -> float:
    """Measure execution time of an algorithm over multiple iterations."""
    start = timeit.default_timer()
    for _ in range(iterations):
        func(data.copy())
    return timeit.default_timer() - start


def sanity_check() -> None:
    """Ensure all algorithms sort correctly."""
    test = [5, 3, 1, 4, 2]
    for name, alg in ALGORITHMS.items():
        assert alg(test.copy()) == sorted(test), f"{name} FAILED correctness test"


def run_benchmark() -> None:
    sanity_check()

    divider = "-" * 42

    print(divider)
    print(f" ITERATIONS: {ITERATIONS}")
    print(divider)

    for size in SIZES:
        original = generate_data(size)
        print("\n" + divider)
        print(f" Size: {size:,}")
        print(divider)

        for name, algorithm in ALGORITHMS.items():
            time_taken = measure_time(algorithm, original, ITERATIONS)
            print(f"{name:<25} {time_taken:>12.6f} s")


if __name__ == "__main__":
    run_benchmark()
