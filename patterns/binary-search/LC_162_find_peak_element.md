# LC 162: Find Peak Element

## Problem
A peak element is an element that is strictly greater than its neighbors.

Given an integer array `nums`, find a peak element, and return its index. If the array contains multiple peaks, return the index to any of the peaks.

You may imagine that `nums[-1] = nums[n] = -∞`. In other words, an element is always considered to be strictly greater than a neighbor that is outside the array.

You must write an algorithm that runs in `O(log n)` time.

**Example:**
```
Input: nums = [1,2,3,1]
Output: 2
Explanation: 3 is a peak element and your function should return the index number 2.
```

---

## Approach

**Binary search on the array:**

1. Use binary search on the index range from 0 to len(nums) - 1.
2. At each step, compute `mid = left + (right - left) // 2`.
3. Compare `nums[mid]` with `nums[mid + 1]`:
   - If `nums[mid] < nums[mid + 1]`, then the peak must be on the right side (since the array is increasing at mid, and we can always find a peak to the right due to the -∞ at the end).
   - Otherwise, the peak is on the left side (including mid, since mid could be a peak).
4. Narrow the search range accordingly until `left == right`.

This works because the problem guarantees a peak exists, and binary search efficiently finds one by always moving towards the side that must contain a peak.

---

## 🧠 Binary Search Solution

```python
from typing import List


def find_peak_element(nums: List[int]) -> int:
    left, right = 0, len(nums) - 1

    while left < right:
        mid = left + (right - left) // 2

        if nums[mid] < nums[mid + 1]:
            # Peak is on the right
            left = mid + 1
        else:
            # Peak is on the left (including mid)
            right = mid

    return left
```

**Why it works:**
- The array has imaginary -∞ at both ends, ensuring a peak exists.
- By comparing mid with mid+1, we decide which half must contain a peak.
- If increasing, right half has a peak; if not, left half (including mid) has a peak.
- Converges to a peak index.

**Complexity:**
- **Time:** O(log n)
- **Space:** O(1)

## 📊 Metrics

| Metric | Value |
|--------|-------|
| **Date Solved** | Apr 19, 2026 |
| **Difficulty** | Medium |
| **Status** | ✅ Solved |
| **Planning Time** | 5 min |
| **Coding Time** | 8 min |
| **Testing Time** | 5 min |
| **Total Time** |18 min |
| **Submission** | 1st Attempt |