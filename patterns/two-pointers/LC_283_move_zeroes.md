# LC 283: Move Zeroes

## Problem
Given an integer array `nums`, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

**Note:** You must do this in-place without making a copy of the array.

**Example:**
```
Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]
```

---

## Approach

**Two Pointer Technique:**

1. Use two pointers: one to track current position, another to track where next non-zero should go
2. Iterate through array, when non-zero found, swap with position at "next non-zero" pointer
3. Increment both pointers when swap occurs, only current pointer when zero encountered

---

## 🐢 Two Pointer Solution

**Idea:** Maintain relative order by swapping non-zeros to front
```python
def moveZeroes(nums: List[int]) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    # Pointer for next non-zero position
    next_non_zero = 0
    
    # Iterate through array
    for current in range(len(nums)):
        if nums[current] != 0:
            # Swap with next non-zero position
            nums[next_non_zero], nums[current] = nums[current], nums[next_non_zero]
            next_non_zero += 1
```

**Complexity:**
- **Time:** O(n) - single pass through array
- **Space:** O(1) - in-place modification

## 📊 Metrics

| Metric | Value |
|--------|-------|
| **Date Solved** | Apr 7, 2026 |
| **Difficulty** | easy |
| **Status** | ✅ Solved |
| **Planning Time** | 5 min |
| **Coding Time** | 8 min |
| **Testing Time** | 3 min |
| **Total Time** | 16 min |
| **Submission** | 1st Attempt |