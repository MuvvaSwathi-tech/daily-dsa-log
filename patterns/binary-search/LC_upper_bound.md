# Upper Bound (First Element > Target)

## Problem
Given a sorted array of integers `nums` and a target value `target`, find the smallest index `i` such that `nums[i] > target`.

If all elements are less than or equal to `target`, return `len(nums)`.

**Example:**
```
Input: nums = [1,2,4,4,5], target = 4
Output: 4
```

---

## Approach

**Binary Search for Upper Bound:**

1. Initialize `low = 0` and `high = len(nums)`.
2. While `low < high`:
   - Compute `mid = (low + high) // 2`.
   - If `nums[mid] <= target`, move `low = mid + 1`.
   - Otherwise, move `high = mid`.
3. When the loop ends, `low` is the first index where `nums[low] > target`, or `len(nums)` if no such index exists.

---

## 🧠 Binary Search Solution

```python
from typing import List

def upper_bound(nums: List[int], target: int) -> int:
    low, high = 0, len(nums)

    while low <= high:
        mid = (low + high) // 2
        if nums[mid] <= target:
            low = mid + 1
        else:
            high = mid

    return low
```

**Why it works:**
- The loop preserves the invariant that the upper bound is in the range `[low, high)`.
- When `nums[mid] <= target`, the answer must be strictly to the right of `mid`.
- When `nums[mid] > target`, the answer may be `mid` or to its left.

**Complexity:**
- **Time:** O(log n)
- **Space:** O(1)

## 📊 Metrics

| Metric | Value |
|--------|-------|
| **Date Solved** | Apr 14, 2026 |
| **Difficulty** | Easy |
| **Status** | ✅ Solved |
| **Planning Time** | 5 min |
| **Coding Time** | 8 min |
| **Testing Time** | 5 min |
| **Total Time** |18 min |
| **Submission** | 1st Attempt |
