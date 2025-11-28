import heapq
from typing import List


def merge_k_lists(lists: List[List[int]]) -> List[int]:
    """
    Merge k sorted lists into a single sorted list using a min-heap.
    Time complexity: O(n log k)
    """
    heap = []
    result = []

    # Initialize heap with the first element from each list
    for list_idx, lst in enumerate(lists):
        if lst:
            heapq.heappush(heap, (lst[0], list_idx, 0))

    # Extract min element and add next element from the same list
    while heap:
        val, list_idx, elem_idx = heapq.heappop(heap)
        result.append(val)

        next_idx = elem_idx + 1
        if next_idx < len(lists[list_idx]):
            heapq.heappush(heap, (lists[list_idx][next_idx], list_idx, next_idx))

    return result


if __name__ == "__main__":
    input_list = [[1, 4, 5], [1, 3, 4], [2, 6]]
    print("Input:", input_list)
    print("Merged:", merge_k_lists(input_list))
