# LC 744: Find Smallest Letter Greater Than Target

## Problem
Given a sorted list of **only lowercase English letters** and a target letter, find the smallest letter in the list that is **strictly greater than** the target.

**Important:** The list is cyclic. If the target is greater than or equal to all letters in the list, return the first letter.

**Example 1:**
```
Input: letters = ["c", "f", "j"], target = "a"
Output: "c"
Explanation: The smallest letter greater than "a" is "c".
```

**Example 2:**
```
Input: letters = ["c", "f", "j"], target = "c"
Output: "f"
Explanation: The smallest letter greater than "c" is "f".
```

**Example 3:**
```
Input: letters = ["c", "f", "j"], target = "j"
Output: "c"
Explanation: The letters wrap around. Since "j" is the largest, 
we return the smallest letter "c".
```

**Constraints:**
- `2 <= letters.length <= 10^4`
- `letters[i]` is a lowercase English letter
- `letters` is sorted in strictly ascending order
- `target` is a lowercase English letter

---

## Approach

**Binary Search (Find First Greater Element):**

This is a variation of binary search where instead of finding an exact match, we find the **first element greater than** the target.

1. **Initialize:** `low = 0`, `high = len(letters) - 1`

2. **Binary Search Logic:**
   - Compute `mid = (low + high) // 2`
   - If `letters[mid] > target`: This could be our answer, but there might be a smaller one on the left. Move `high = mid` (keep mid as candidate)
   - If `letters[mid] <= target`: We need something larger, move `low = mid + 1`

3. **Return:** `letters[low % len(letters)]` (the modulo handles the cyclic wrap-around)

**Why modulo?**
- If no letter is greater than target, `low` will reach `len(letters)`, and we wrap around to index 0 (the first letter).

**Key Differences from Standard Binary Search:**
- We're not looking for an exact match
- We're finding the **leftmost position** where the condition is satisfied
- The answer is at `low` index, not necessarily at the position where we exit

---

## 🧠 Solution

```python
def nextGreatestLetter(letters: list[str], target: str) -> str:
    """
    Find the smallest letter greater than target using binary search.
    
    Args:
        letters: Sorted list of lowercase English letters
        target: Target letter
    
    Returns:
        The smallest letter strictly greater than target
    """
    low, high = 0, len(letters) - 1
    
    while low < high:  # Note: strict inequality
        mid = (low + high) // 2
        if letters[mid] <= target:
            # Current letter is not greater, search right
            low = mid + 1
        else:
            # Current letter is greater, might be answer, search left
            high = mid
    
    # Wrap around if low reaches end (target >= all letters)
    return letters[low % len(letters)]
```

**Complexity:**
- **Time:** O(log n) - binary search
- **Space:** O(1) - only using pointers

---

## Alternative Approach: Linear Search

```python
def nextGreatestLetter(letters: list[str], target: str) -> str:
    """Simple linear search approach."""
    for letter in letters:
        if letter > target:
            return letter
    return letters[0]  # Wrap around
```

**Complexity:**
- **Time:** O(n) - iterating through all letters
- **Space:** O(1)

Use binary search for better performance with large inputs.

---

## Key Insights

1. **Cyclic Nature:** Remember to handle wrap-around with modulo operator
2. **Finding First Greater:** Use `letters[mid] <= target` to decide direction (different from exact match)
3. **Loop Condition:** Use `low < high` instead of `low <= high` to avoid infinite loops
4. **Post-Loop:** The answer is always at index `low` before applying modulo

---

## 📊 Metrics

| Metric | Value |
|--------|-------|
| **Date Solved** | Apr 22, 2026 |
| **Difficulty** | Easy |
| **Status** | ✅ Solved |
| **Planning Time** | 5 min |
| **Coding Time** | 7 min |
| **Testing Time** | 5 min |
| **Total Time** | 17 min |
| **Submission** | 1st Attempt |
