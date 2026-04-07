# LC 3823: Reverse Letters & Special Characters

## Problem
Reverse letters separately and special characters separately, then merge them back.

**Example:**
```
Input:  ")ebc#da@f("
Output: "(fad@cb#e)"
```

---

## Approach

**Simple 3-step process:**

1. Extract all letters, reverse them → [f, a, d, c, b, e]
2. Extract all special chars, reverse them → [(, @, #, )]
3. Reconstruct: go through original, fill in reversed items matching their type

---

## 🐢 Brute Force Approach

**Idea:** Find all letter positions, find all special positions, build separately
```python
def reverseLettersAndSpecialCharacters_bruteforce(s: str) -> str:
    # Find indices of letters and special chars
    letter_indices = []
    special_indices = []
    
    for i, ch in enumerate(s):
        if ch.isalpha():
            letter_indices.append(i)
        else:
            special_indices.append(i)
    
    # Extract values
    letters = [s[i] for i in letter_indices]
    specials = [s[i] for i in special_indices]
    
    # Reverse both
    letters.reverse()
    specials.reverse()
    
    # Reconstruct by building string character by character
    result = [''] * len(s)
    for i, idx in enumerate(letter_indices):
        result[idx] = letters[i]
    for i, idx in enumerate(special_indices):
        result[idx] = specials[i]
    
    return ''.join(result)
```

**Complexity:**
- **Time:** O(n) - but with extra passes
- **Space:** O(n) - storing indices separately

**Why it's less optimal:**
- Extra list for indices tracking
- Multiple passes: extract → reverse → reconstruct
- More memory overhead

---

## ⚡ Optimal Solution

**Idea:** Extract, reverse, reconstruct in one clean flow
```python
def reverseLettersAndSpecialCharacters(s: str) -> str:
    # Extract and reverse letters
    letters = [ch for ch in s if ch.isalpha()]
    letters.reverse()
    
    # Extract and reverse special characters
    specials = [ch for ch in s if not ch.isalpha()]
    specials.reverse()
    
    # Reconstruct
    result = []
    letter_idx = special_idx = 0
    
    for ch in s:
        if ch.isalpha():
            result.append(letters[letter_idx])
            letter_idx += 1
        else:
            result.append(specials[special_idx])
            special_idx += 1
    
    return ''.join(result)
```

**Complexity:**
- **Time:** O(n) - cleaner passes
- **Space:** O(n) - only what we need

**Why it's optimal:**
- No extra index lists
- Direct letter/special list access
- Cleaner, more intuitive flow


---

## Complexity

| Time | O(n) - single pass through string |
| Space | O(n) - storing letters & specials |

---

## Walkthrough: ")ebc#da@f("

```
Step 1: Extract & Reverse
  Letters: e,b,c,d,a,f → f,a,d,c,b,e
  Specials: ),#,@,( → (,@,#,)

Step 2: Reconstruct
  Pos 0: ) = special → (
  Pos 1: e = letter  → f
  Pos 2: b = letter  → a
  Pos 3: c = letter  → d
  Pos 4: # = special → @
  Pos 5: d = letter  → c
  Pos 6: a = letter  → b
  Pos 7: @ = special → #
  Pos 8: f = letter  → e
  Pos 9: ( = special → )

Result: "(fad@cb#e)" ✅
```

---

## Tests

```python
assert reverseLettersAndSpecialCharacters(")ebc#da@f(") == "(fad@cb#e)"
assert reverseLettersAndSpecialCharacters("a#b@c") == "c@b#a"
assert reverseLettersAndSpecialCharacters("abcd") == "dcba"
assert reverseLettersAndSpecialCharacters("!@#$") == "$#@!"
```

---

## Key Points

✅ Track 2 separate indices (letters & specials)  
✅ Position type never changes  
✅ Both reversed independently, merged back

---

## 📊 Metrics

| Metric | Value |
|--------|-------|
| **Date Solved** | Apr 6, 2026 |
| **Difficulty** | easy |
| **Status** | ✅ Solved |
| **Planning Time** | 5 min |
| **Coding Time** | 8 min |
| **Testing Time** | 3 min |
| **Total Time** | 16 min |
| **Submission** | 1st Attempt |


