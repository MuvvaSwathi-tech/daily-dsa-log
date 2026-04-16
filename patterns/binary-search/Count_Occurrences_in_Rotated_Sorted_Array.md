# Count Occurrences in Rotated Sorted Array

## Problem
Given a rotated sorted array of integers `nums` and a target value `target`, return the number of times `target` appears in `nums`.

If `target` is not present, return `0`.

**Example:**
```
Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 1
```

---

## Approach

**Rotate-aware binary search:**

1. Find the pivot index where the array rotation begins (the smallest element).
2. Determine which sorted half of the rotated array can contain `target`.
3. Use binary search in that sorted half to find the first occurrence.
4. Use binary search in that same half to find the last occurrence.
5. Return `last - first + 1`, or `0` if the target is absent.

This is still `O(log n)` time because the pivot search and the two boundary searches are all binary search operations.

---

## 🧠 Binary Search Solution

```python
from typing import List

def count_occurrences_rotated(nums: List[int], target: int) -> int:
    if not nums:
        return 0

    def find_pivot() -> int:
        low, high = 0, len(nums) - 1

        while low < high:
            mid = low + (high - low) // 2
            if nums[mid] > nums[high]:
                low = mid + 1
            else:
                high = mid

        return low

    def search_first(left: int, right: int) -> int:
        idx = -1
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                idx = mid
                right = mid - 1
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return idx

    def search_last(left: int, right: int) -> int:
        idx = -1
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                idx = mid
                left = mid + 1
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return idx

    pivot = find_pivot()
    n = len(nums)

    if nums[pivot] <= target <= nums[n - 1]:
        left, right = pivot, n - 1
    else:
        left, right = 0, pivot - 1

    first = search_first(left, right)
    if first == -1:
        return 0

    last = search_last(left, right)
    return last - first + 1
```

**Why it works:**
- The rotated array is composed of two sorted subarrays separated at the pivot.
- After locating the pivot, the correct half is chosen by comparing with the endpoints.
- Then the standard first/last occurrence binary search gives the count.

**Complexity:**
- **Time:** O(log n)
- **Space:** O(1)

## 📊 Metrics

| Metric | Value |
|--------|-------|
| **Date Solved** | Apr 16, 2026 |
| **Difficulty** | Medium |
| **Status** | ✅ Solved |
| **Planning Time** | 5 min |
| **Coding Time** | 12 min |
| **Testing Time** | 10 min |
| **Total Time** |27 min |
| **Submission** | 1st Attempt |
