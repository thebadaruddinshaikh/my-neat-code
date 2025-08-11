# Insert Interval

You are given an array of non-overlapping intervals `intervals` where  
`intervals[i] = [start_i, end_i]` represents the start and the end time of the  
ith interval. `intervals` is initially sorted in ascending order by `start_i`.

You are also given another interval `newInterval = [start, end]`.

Insert `newInterval` into `intervals` such that `intervals` is still sorted in  
ascending order by `start_i` and also `intervals` still does not have any  
overlapping intervals. You may merge the overlapping intervals if needed.

Return `intervals` after adding `newInterval`.

**Note:**  
Intervals are non-overlapping if they have no common point. For example,  
`[1,2]` and `[3,4]` are non-overlapping, but `[1,2]` and `[2,3]` are
overlapping.

---

## Example 1

```
Input: intervals = [[1,3],[4,6]], newInterval = [2,5]
Output: [[1,6]]
```

---

## Example 2

```
Input: intervals = [[1,2],[3,5],[9,10]], newInterval = [6,7]
Output: [[1,2],[3,5],[6,7],[9,10]]
```

---

## Constraints

- `0 <= intervals.length <= 1000`
- `newInterval.length == intervals[i].length == 2`
- `0 <= start <= end <= 1000`

## Solution

```python
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        i = 0
        n = len(intervals)
        res = []

        while i < n and intervals[i][1] < newInterval[0] :
            res.append(intervals[i])
            i+=1

        while i < n and intervals[i][0] <= newInterval[1]:
            print(newInterval)
            newInterval[0] = min(newInterval[0], intervals[i][0])
            newInterval[1] = max(newInterval[1], intervals[i][1])
            i += 1

        res.append(newInterval)

        while i < n:
            res.append(intervals[i])
            i+=1

        return res
```

**Time Complexity:** O(N)<br> **Space Complexity:** O(N)

## Discussion

- Although this problem is rate medium it doesnt require clubbing concepts. You
  could use binary search since the array is sorted but the Big-O notation will
  still be linear. Althogh that is a better solution.
- The Complexity of this problem comes from being able to understand what an
  overlap means, check out [Meeting Rooms](./meeting-rooms.md).
