# LC 35: Search Insert Position

## Problem
Given a sorted array of distinct integers `nums` and a target value `target`, return the index if the target is found.

If not, return the index where it would be if it were inserted in order.

You must write an algorithm with `O(log n)` runtime complexity.

**Example:**
```
Input: nums = [1,3,5,6], target = 5
Output: 2
```

---

## Approach

**Binary Search:**

1. Maintain `low` and `high` pointers over the sorted array.
2. Compute `mid = (low + high) // 2`.
3. If `nums[mid] == target`, return `mid`.
4. If `nums[mid] < target`, search the right half and set `low = mid + 1`.
5. If `nums[mid] > target`, search the left half and set `high = mid - 1`.
6. If the loop ends without finding the target, `low` is the insertion index.

---

## 🧠 Binary Search Solution

```python
def searchInsert(nums: List[int], target: int) -> int:
    low, high = 0, len(nums) - 1

    while low <= high:
        mid = (low + high) // 2
        if nums[mid] == target:
            return mid
        if nums[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return high+1
```

**Why `low`?**
- When the target is not present, `low` ends at the smallest index where the target can be inserted while preserving order.

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
