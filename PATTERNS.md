# 🎯 This Week's Focus: Two Pointers Pattern

Master this pattern completely. Next week we'll move to the next pattern.

---

## 📌 Two Pointers

**When to use:**
- Sorted array/string problems
- Finding pairs with a target
- Reversing or rearranging elements
- Removing duplicates

**Key Signals:**
- "Reverse", "Pair", "Palindrome"
- Sorted input
- Need to compare elements from different positions

**Template:**
```python
def solve(arr):
    left, right = 0, len(arr) - 1
    while left < right:
        # Process
        left += 1
        right -= 1
```

---

## 📚 Resources

- [Two Pointers Detailed Guide](patterns/two-pointers/README.md)
- [Solutions & Examples](patterns/two-pointers/solutions.py)
- [Complexity Analysis](notes/COMPLEXITY_ANALYSIS.md)

---

## 🎯 This Week's Problems

Target: **5-8 problems** with Two Pointers pattern

1. ✅ LC 3823: Reverse Only Letters (Done)
2. ⏳ LC 125: Valid Palindrome
3. ⏳ LC 167: Two Sum II
4. ⏳ LC 11: Container With Most Water
5. ⏳ LC 26: Remove Duplicates
6. ⏳ Pick 3-5 more...

---

## 📋 Future Patterns (Next Weeks)

We'll cover these one pattern per week:

### Week 2: Sliding Window
- Contiguous subarrays/substrings
- When pattern: "Longest", "Shortest", max/min

### Week 3: Binary Search
- Sorted arrays
- When pattern: "Sorted", find target, O(log n)

### Week 4-5: Dynamic Programming
- Optimization problems
- When pattern: "Maximum", "Minimum", "ways to"

### Week 6: Tree/Graph Traversals
- BFS/DFS operations
- When pattern: "Tree", "Graph", "connected"

### Week 7: Backtracking
- All combinations/permutations
- When pattern: "All", "combinations", "permutations"

### Week 8: Heap/Priority Queue
- Top K problems
- When pattern: "Top K", "Kth largest", "priority"

### Week 9: Linked Lists
- Node-based problems
- When pattern: "Linked list", "cycle", "merge"

---

**One week per pattern = deep mastery, not surface coverage!**
