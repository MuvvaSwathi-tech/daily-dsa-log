# Binary Search Pattern

The binary search pattern is a classic algorithmic technique for efficiently searching sorted arrays or lists by repeatedly dividing the search interval in half.

---

## Core Concept
- Works on sorted data structures (arrays, lists)
- Compare the target with the middle element
- Narrow the search space by half each time
- Variants: finding boundaries, first/last occurrence, searching rotated arrays

---

## Time & Space Complexity
- **Time Complexity:** O(log n)
- **Space Complexity:** O(1) (iterative), O(log n) (recursive)

---

## Common Use Cases
- Search for a target value in a sorted array
- Find lower/upper bounds
- Search in rotated sorted arrays
- Find peak/minimum/maximum in sorted or rotated arrays

---

## Example Problems
- LC 704: Binary Search
- LC 34: Find First and Last Position of Element
- LC 33: Search in Rotated Sorted Array
- LC 162: Find Peak Element

---

**Tip:** Always check if the array is sorted and consider edge cases (empty array, single element, duplicates).
