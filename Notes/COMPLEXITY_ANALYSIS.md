# ⏱️ Complexity Analysis Cheat Sheet

Quick reference for analyzing time and space complexity.

---

## Common Time Complexities

| Notation | Example | Operations (n=1000) |
|----------|---------|-------------------|
| O(1) | Accessing array element | 1 |
| O(log n) | Binary search | ~10 |
| O(n) | Linear search | 1,000 |
| O(n log n) | Merge sort | ~10,000 |
| O(n²) | Nested loops | 1,000,000 |
| O(n³) | Triple nested loops | 1,000,000,000 |
| O(2ⁿ) | Recursive permutations | ∞ (impractical) |
| O(n!) | All permutations | ∞ (impractical) |

---

## How to Analyze

### Time Complexity Steps:

1. **Count the operations** (loops, recursion levels)
2. **Identify the dominant term** (largest grows fastest)
3. **Drop the constant** (O(2n) → O(n))
4. **Express in Big-O notation**

### Examples:

**Linear Search:**
```python
for i in range(n):      # Runs n times
    if arr[i] == target:
        return True
```
→ **O(n)**

**Nested Loops:**
```python
for i in range(n):      # Runs n times
    for j in range(n):  # Runs n times for each i
        print(i, j)
```
→ **O(n²)**

**Binary Search:**
```python
while left <= right:    # Divides problem in half each time
    mid = (left + right) // 2
    if arr[mid] == target:
        return True
    elif arr[mid] < target:
        left = mid + 1
    else:
        right = mid - 1
```
→ **O(log n)** (dividing by 2 each step = log₂(n))

**Merge Sort:**
```python
# Divide: O(log n) levels
# Merge at each level: O(n)
```
→ **O(n log n)**

---

## Common Space Complexities

| Approach | Space |
|----------|-------|
| In-place (no extra) | O(1) |
| Single variables | O(1) |
| Dynamic array/list | O(n) |
| 2D matrix | O(n²) |
| Recursion depth | O(log n) to O(n) |
| Hash map storage | O(n) |

---

## Trade-offs to Know

| Strategy | Time | Space | Use When |
|----------|------|-------|----------|
| Brute force | High | Low | Understanding problem |
| Memoization | Medium | Medium | DP problems |
| Hash optimization | Low | High | Speed matters |
| Two-pointer | Low | Low | Optimal solution |

---

## Interview Tips

✅ **Do:**
- Start with simple algorithm first
- Then optimize (recognize patterns)
- Clearly state your analysis
- Consider best/worst/average cases

❌ **Don't:**
- Guess complexity
- Forget about constants (for space)
- Overlook hidden operations (string concatenation = O(n))
- Count the exact number of operations

---

## Quick Analysis Questions

**For any solution, ask:**
1. How many loops? Nested or sequential?
2. Does it divide/halve the problem? (→ log n)
3. How much extra space do I use?
4. Can I optimize further?
