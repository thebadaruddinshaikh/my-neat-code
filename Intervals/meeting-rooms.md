# Meeting Rooms

Given an array of meeting time intervals consisting of start and end times
`[[start_1, end_1], [start_2, end_2], ...]` where `start_i < end_i`, determine
if a person could attend all meetings without any conflicts.

---

**Example 1:**

```
Input: intervals = [(0,30),(5,10),(15,20)]
Output: false
```

**Explanation:**

- `(0,30)` and `(5,10)` will conflict
- `(0,30)` and `(15,20)` will conflict

---

**Example 2:**

```
Input: intervals = [(5,8),(9,15)]
Output: true
```

---

**Note:**

- `(0,8)` and `(8,10)` is **not** considered a conflict at `8`.

---

**Constraints:**

- `0 <= intervals.length <= 500`
- `0 <= intervals[i].start < intervals[i].end <= 1,000,000`

## Solution

```python

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key = lambda x : x.start)


        for i in range(1, len(intervals)):
            if intervals[i-1].end > intervals[i].start:
                return False

        return True
```

## Discussion

**Why do we sort based on Start times, would it work if we sort based on end
times?**

You can sort either way and it will still work, for one to be able to understand
why this work, one needs to understand what is an overlap An overlap is when the
start time an interval lies before the end time of the previous interval.

    Lets say you sort it by end times, so i ends after i-1, okay but if it starts before the previoius one ends its an overlap.

    now if you sort by end times, i starts after i-1 but if it starts before i-1 ends its an overlap. Sometimes its hard to fully comprehend this and one should try drawing the different intervals as lines on on a x,y axis. I might add some visuals for this at somepoint to help elucidate.
