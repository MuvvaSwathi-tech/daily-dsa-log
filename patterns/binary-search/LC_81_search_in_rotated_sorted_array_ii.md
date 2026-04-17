# LC 81 Search in Rotated Sorted Array II

## Problem
Given an integer array `nums` sorted in ascending order, rotated at an unknown pivot, and a target value `target`, return `true` if `target` is in `nums`, or `false` otherwise.

The array may contain duplicates. You must write an algorithm with average `O(log n)` runtime, but worst-case may degrade to `O(n)` due to duplicates.

**Example:**
```
Input: nums = [2,5,6,0,0,1,2], target = 0
Output: true
```

---

## Approach

**Duplicate-aware rotated binary search:**

1. Use binary search on the entire array.
2. If `nums[mid] == target`, return `true` immediately.
3. If the values at `left`, `mid`, and `right` are equal, increment `left` and decrement `right` to skip duplicates.
4. Otherwise, determine which half is sorted:
   - left half sorted when `nums[left] <= nums[mid]`
   - else right half sorted
5. Check if `target` lies within the sorted half. If it does, narrow search to that half; otherwise search the other half.
6. Repeat until the search window closes.

This handles duplicates while preserving binary search when one sorted half is identifiable.

---

## 🧠 Binary Search Solution

```python
from typing import List


def search_rotated_with_duplicates(nums: List[int], target: int) -> bool:
    left, right = 0, len(nums) - 1

    while left <= right:
        mid = left + (right - left) // 2
        if nums[mid] == target:
            return True

        if nums[left] == nums[mid] == nums[right]:
            left += 1
            right -= 1
        elif nums[left] <= nums[mid]:
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

    return False
```

**Why it works:**
- In a rotated sorted array with duplicates, one half is still sorted unless duplicates hide the boundary.
- When `nums[left]`, `nums[mid]`, and `nums[right]` are equal, the sorted half cannot be determined, so we shrink the window safely.
- Once the sorted half is known, normal rotated binary search rules apply.
- Worst-case time becomes `O(n)` only when duplicates force repeated boundary shrinking.

**Complexity:**
- **Average time:** O(log n)
- **Worst-case time:** O(n)
- **Space:** O(1)

## 📊 Metrics

| Metric | Value |
|--------|-------|
| **Date Solved** | Apr 17, 2026 |
| **Difficulty** | Medium |
| **Status** | ✅ Solved |
| **Planning Time** | 4 min |
| **Coding Time** | 9 min |
| **Testing Time** | 7 min |
| **Total Time** |20 min |
| **Submission** | 1st Attempt |
