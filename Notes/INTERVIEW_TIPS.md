# 💡 Interview Tips & Tricks

Practical advice from the DSA trenches for crushable interviews.

---

## 🎤 During the Interview

### Before Coding (5 min)
- [ ] Clarify the problem—ask questions
- [ ] Discuss approach & complexity first
- [ ] Mention edge cases you'll handle
- [ ] Get agreement before coding

### While Coding (20-30 min)
- [ ] Write clean, readable code
- [ ] Add comments for complex parts
- [ ] Don't overcomplicate early
- [ ] Test mentally as you code
- [ ] Keep variable names meaningful

### After Coding (5-10 min)
- [ ] Walk through test cases
- [ ] Discuss complexity analysis
- [ ] Talk about trade-offs
- [ ] Suggest optimizations

---

## 🚨 Common Mistakes to Avoid

| Mistake | Fix |
|---------|-----|
| Jump to code without thinking | Clarify problem first, discuss approach |
| Ignore edge cases | List edge cases explicitly |
| Suboptimal complexity | Try to reduce from O(n²) to O(n) |
| Poor variable names | Use `left`, `right`, `window` not `l`, `r`, `w` |
| No space analysis | Always mention space after time |
| Forgetting base cases | Recursion needs base case |
| Off-by-one errors | Be careful with `<` vs `<=` |
| Modifying input unnecessarily | Avoid unless explicitly allowed |

---

## 💬 What Interviewers Listen For

✅ **Good Signs:**
- "Let me think about the edge cases..."
- "The time complexity is O(n), space is O(1) because..."
- "This brute force is O(n²), let me optimize..."
- "Can I ask a clarifying question?"
- "Let me trace through this example..."

❌ **Red Flags:**
- Silent for 5+ minutes
- Coding without talking
- "I don't know" without thinking
- Changing approach 3 times
- No mention of complexity

---

## 🎯 Code Quality Checklist

```python
# ✅ GOOD CODE
def two_sum(nums, target):
    """Find two numbers that sum to target."""
    seen = {}
    for num in nums:
        complement = target - num
        if complement in seen:
            return [seen[complement], nums.index(num)]
        seen[num] = num
    return []

# ❌ POOR CODE
def f(a,b):
    s={}
    for i in a:
        c=b-i
        if c in s:return [s[c],a.index(i)]
        s[i]=i
    return[]
```

---

## 📝 Things to Verbalize

1. **Problem Understanding:** "So, I need to find... and return..."
2. **Approach:** "I'll use a hash map to track seen numbers..."
3. **Complexity:** "This is O(n) time since we iterate once, O(n) space for the hash map."
4. **Edge Cases:** "If array is empty, I return... If all elements are the same..."
5. **Testing:** "Let me trace through with example [1,2,3,4]..."

---

## 🔄 Optimization Framework

If stuck on optimization:

1. **Brute Force First** → Always have a working solution
2. **Identify Bottleneck** → Where's the O(n²)?
3. **Use Data Structures** → Hash map, heap, graph?
4. **Apply Patterns** → Two pointers? Sliding window?
5. **Verify Improvement** → What's new complexity?

---

## 🎬 Example Interview Dialogue

**You:** "Can I clarify the problem? Are the numbers sorted? Positive/negative? Any duplicates?"

**Interviewer:** "Array can have duplicates, not necessarily sorted, can be negative."

**You:** "So for [3,2,4] with target 6, return indices [1,2]? And if no pair exists, return empty?"

**Interviewer:** "Exactly."

**You:** "Alright, my approach: use a hash map. For each number, check if we've seen its complement. Time O(n), space O(n)."

*(Start coding with comments)*

**You:** "Let me trace through: first element 3, need 3, haven't seen it. Add to map. Second element 2, need 4, haven't seen it. Third element 4, need 2, found it in map!"

**Interviewer:** "Good. Any edge cases?"

**You:** "Yes—empty array returns []. Single element returns []. Two elements that sum returns [0,1]."

---

## 🏆 Final Tips

- **Communicate constantly** - they want to hear your thinking
- **Start simple** - solve the problem first, optimize later
- **Name things well** - `left`, `right` > `l`, `r`
- **Break down logic** - make helper functions if needed
- **Defend your solution** - know why it works
- **Show enthusiasm** - for the problem and problem-solving
