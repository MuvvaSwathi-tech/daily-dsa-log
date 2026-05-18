# LeetCode 643: Maximum Average Subarray I

## Problem Statement
Given an array consisting of n integers and an integer k, find the contiguous subarray of length k that has the maximum average value. Return this value.

- [LeetCode 643 - Maximum Average Subarray I](https://leetcode.com/problems/maximum-average-subarray-i/)

## Approach: Sliding Window

1. **Initialize** the sum of the first `k` elements.
2. **Slide the window**: For each subsequent element, subtract the element going out of the window and add the new element coming in.
3. **Track the maximum sum** seen so far.
4. **Return** the maximum average by dividing the maximum sum by `k`.

### Python Solution
```python
def findMaxAverage(nums, k):
    window_sum = sum(nums[:k])
    max_sum = window_sum
    for i in range(k, len(nums)):
        window_sum += nums[i] - nums[i - k]
        max_sum = max(max_sum, window_sum)
    return max_sum / k
```

### Complexity Analysis
- **Time Complexity:** $O(n)$, where $n$ is the length of the array.
- **Space Complexity:** $O(1)$, only constant extra space is used.

## Key Points
- Sliding window is efficient for fixed-size subarray problems.
- Update the window sum in constant time as you move the window.

---

**Pattern:** Sliding Window

**Related Problems:**
- [LC 567: Permutation in String](https://leetcode.com/problems/permutation-in-string/)
- [LC 3: Longest Substring Without Repeating Characters](https://leetcode.com/problems/longest-substring-without-repeating-characters/)
