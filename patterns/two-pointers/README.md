# Two Pointers Pattern

The two-pointers technique is fundamental for solving many array/string problems efficiently.

---

## 🎯 Core Concept

Use **two independent pointers** moving through the data structure to solve the problem:
- **Starting Positions:** Can start from opposite ends, same start, or moving together
- **Movement:** Pointers move based on some condition (compare values, skip duplicates, etc.)
- **Meeting:** Usually terminate when pointers meet or cross

---

## ⏱️ Time & Space

- **Time Complexity:** Usually **O(n)** - single pass through data
- **Space Complexity:** Usually **O(1)** - in-place operations, or O(n) if modifying/creating output

---

## 🎬 Key Patterns

### Pattern 1: Opposite Ends Meeting

```python
# Start from both ends, move toward middle
left, right = 0, len(arr) - 1
while left < right:
    if condition:
        left += 1
    else:
        right -= 1
```

**Use Cases:**
- Palindrome validation
- Reverse operations
- Container with most water
- Valid trapping rain water

---

### Pattern 2: Same Direction (Fast & Slow)

```python
# Both pointers move forward, but at different speeds
slow, fast = 0, 0
while fast < len(arr):
    # Process
    if condition:
        slow += 1
    fast += 1
```

**Use Cases:**
- Remove duplicates (slow = write position, fast = read position)
- Find Kth element from end
- Linked list cycle detection

---

### Pattern 3: Sorted Array Search

```python
# One pointer at start, one at end in sorted array
left, right = 0, len(arr) - 1
while left < right:
    current_sum = arr[left] + arr[right]
    if current_sum == target:
        return [left, right]
    elif current_sum < target:
        left += 1  # Need larger sum
    else:
        right -= 1  # Need smaller sum
```

**Use Cases:**
- Two Sum (sorted array)
- 3Sum problems
- Sum pairs with target

---

## 🚀 When to Recognize This Pattern

**Red Flags (Pattern Signals):**
- ✅ "Reverse" - reverse entire array/string/list
- ✅ "Palindrome" - check if palindrome
- ✅ "Sorted array" + "Two numbers" - likely two-sum variant
- ✅ "Remove/Delete" without extra space - in-place modification
- ✅ "Pair with target" - sorted array often hints two-pointers
- ✅ "Container" or "Area" - opposite ends moving inward
- ✅ Two pointer names appears in problem ("left", "right")

---

## 💡 Tips & Tricks

### Avoid Off-by-One Errors
```python
while left < right:      # Not <=
```

### Skip Non-Target Elements
```python
while left < right and not s[left].isalpha():
    left += 1
```

### Movement Logic Depends on Problem
```python
# For sorted array pair problems:
if sum < target:
    left += 1      # Need bigger sum
else:
    right -= 1     # Need smaller sum
```

### Test with Edge Cases
- Empty array/string
- Single element
- All elements same
- No valid pair/solution

---

## 📚 Classic Problems

| Problem | Difficulty | Link |
|---------|-----------|------|
| Valid Palindrome | Easy | [LC 125](../LC_125_valid_palindrome.md) |
| Reverse String | Easy | [LC 344](../LC_344_reverse_string.md) |
| Remove Duplicates | Easy | [LC 26](../LC_26_remove_duplicates.md) |
| 2Sum (sorted) | Medium | [LC 167](../LC_167_two_sum_ii.md) |
| Container With Most Water | Medium | [LC 11](../LC_11_container_with_water.md) |
| 3Sum | Medium | LC 15 |
| Valid Palindrome II | Medium | LC 680 |

---

## 🔄 Variations to Practice

1. **Two-pointer with filtering:** Skip non-letters, non-digits
2. **Window movement:** Expand and contract based on condition
3. **Partitioning:** Rearrange elements based on pivot
4. **Reverse operations:** Truly in-place reversal
5. **Cycle detection:** Linked list fast/slow pointers

---

## 🎯 Template for New Problems

```python
def two_pointer_template(arr):
    """Template for two-pointer problems"""
    
    left, right = 0, len(arr) - 1
    
    while left < right:
        # Handle preprocessing (skip elements, etc.)
        while left < right and skip_condition(arr[left]):
            left += 1
        while left < right and skip_condition(arr[right]):
            right -= 1
        
        # Main logic
        if main_condition(arr[left], arr[right]):
            # Process found pair
            pass
        
        # Move pointers
        left += 1  # or based on condition
        right -= 1  # or based on condition
    
    return result
```

---

## 📊 Common Mistakes to Avoid

| Mistake | Fix |
|---------|-----|
| Using `while left <= right` | Use `while left < right` (prevents overlap) |
| Forgetting to move pointers | Always increment/decrement both after processing |
| Moving wrong pointer | Choose based on problem logic (not arbitrary) |
| Modifying input unnecessarily | Only if problem allows |
| Not handling edge cases | Empty, single element, all same |

---

**Master this pattern and crack ~20% of interview problems!**

👉 Check [solutions.py](solutions.py) for runnable implementations!
