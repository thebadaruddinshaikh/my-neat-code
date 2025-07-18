# 199. Binary Tree Right Side View

**Difficulty:** Medium

---

Given the root of a binary tree, imagine yourself standing on the right side of
it, return the values of the nodes you can see ordered from top to bottom.

---

## Example 1:

```
Input: root = [1,2,3,null,5,null,4]
Output: [1,3,4]
```

**Explanation:**  
From the right side, you can see nodes 1 (root), 3 (right child of root), and 4
(right child at bottom level).

---

## Example 2:

```
Input: root = [1,2,3,4,null,null,null,5]
Output: [1,3,4,5]
```

**Explanation:**  
You can see the rightmost node at each level of the tree.

---

## Example 3:

```
Input: root = [1,null,3]
Output: [1,3]
```

---

## Example 4:

```
Input: root = []
Output: []
```

---

## Constraints:

- The number of nodes in the tree is in the range [0, 100].
- -100 <= Node.val <= 100
