# LC 3633: Minimum Time to Visit Theme Park (Both Ride Types)

## Problem
You are given two categories of theme park attractions: land rides and water rides.

**Land rides:**
- `landStartTime[i]` – the earliest time the ith land ride can be boarded.
- `landDuration[i]` – how long the ith land ride lasts.

**Water rides:**
- `waterStartTime[j]` – the earliest time the jth water ride can be boarded.
- `waterDuration[j]` – how long the jth water ride lasts.

A tourist must experience exactly one ride from each category, in either order.

- A ride may be started at its opening time or any later moment.
- If a ride is started at time t, it finishes at time t + duration.
- Immediately after finishing one ride the tourist may board the other (if it is already open) or wait until it opens.

Return the earliest possible time at which the tourist can finish both rides.

**Example 1:**
```
Input: landStartTime = [2,8], landDuration = [4,1], waterStartTime = [6], waterDuration = [3]
Output: 9

Plan A (land ride 0 → water ride 0):
- Start land ride 0 at time 2, finish at 2 + 4 = 6
- Water ride 0 opens at 6, start at 6, finish at 6 + 3 = 9

Plan B (water ride 0 → land ride 1):
- Start water ride 0 at time 6, finish at 6 + 3 = 9
- Land ride 1 opens at 8, start at 9, finish at 9 + 1 = 10

Plan C (land ride 1 → water ride 0):
- Start land ride 1 at time 8, finish at 8 + 1 = 9
- Water ride 0 opened at 6, start at 9, finish at 9 + 3 = 12

Plan D (water ride 0 → land ride 0):
- Start water ride 0 at time 6, finish at 6 + 3 = 9
- Land ride 0 opened at 2, start at 9, finish at 9 + 4 = 13

Plan A gives the earliest finish time of 9.
```

**Example 2:**
```
Input: landStartTime = [5], landDuration = [3], waterStartTime = [1], waterDuration = [10]
Output: 14
```

---

## Approach

**Binary Search on Answer:**

The key insight is to binary search on the finish time, not on the rides themselves.

1. **Define search space:** The minimum possible finish time is at least the maximum of (first land ride start + duration, first water ride start + duration). The maximum is the sum of all times.

2. **For each candidate time T, check if it's feasible:**
   - For each land ride `i`: Can we finish land at time `≤ T` and then finish water at time `≤ T`?
     - Land finishes at: `landStartTime[i] + landDuration[i]`
     - Water must start at: `max(landFinishTime, waterStartTime[j])`
     - Water finishes at: `waterStartTime + waterDuration[j]`
     - Check: Does any water ride finish by time `T`?
   
   - Similarly, for each water ride `j`: Can we finish water first, then land by time `T`?

3. **Binary search:** Find the minimum time T where at least one valid combination exists.

Why binary search:
- The answer is monotonic: if time T works, any time > T also works.
- We can eliminate half the search space with each check.
- More efficient than checking all pairs when finish times span a large range.

---

## 🧠 Solution

```python
def minimumTime(landStartTime: list[int], landDuration: list[int], 
                waterStartTime: list[int], waterDuration: list[int]) -> int:
    """
    Find the minimum time to finish both rides using binary search on answer.
    
    Args:
        landStartTime: Start times for land rides
        landDuration: Durations for land rides
        waterStartTime: Start times for water rides
        waterDuration: Durations for water rides
    
    Returns:
        Earliest finish time for both rides
    """
    
    def can_finish_by_time(target_time):
        """Check if we can finish both rides by target_time."""
        # Try all land rides first
        for i in range(len(landStartTime)):
            land_finish = landStartTime[i] + landDuration[i]
            
            # Try both orderings for each land ride
            # Order 1: Land first, then water
            for j in range(len(waterStartTime)):
                water_start = max(land_finish, waterStartTime[j])
                water_finish = water_start + waterDuration[j]
                if water_finish <= target_time:
                    return True
            
            # Order 2: Water first, then land
            for j in range(len(waterStartTime)):
                water_finish = waterStartTime[j] + waterDuration[j]
                land_start = max(land_finish, waterStartTime[j])
                if land_start + landDuration[i] <= target_time:
                    return True
        
        return False
    
    # Binary search on the answer
    left = max(
        min(landStartTime[i] + landDuration[i] for i in range(len(landStartTime))),
        min(waterStartTime[j] + waterDuration[j] for j in range(len(waterStartTime)))
    )
    right = sum(landDuration) + sum(waterDuration) + max(landStartTime + waterStartTime)
    
    while left < right:
        mid = left + (right - left) // 2
        if can_finish_by_time(mid):
            right = mid
        else:
            left = mid + 1
    
    return left
```

**Why it works:**
- We binary search on the finish time rather than on which rides to choose.
- For each candidate time, we verify if any combination can complete by that time.
- The search space is monotonic: if time T is feasible, any time > T is also feasible.
- We find the minimum feasible time.

**Complexity:**
- **Time:** O((n × m) × log(max_time)) where n = land rides, m = water rides.
- **Space:** O(1) - Only using constant extra space.

**Note:** While binary search works, the brute force O(n × m) approach is simpler and often preferred for small arrays since the problem constraints are typically small (n, m ≤ 100).

## 📊 Metrics

| Metric | Value |
|--------|-------|
| **Date Solved** | Apr 21, 2026 |
| **Difficulty** | Easy |
| **Status** | ✅ Solved |
| **Planning Time** | 5 min |
| **Coding Time** | 6 min |
| **Testing Time** | 4 min |
| **Total Time** | 15 min |
| **Submission** | 1st Attempt |
