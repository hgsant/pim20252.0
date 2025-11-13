
from typing import List, Callable, Any, Optional

def merge_sort(seq: List[Any], key: Callable[[Any], Any] = lambda x: x) -> List[Any]:
    if len(seq) <= 1: return seq[:]
    mid = len(seq)//2
    left = merge_sort(seq[:mid], key)
    right = merge_sort(seq[mid:], key)
    return _merge(left, right, key)

def _merge(left: List[Any], right: List[Any], key: Callable[[Any], Any]) -> List[Any]:
    i = j = 0
    out = []
    while i < len(left) and j < len(right):
        if key(left[i]) <= key(right[j]):
            out.append(left[i]); i += 1
        else:
            out.append(right[j]); j += 1
    out.extend(left[i:]); out.extend(right[j:])
    return out

def binary_search(sorted_seq: List[Any], target_key, key: Callable[[Any], Any] = lambda x: x) -> Optional[Any]:
    lo, hi = 0, len(sorted_seq)-1
    while lo <= hi:
        mid = (lo+hi)//2
        km = key(sorted_seq[mid])
        if km == target_key: return sorted_seq[mid]
        if km < target_key: lo = mid+1
        else: hi = mid-1
    return None

def build_index(seq: List[Any], key: Callable[[Any], Any] = lambda x: x) -> dict:
    idx = {}
    for item in seq:
        idx[key(item)] = item
    return idx
