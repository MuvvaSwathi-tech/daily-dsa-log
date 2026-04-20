# LC 278: First Bad Version

## Problem
You are a product manager and currently leading a team to develop a new product. Unfortunately, the latest version of your product fails the quality check. Since each version is developed based on the previous version, all the versions after a bad version are also bad.

Suppose you have `n` versions `[1, 2, ..., n]` and you want to find the first bad one. You are given an API function `isBadVersion(version)` which will return whether `version` is bad.

Calling the API is expensive (takes O(1) time but counts towards your API call quota). You need to find the first bad version while minimizing the number of API calls.

**Example:**
```
Given n = 5, and version 4 is the first bad version.

call isBadVersion(3) -> False
call isBadVersion(5) -> True
call isBadVersion(4) -> True

Then you should return 4.
```

---

## Approach

**Binary search to minimize API calls:**

1. Use binary search on the version range from 1 to n.
2. At each step, compute `mid = left + (right - left) // 2`.
3. Call `isBadVersion(mid)`:
   - If `mid` is bad, the first bad version is at `mid` or to the left, so `right = mid`.
   - If `mid` is good, the first bad version must be to the right, so `left = mid + 1`.
4. Continue until `left == right`, which gives the first bad version.

This works because:
- Once we find a bad version, we know all subsequent versions are bad.
- We need to find the leftmost bad version.
- Binary search reduces the search space logarithmically, minimizing API calls.

---

## 🧠 Binary Search Solution

```python
def firstBadVersion(n: int) -> int:
    """
    Find the first bad version using binary search.
    
    Args:
        n: Total number of versions
    
    Returns:
        The index of the first bad version
    """
    left, right = 1, n

    while left < right:
        mid = left + (right - left) // 2

        if isBadVersion(mid):
            # mid is bad, so the first bad is at mid or to the left
            right = mid
        else:
            # mid is good, so the first bad is to the right
            left = mid + 1

    return left
```

**Why it works:**
- Binary search narrows down the search space to find the boundary between good and bad versions.
- When we find a bad version, we move right to mid to include the possibility that mid itself is the first bad.
- When we find a good version, we move left to mid + 1 because all versions before mid are guaranteed to be good.
- The loop terminates when left == right, pointing to the first bad version.

**Complexity:**
- **Time:** O(log n) - Each API call and binary search iteration reduces the search space by half.
- **Space:** O(1) - Only using constant extra space for left, right, and mid pointers.

## 📊 Metrics

| Metric | Value |
|--------|-------|
| **Date Solved** | Apr 21, 2026 |
| **Difficulty** | Easy |
| **Status** | ✅ Solved |
| **Planning Time** | 3 min |
| **Coding Time** | 5 min |
| **Testing Time** | 4 min |
| **Total Time** | 12 min |
| **Submission** | 1st Attempt |
