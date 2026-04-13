# LC 704: Binary Search

## Problem
Given an array of integers `nums` sorted in ascending order and a target value `target`, write a function to search `target` in `nums`.

If the target exists, return its index. Otherwise, return `-1`.

You must write an algorithm with `O(log n)` runtime complexity.

**Example:**
```
Input: nums = [-1,0,3,5,9,12], target = 9
Output: 4
```

---

## Approach

**Standard Binary Search:**

1. Start with `low = 0` and `high = len(nums) - 1`.
2. While `low <= high`:
   - Compute `mid = (low + high) // 2`.
   - If `nums[mid] == target`, return `mid`.
   - If `nums[mid] < target`, move `low` to `mid + 1`.
   - If `nums[mid] > target`, move `high` to `mid - 1`.
3. If the loop exits without finding `target`, return `-1`.

---

## 🧠 Binary Search Solution

```python
def search(nums: List[int], target: int) -> int:
    low, high = 0, len(nums) - 1

    while low <= high:
        mid = (low + high) // 2
        if nums[mid] == target:
            return mid
        if nums[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1
```

**Complexity:**
- **Time:** O(log n)
- **Space:** O(1)

## 📊 Metrics

| Metric | Value |
|--------|-------|
| **Date Solved** | Apr 13, 2026 |
| **Difficulty** | Easy |
| **Status** | ✅ Solved |
| **Planning Time** | 5 min |
| **Coding Time** | 8 min |
| **Testing Time** | 7 min |
| **Total Time** |20 min |
| **Submission** | 1st Attempt |
