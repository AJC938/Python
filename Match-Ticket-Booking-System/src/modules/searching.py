"""
searching.py
------------
Three search variants used by the lookup panel and KPI benchmark.
"""

from typing import List, Optional


def linear_search(users: List, user_id: str) -> Optional[object]:
    """O(n) scan, O(1) extra space."""
    for u in users:
        if u.user_id == user_id:
            return u
    return None


def hash_search(table, user_id: str) -> Optional[object]:
    """O(1) average via HashTable.search."""
    return table.search(user_id)


def binary_search(sorted_users: List, user_id: str) -> Optional[object]:
    """O(log n) on a list pre-sorted by user_id."""
    lo, hi = 0, len(sorted_users) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if sorted_users[mid].user_id == user_id:
            return sorted_users[mid]
        if sorted_users[mid].user_id < user_id:
            lo = mid + 1
        else:
            hi = mid - 1
    return None
