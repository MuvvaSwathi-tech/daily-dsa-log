# Sliding Window Pattern

The sliding window pattern is a powerful technique for solving problems involving subarrays or substrings, especially when you need to find an optimal value (sum, length, etc.) for a contiguous block.

---

## Core Concept
- Use a window (subarray/subsequence) that slides over the input
- Adjust window size or position based on problem constraints
- Efficiently compute results in O(n) time

---

## Time & Space Complexity
- **Time Complexity:** O(n)
- **Space Complexity:** O(1) (fixed window), O(n) (variable window with extra data structures)

---

## Common Use Cases
- Maximum/minimum sum subarray of size k
- Longest substring with/without certain properties
- Counting or tracking elements in a window

---

## Example Problems
- LC 643: Maximum Average Subarray I
- LC 3: Longest Substring Without Repeating Characters
- LC 567: Permutation in String

---

**Tip:** Identify when a problem can be solved by maintaining a running window and updating results as the window moves.
