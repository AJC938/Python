"""
hash_table.py
-------------
Custom hash table with separate chaining, polynomial rolling hash,
and automatic resize at load factor 0.75.

Big-O:
    insert / search / delete : O(1) average, O(n) worst case
    space                    : O(n + m), m = bucket count
"""

from typing import Any, Iterator, List, Optional, Tuple


class HashTable:
    """Separate-chaining hash table keyed by string IDs."""

    _INITIAL_CAPACITY = 16
    _LOAD_FACTOR_THRESHOLD = 0.75

    def __init__(self) -> None:
        self._capacity: int = self._INITIAL_CAPACITY
        self._size: int = 0
        self._buckets: List[List[Tuple[str, Any]]] = [
            [] for _ in range(self._capacity)
        ]

    def _hash(self, key: str) -> int:
        """Polynomial rolling hash, multiplier 31, masked to 32 bits."""
        h = 0
        for ch in key:
            h = (h * 31 + ord(ch)) & 0xFFFFFFFF
        return h % self._capacity

    def _resize(self) -> None:
        old_buckets = self._buckets
        self._capacity *= 2
        self._buckets = [[] for _ in range(self._capacity)]
        self._size = 0
        for bucket in old_buckets:
            for key, value in bucket:
                self.insert(key, value)

    def insert(self, key: str, value: Any) -> None:
        idx = self._hash(key)
        bucket = self._buckets[idx]
        for i, (k, _) in enumerate(bucket):
            if k == key:
                bucket[i] = (key, value)
                return
        bucket.append((key, value))
        self._size += 1
        if self._size / self._capacity > self._LOAD_FACTOR_THRESHOLD:
            self._resize()

    def search(self, key: str) -> Optional[Any]:
        idx = self._hash(key)
        for k, v in self._buckets[idx]:
            if k == key:
                return v
        return None

    def delete(self, key: str) -> bool:
        idx = self._hash(key)
        bucket = self._buckets[idx]
        for i, (k, _) in enumerate(bucket):
            if k == key:
                bucket.pop(i)
                self._size -= 1
                return True
        return False

    def __contains__(self, key: str) -> bool:
        return self.search(key) is not None

    def __len__(self) -> int:
        return self._size

    def __iter__(self) -> Iterator[Any]:
        for bucket in self._buckets:
            for _, value in bucket:
                yield value

    def load_factor(self) -> float:
        return self._size / self._capacity

    def collision_count(self) -> int:
        return sum(max(0, len(b) - 1) for b in self._buckets)

    def stats(self) -> dict:
        return {
            "capacity": self._capacity,
            "size": self._size,
            "load_factor": round(self.load_factor(), 3),
            "collisions": self.collision_count(),
        }
