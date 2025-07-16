# 2251. Number of Flowers in Full Bloom

**Difficulty:** Hard

---

You are given a 0-indexed 2D integer array `flowers`, where  
`flowers[i] = [start_i, end_i]` means the *i*th flower will be in full bloom  
from `start_i` to `end_i` (**inclusive**). You are also given a 0-indexed  
integer array `people` of size _n_, where `people[i]` is the time that the
*i*th  
person will arrive to see the flowers.

Return an integer array `answer` of size _n_, where `answer[i]` is the number
of  
flowers that are in full bloom when the *i*th person arrives.

---

## Example 1

```
Input: flowers = [[1,6],[3,7],[9,12],[4,13]], people = [2,3,7,11]
Output: [1,2,2,2]
```

**Explanation:**  
The figure above shows the times when the flowers are in full bloom and when
the  
people arrive. For each person, we return the number of flowers in full bloom  
during their arrival.

---

## Example 2

```
Input: flowers = [[1,10],[3,3]], people = [3,3,2]
Output: [2,2,1]
```

**Explanation:**  
The figure above shows the times when the flowers are in full bloom and when
the  
people arrive. For each person, we return the number of flowers in full bloom  
during their arrival.

---

## Constraints

- `1 <= flowers.length <= 5 * 10^4`
- `flowers[i].length == 2`
- `1 <= start_i <= end_i <= 10^9`
- `1 <= people.length <= 5 * 10^4`
- `1 <= people[i] <= 10^9`

TODO:
