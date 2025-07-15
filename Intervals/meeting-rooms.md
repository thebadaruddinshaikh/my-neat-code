# Meeting Rooms

Given an array of meeting time intervals consisting of start and end times  
`[[start_1, end_1], [start_2, end_2], ...]` where `start_i < end_i`, determine  
if a person could attend all meetings without any conflicts.

---

## Examples

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

## Note

- `(0,8)` and `(8,10)` is **not** considered a conflict at `8`.

---

## Constraints

- `0 <= intervals.length <= 500`
- `0 <= intervals[i].start < intervals[i].end <= 1,000,000`

---

## Solution

```python
class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key=lambda x: x.start)
        for i in range(1, len(intervals)):
            if intervals[i-1].end > intervals[i].start:
                return False
        return True
```

**Time Complexity** : O(N)

## Discussion

**Why do we sort based on start times? Would it work if we sort based on end
times?**

You can sort either way and it will still work. To understand why, consider
what  
constitutes an overlap: an overlap occurs when the start time of an interval  
lies before the end time of the previous interval.

If you sort by end times, `i` ends after `i-1`, but if it starts before the
previous one ends,  
it's an overlap. If you sort by start times, `i` starts after `i-1`, but if it
starts before  
`i-1` ends, it's an overlap.

Sometimes it's hard to fully comprehend this, so try drawing the different
intervals  
as lines on an x-y axis. Visuals can help
