# LC 27: Remove Element

## Problem
Given an integer array `nums` and an integer `val`, remove all occurrences of `val` in `nums` **in-place**. The order of the elements may be changed. Then return the number of elements in `nums` which are not equal to `val`.

Consider the number of elements in `nums` which are not equal to `val` be `k`, to get accepted, you need to do the following things:

- Change the array `nums` such that the first `k` elements of `nums` contain the elements which are not equal to `val`. The remaining elements of `nums` are not important as well as the size of `nums`.
- Return `k`.

**Example:**
```
Input: nums = [3,2,2,3], val = 3
Output: 2, nums = [2,2,_,_]
Explanation: Your function should return k = 2, with the first two elements of nums being 2.
It does not matter what you leave beyond the returned k (hence they are underscores).
```

---

## Approach

**Two Pointer Technique:**

1. Use two pointers: one to track position for non-val elements, one to iterate
2. When current element is not equal to val, copy it to the "next position" and increment
3. When current element equals val, skip it (don't copy, don't increment position)

---

## 🐢 Two Pointer Solution

**Idea:** Overwrite elements equal to val with elements not equal to val
```python
def removeElement(nums: List[int], val: int) -> int:
    # Pointer for next position to place non-val element
    next_pos = 0
    
    # Iterate through array
    for current in range(len(nums)):
        if nums[current] != val:
            # Place non-val element at next position
            nums[next_pos] = nums[current]
            next_pos += 1
    
    # Return count of non-val elements
    return next_pos
```

**Complexity:**
- **Time:** O(n) - single pass through array
- **Space:** O(1) - in-place modification

## 📊 Metrics

| Metric | Value |
|--------|-------|
| **Date Solved** | Apr 8, 2026 |
| **Difficulty** | Easy |
| **Status** | ✅ Solved |
| **Planning Time** | 5 min |
| **Coding Time** | 10 min |
| **Testing Time** | 10 min |
| **Total Time** |25 min |
| **Submission** | 1st Attempt |
