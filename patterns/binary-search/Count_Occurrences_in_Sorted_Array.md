# Count Occurrences in Sorted Array

## Problem
Given a sorted array of integers `nums` and a target value `target`, return the number of times `target` appears in `nums`.

If `target` is not present, return `0`.

**Example:**
```
Input: nums = [1,2,2,2,3,4], target = 2
Output: 3
```

---

## Approach

**Binary Search for First and Last Occurrence:**

1. Use binary search to find the first index where `nums[mid] == target`.
2. Use binary search to find the last index where `nums[mid] == target`.
3. If the target is not found, return `0`.
4. Otherwise, return `last - first + 1`.

This uses two binary searches and runs in `O(log n)` time.

---

## 🧠 Binary Search Solution

```python
from typing import List

def count_occurrences(nums: List[int], target: int) -> int:
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
        return 0

    return find_last() - first + 1
```

**Why it works:**
- `lower_bound(target)` finds the first index where `nums[i] >= target`.
- `lower_bound(target + 1)` finds the first index where `nums[i] > target`.
- Subtracting the two gives the number of occurrences.

**Complexity:**
- **Time:** O(log n)
- **Space:** O(1)

## 📊 Metrics

| Metric | Value |
|--------|-------|
| **Date Solved** | Apr 16, 2026 |
| **Difficulty** | Easy |
| **Status** | ✅ Solved |
| **Planning Time** | 5 min |
| **Coding Time** | 10 min |
| **Testing Time** | 8 min |
| **Total Time** |23 min |
| **Submission** | 1st Attempt |
