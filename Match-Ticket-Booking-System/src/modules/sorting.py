"""
sorting.py
----------
Two sorting algorithms used by the benchmark layer.
"""

from typing import Callable, List, TypeVar

T = TypeVar("T")


def merge_sort(arr: List[T], key: Callable[[T], float],
               descending: bool = True) -> List[T]:
    """Classic stable merge sort: O(n log n) time, O(n) auxiliary space."""
    if len(arr) <= 1:
        return arr[:]
    mid = len(arr) // 2
    left = merge_sort(arr[:mid], key, descending)
    right = merge_sort(arr[mid:], key, descending)
    return _merge(left, right, key, descending)


def _merge(left: List[T], right: List[T],
           key: Callable[[T], float], descending: bool) -> List[T]:
    out: List[T] = []
    i = j = 0
    while i < len(left) and j < len(right):
        a = key(left[i])
        b = key(right[j])
        take_left = (a > b) if descending else (a < b)
        if take_left or a == b:
            out.append(left[i])
            i += 1
        else:
            out.append(right[j])
            j += 1
    out.extend(left[i:])
    out.extend(right[j:])
    return out


def bubble_sort(arr: List[T], key: Callable[[T], float],
                descending: bool = True) -> List[T]:
    """O(n^2) baseline for the speed comparison."""
    a = arr[:]
    n = len(a)
    for i in range(n - 1):
        swapped = False
        for j in range(n - 1 - i):
            cond = ((key(a[j]) < key(a[j + 1])) if descending
                    else (key(a[j]) > key(a[j + 1])))
            if cond:
                a[j], a[j + 1] = a[j + 1], a[j]
                swapped = True
        if not swapped:
            break
    return a


def sort_users_by_attendance(users: List, descending: bool = True,
                             algorithm: str = "merge") -> List:
    fn = merge_sort if algorithm == "merge" else bubble_sort
    return fn(users, key=lambda u: u.attendance, descending=descending)
