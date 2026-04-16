# Find Minimum in Rotated Sorted Array

## Problem
Given a rotated sorted array of unique integers `nums`, return the minimum element.

The array was originally sorted in ascending order, then rotated at some pivot.

**Example:**
```
Input: nums = [3,4,5,1,2]
Output: 1
```

---

## Approach

**Binary Search on the Pivot:**

1. Use binary search with `low` and `high` pointers.
2. At each step, compare `nums[mid]` with `nums[high]`.
3. If `nums[mid] > nums[high]`, the minimum lies to the right of `mid`.
4. Otherwise, the minimum lies at `mid` or to the left.
5. When `low == high`, that index is the minimum.

This locates the pivot in `O(log n)` time.

---

## 🧠 Binary Search Solution

```python
from typing import List

def find_min_in_rotated(nums: List[int]) -> int:
    low, high = 0, len(nums) - 1

    while low < high:
        mid = low + (high - low) // 2
        if nums[mid] > nums[high]:
            low = mid + 1
        else:
            high = mid

    return nums[low]
```

**Why it works:**
- If `nums[mid] > nums[high]`, the pivot is to the right because the smallest element is in the unsorted suffix.
- Otherwise, the pivot is at `mid` or left of `mid`.
- The search reduces the candidate range by half each iteration.

**Complexity:**
- **Time:** O(log n)
- **Space:** O(1)

## 📊 Metrics

| Metric | Value |
|--------|-------|
| **Date Solved** | Apr 16, 2026 |
| **Difficulty** | Easy |
| **Status** | ✅ Solved |
| **Planning Time** | 3 min |
| **Coding Time** | 8 min |
| **Testing Time** | 5 min |
| **Total Time** |16 min |
| **Submission** | 1st Attempt |
