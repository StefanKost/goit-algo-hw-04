from typing import List, TypeVar

T = TypeVar("T")


def insertion_sort(arr: List[T]) -> List[T]:
    """
    Insertion sort algorithm.
    """
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1

        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = key

    return arr


def merge_sort(arr: List[T]) -> List[T]:
    """
    Merge sort algorithm.
    """
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2

    # Recursively split the array into two halves.
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    # Merge the sorted halves.
    return __merge(left, right)


def __merge(left: List[T], right: List[T]) -> List[T]:
    """
    Merge two sorted lists into a single sorted list.
    """
    merged = []
    i = j = 0

    # Compare elements from both lists and append the smallest.
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1

    merged.extend(left[i:])
    merged.extend(right[j:])

    return merged
