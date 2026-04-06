# LC 3794: Reverse String Prefix

## Problem
Reverse first k characters of a string.

**Example:**
```
Input:  s = "abcd", k = 2
Output: "bacd"

Explanation: Reverse first 2 chars: "ab" → "ba"
```

---

## Approach

**Simple process:**

1. Reverse first k characters
2. Keep rest of string as is
3. Merge together

---

## 🐢 Brute Force Approach

**Idea:** Convert to list, manually swap elements from start to k
```python
def reversePrefix_bruteforce(s: str, k: int) -> str:
    chars = list(s)
    
    class Solution:
    def reverseFirstK(self, s: str, k: int) -> str:
        p = s[:k]
        o = s[k:]

        ch = []
        for c in p:
            ch.append(c)

        ch.reverse()

        return ''.join(ch) + o
    
    return ''.join(chars)
```

**Complexity:**
- **Time:** O(k) - only swap k/2 times
- **Space:** O(n) - need list for string mutation

**Why it's less clean:**
- Manual index calculation for swaps
- Need to track i and k-1-i
- More error-prone logic

---

## ⚡ Optimal Solution

**Idea:** Use built-in reverse, slicing is clean
```python
def reversePrefix(s: str, k: int) -> str:
    # Reverse first k chars + rest
    return s[:k][::-1] + s[k:]
```

**Complexity:**
- **Time:** O(k) - reversal is O(k)
- **Space:** O(n) - creating new string

**Why it's optimal:**
- Super clean and readable ✅
- Pythonic slice notation
- Less code, fewer bugs

---

## ⚙️ Two-Pointers Variant

**If you want traditional two-pointer style:**
```python
def reversePrefix_twopointer(s: str, k: int) -> str:
    chars = list(s)
    left, right = 0, k - 1
    
    # Two pointers meet in middle
    while left < right:
        chars[left], chars[right] = chars[right], chars[left]
        left += 1
        right -= 1
    
    return ''.join(chars)
```

**Complexity:**
- **Time:** O(k)
- **Space:** O(n)

**Why use this:**
- Classic two-pointer pattern
- Demonstrates convergence style


---

## Complexity Analysis

| **Time** | O(k) - only reverse first k chars |
| **Space** | O(n) - new string created |

---

## Walkthrough: "abcd", k=2

```
Input:  "abcd", k=2

Step 1: Extract first k chars
  First k: "ab"
  Rest: "cd"

Step 2: Reverse first k
  "ab"[::-1] = "ba"

Step 3: Merge
  "ba" + "cd" = "bacd"

Output: "bacd" ✅
```

---

## Tests

```python
assert reversePrefix("abcd", 2) == "bacd"
assert reversePrefix("xyxzxe", 3) == "zxyxe"
assert reversePrefix("abcd", 4) == "dcba"
assert reversePrefix("a", 1) == "a"
```

---

## Key Points

✅ Two-pointer convergence pattern  
✅ Can use slicing or manual swap  
✅ Only affects first k characters

---

## 📊 Metrics

| Metric | Value |
|--------|-------|
| **Date Solved** | Apr 6, 2026 |
| **Difficulty** | Easy |
| **Status** | ✅ Solved |
| **Planning Time** | 5 min |
| **Coding Time** | 10 min |
| **Testing Time** | 10 min |
| **Total Time** |25 min |
| **Submission** | 1st Attempt |

---

## ✅ Mastery Checklist

- [x] Problem understood
- [x] Multiple approaches identified
- [x] Solution coded
- [x] Tests passing
- [x] Complexity analyzed
- [ ] Can solve variations with different constraints?  
✅ Position type never changes  
✅ Both reversed independently, merged back

---



