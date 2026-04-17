# LC 33 Search in Rotated Sorted Array

## Problem
Given an integer array `nums` sorted in ascending order, rotated at an unknown pivot, and a target value `target`, return the index of `target` if it exists in `nums`. If it does not exist, return `-1`.

You must write an algorithm with `O(log n)` runtime complexity.

**Example:**
```
Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4
```

---

## Approach

**Rotate-aware binary search:**

1. Use a modified binary search on the entire array.
2. At each step, determine which half is sorted:
   - left half is sorted if `nums[left] <= nums[mid]`
   - otherwise, right half is sorted.
3. Check whether `target` lies within the sorted half.
4. Narrow the search range into the half that may contain `target`.
5. Repeat until `target` is found or the range is empty.

This keeps the runtime at `O(log n)` because each step discards half of the search space.

---

## 🧠 Binary Search Solution

```python
from typing import List


def search_rotated(nums: List[int], target: int) -> int:
    left, right = 0, len(nums) - 1

    while left <= right:
        mid = left + (right - left) // 2
        if nums[mid] == target:
            return mid

        if nums[left] <= nums[mid]:
            # Left half is sorted
            if nums[left] <= target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        else:
            # Right half is sorted
            if nums[mid] < target <= nums[right]:
                left = mid + 1
            else:
                right = mid - 1

    return -1
```

**Why it works:**
- A rotated sorted array always keeps one half sorted.
- The algorithm decides which half is ordered, then checks if `target` falls inside that half.
- If not, it searches the other half.
- This ensures the search range halves every iteration.

**Complexity:**
- **Time:** O(log n)
- **Space:** O(1)

## 📊 Metrics

| Metric | Value |
|--------|-------|
| **Date Solved** | Apr 17, 2026 |
| **Difficulty** | Medium |
| **Status** | ✅ Solved |
| **Planning Time** | 4 min |
| **Coding Time** | 8 min |
| **Testing Time** | 6 min |
| **Total Time** |18 min |
| **Submission** | 1st Attempt |
