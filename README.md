# goit-algo-hw-04
Sorting algorithms

## Task 1
Compare sorting algorithms: Insertion Sort O(n²), Merge Sort O(n log n), Timsort O(n log n).

Run benchmark
```bash
python sorting_benchmark.py
```

![Benchmark Results](https://github.com/user-attachments/assets/3ab0fcac-e037-4d97-9dc0-2d560c2d09ab)

The results of the benchmark clearly illustrate the differences in performance between the sorting algorithms and confirm theoretical expectations:

1. Insertion Sort
   - Extremely fast on very small datasets (e.g., 100 elements: 0.001 s).
   - Performance deteriorates rapidly on larger datasets:
     - `100` elements → `0.001`s
     - `2,000` elements → `0.42`s
     - `6,000` elements → `3.79`s
     - `10,000` elements → `10.46`s
   - This exponential growth of execution time is consistent with its `O(n²)` complexity.
   - **Complexity verification:** When execution times are divided by `n²` the normalized values remain roughly constant, empirically confirming the quadratic time complexity.
   - **Conclusion:** Insertion Sort is suitable only for small or nearly sorted arrays. It is impractical for medium or large datasets.
2. Merge Sort
   - Shows stable and predictable growth:
     - `100` elements → `0.00066`s
     - `10,000` elements → `0.11`s
   - Execution time scales roughly with `O(n log n)`, confirming theoretical expectations.
   - Merge Sort is much faster than Insertion Sort for medium and large datasets, but slightly slower than Timsort on small datasets due to fixed recursive overhead.
   - **Complexity verification:** Normalizing execution time by `n log n` produces nearly constant values across dataset sizes, confirming the expected logarithmic scaling.
   - **Conclusion:** Merge Sort is a reliable general-purpose sorting algorithm with predictable performance.
3. Python’s Timsort (sorted() and .sort())
   - Extremely fast across all dataset sizes:
     - `100` elements → `0.00003`s
     - `10,000` elements → `0.0063`s
   - Advantages over custom implementations:
     - Combines insertion sort on small “runs” and merge sort on larger blocks.
     - Adaptive: detects partially sorted sequences, reducing unnecessary operations.
     - Highly optimized in C for minimal memory operations and fast comparisons.
     - Minor difference between `sorted()` and `.sort()`: `.sort()` is slightly faster because it sorts in-place, avoiding the creation of a new list.
   - **Complexity verification:** Empirical measurements confirm near O(n log n) scaling, even on large datasets.
   - **Conclusion:** Timsort is the most efficient algorithm in practice, significantly outperforming both Insertion and Merge Sort, especially for large or partially sorted datasets.

### General Observations
- Small arrays favor algorithms with minimal overhead.
- Medium arrays clearly show the difference between `O(n²)` and `O(n log n)` algorithms.
- Large arrays demonstrate the efficiency of hybrid approaches and why Python’s built-in sort is preferred in real-world applications.
- Empirical results align perfectly with theoretical time complexities, reinforcing the understanding of algorithm efficiency in practice.

### Final Takeaway
While custom sorting algorithms like Insertion and Merge Sort are excellent for learning and experimentation,
Python’s built-in Timsort provides unmatched performance due to its hybrid and adaptive design.
Complexity verification confirms that the empirical growth of execution time matches theoretical expectations:
`O(n²)` for Insertion Sort and `O(n log n)` for Merge Sort and Timsort.
For real-world applications, using `sorted()` or `.sort()` is strongly recommended.

## Task 2
Merge list of sorted lists into one list:
```bash
python sorting_benchmark.py
```
