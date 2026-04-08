# LC 26: Remove Duplicates from Sorted Array

## Problem
Given an integer array `nums` sorted in non-decreasing order, remove the duplicates **in-place** such that each unique element appears only once. The relative order of the elements should be kept the same. Then return the number of unique elements in `nums`.

Consider the number of unique elements of `nums` to be `k`, to get accepted, you need to do the following things:

- Change the array `nums` such that the first `k` elements of `nums` contain the unique elements in the order they were present in `nums` initially. The remaining elements of `nums` are not important as well as the size of `nums`.
- Return `k`.

**Example:**
```
Input: nums = [1,1,2]
Output: 2, nums = [1,2,_]
Explanation: Your function should return k = 2, with the first two elements of nums being 1 and 2 respectively.
It does not matter what you leave beyond the returned k (hence they are underscores).
```

---

## Approach

**Two Pointer Technique:**

1. Use two pointers: one slow pointer to track unique elements, one fast pointer to iterate
2. When fast pointer finds a different element than slow pointer, copy it to slow+1 position
3. Increment slow pointer only when unique element found

---

## 🐢 Two Pointer Solution

**Idea:** Use slow and fast pointers to overwrite duplicates
```python
def removeDuplicates(nums: List[int]) -> int:
    if not nums:
        return 0
    
    # Slow pointer for unique elements
    slow = 0
    
    # Fast pointer to iterate
    for fast in range(1, len(nums)):
        if nums[fast] != nums[slow]:
            slow += 1
            nums[slow] = nums[fast]
    
    # Return number of unique elements
    return slow + 1
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
