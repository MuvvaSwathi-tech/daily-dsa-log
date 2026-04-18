# LC 540: Single Element in a Sorted Array

## Problem
Given a sorted array of integers `nums` where every element appears exactly twice except for one element which appears exactly once, return the single element that appears only once.

The solution must run in `O(log n)` time and `O(1)` space.

**Example:**
```
Input: nums = [1,1,2,3,3,4,4,8,8]
Output: 2
```

---

## Approach

**Binary search using pair parity:**

1. Use binary search on the index range.
2. At each step, compute `mid = left + (right - left) // 2`.
3. Pair alignment rule:
   - If `mid` is even, the duplicate should start at `mid` when the single element is on the right.
   - If `mid` is odd, the duplicate should start at `mid - 1` when the single element is on the right.
4. Compare `nums[mid]` with its adjacent pair element:
   - If `mid` is even and `nums[mid] == nums[mid + 1]`, the single element is to the right.
   - If `mid` is odd and `nums[mid] == nums[mid - 1]`, the single element is to the right.
   - Otherwise, the single element is at `mid` or to the left.
5. Narrow the search range accordingly until `left == right`.

This works because all paired elements before the single element preserve the correct even/odd alignment, while the alignment flips after the single element.

---

## 🧠 Binary Search Solution

```python
from typing import List


def single_non_duplicate(nums: List[int]) -> int:
    left, right = 0, len(nums) - 1

    while left < right:
        mid = left + (right - left) // 2

        # Ensure mid is even for pair comparison
        if mid % 2 == 1:
            mid -= 1

        if nums[mid] == nums[mid + 1]:
            left = mid + 2
        else:
            right = mid

    return nums[left]
```

**Why it works:**
- In the left half before the single element, pairs start at even indices.
- After the single element, pairs begin at odd indices.
- By forcing `mid` to even and checking the adjacent pair, we can decide whether the single element is left or right of `mid`.

**Complexity:**
- **Time:** O(log n)
- **Space:** O(1)

## 📊 Metrics

| Metric | Value |
|--------|-------|
| **Date Solved** | Apr 18, 2026 |
| **Difficulty** | Medium |
| **Status** | ✅ Solved |
| **Planning Time** | 5 min |
| **Coding Time** | 8 min |
| **Testing Time** | 5 min |
| **Total Time** |18 min |
| **Submission** | 1st Attempt |
