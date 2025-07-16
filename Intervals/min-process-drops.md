# Minimum Process Drops for Synchronization

**Difficulty:** Medium

---

A team of developers is working on process synchronization. A set of processes
is synchronized if there is at least one process in the set whose execution time
overlaps with the execution times of all other processes in the set.

You're given two integer arrays `starts` and `ends`, where `starts[i]` and
`ends[i]` represent the start and end times of the i-th process.

Your task is to return the minimum number of processes that must be removed so
that the remaining processes form a synchronized set.

A set containing only one process is considered to be synchronized.

---

## Example 1:

```
Input: starts = [1, 2, 3, 4], ends = [2, 3, 5, 5]
Output: 1
```

**Explanation:**  
The execution intervals are:

- [1, 2]
- [2, 3]
- [3, 5]
- [4, 5]

Removing the process at index 0 (interval [1, 2]) results in:

- [2, 3]
- [3, 5]
- [4, 5]

These three intervals all overlap at time 3, making the set synchronized.

---

## Constraints:

- `1 <= n <= 2 * 10^5`
- `1 <= starts[i] < ends[i] <= 10^9`
- It is guaranteed that no two processes have identical [start, end]

TODO:
