# LC 34: Find First and Last Position of Target in Sorted Array

## Problem
Given an array of integers `nums` sorted in ascending order and a target value `target`, return the starting and ending position of `target` in `nums`.

If `target` is not found, return `[-1, -1]`.

**Example:**
```
Input: nums = [5,7,7,8,8,10], target = 8
Output: [3, 4]
```

---

## Approach

**Binary Search for First and Last Occurrence:**

1. Use binary search to find the first index where `nums[mid] == target`.
2. Use binary search to find the last index where `nums[mid] == target`.
3. Return `[first, last]` if found, otherwise return `[-1, -1]`.

This keeps the algorithm in `O(log n)` and avoids scanning linearly.

---

## 🧠 Binary Search Solution

```python
from typing import List

def search_range(nums: List[int], target: int) -> List[int]:
    def find_first() -> int:
        low, high = 0, len(nums) - 1
        first = -1

        while low <= high:
            mid = low + (high - low) // 2
            if nums[mid] == target:
                first = mid
                high = mid - 1
            elif nums[mid] < target:
                low = mid + 1
            else:
                high = mid - 1

        return first

    def find_last() -> int:
        low, high = 0, len(nums) - 1
        last = -1

        while low <= high:
            mid = low + (high - low) // 2
            if nums[mid] == target:
                last = mid
                low = mid + 1
            elif nums[mid] < target:
                low = mid + 1
            else:
                high = mid - 1

        return last

    first = find_first()
    if first == -1:
        return [-1, -1]

    return [first, find_last()]
```

**Why it works:**
- The first search finds the earliest index where `nums[i] >= target`.
- The second search finds the earliest index where `nums[i] > target`.
- The target range is therefore `[left, right]`.

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
