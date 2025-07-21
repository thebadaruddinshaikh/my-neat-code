# Trees - WIP

Trees are a form of graph, good chuck of question do use algorithms that you
study in graphs like DFS, BFS etc. There could also be a case where you are
required to convert a tree into a adjacency list. BUT, a big BUTT, is that most
question in Trees require **recursion**.

Majorly Tree Questions primarily revolve around finding

1. Height of the Tree/subtree
2. Something with the values of subtree
3. ....

When writing recursive solutions the thing that throws most people (atleast me)
off is the number of possibilities.

A single node in general is quite straight forward it can have a left child
and/or a right child or nothing at all. But when you zoom out a little bit you
start to thing this could be the case with every node and then the mind wanders
off thinking about all the different variations and if your code can handle all
of these cases. This is the biggest pitfall.

To deal with this we find need to understand what is the flow of information
like?

- do the children need to tell something to the parent? (Bottom-Up)
- Or is there a need of some information to be passed down the chlidren from teh
  parent? (Top-down)

Question whose answers depend on their children, obiviously need bottom up
approach. Problems like
[Maximum Depth Binary Tree](./2.maximum-depth-binary-tree.md),
[Diameter of Binary Tree](./3.diameter-binarytree.md),
[Balanced Binary Tree](./4.balanced-binary-tree.md) use Bottom up, because think
about it in any of the questions you have to check the children to see if they
satisfy some condition, right?

There are questions are more suited for Top-Down approach, checkout
[Branch Sum](./9.branch-sum.md)

## Botttom-Up

1. What do I want from the either arm?
2. When I make the recursive call how am I going to use the information that I
   got from the my call ot the other arm.
3. When recursive calls to both arms have finished, what information am I
   passing to the parent?
4. How does the current node contribute to this information I am building.

If you can answer these questions , you can solve any recrusive tree problem
without much effort. Question

## Top Down

In this type of recursion the parent passes information about the tree above
with the information about itself to both the children. The final answer is
prepared/saved at the leaf nodes. The information is passed down as argument to
the children.

Questions to as here are very straight forward.

1. What do the children need to know about the parent.
2. Where and how will the result computed at the leaves be stored?
   - Passing a reference to an answer array that the leaf woudl just append the
     results thats being passed down.
   - Returning the result back to the caller. TODO: Does this make sense? Maybe
     dont do it when you problem ends up making you return arrays?

## Binary Search Trees

A type of binary tree that have the following constraints.

1. Left child is less than or equal to the parent.
2. Right child is strictly greater than parent.

The questions are mostly about traversal. Since there is additional layer of
complexity added with the constraints.

## Standard Terminologies and Algorithms.

**Types of Binary Trees.**

1. Fully filled
2. Complete
3. Incomplete

**Tree Traversals.**

1. [In-Order Traversal](./0.traversal-inorder.md)
2. [Pre-Order Traversal](./0.traversal-preorder.md)
3. [Post-Order Traversal](./0.traversal-postorder.md)
4. Level Order Traversal

**Turning Trees into Graphs Problems** When you work with a Tree problem you are
often always limited by the nodes you can get to - you don't have a reference to
your parent. If you want to find apply a graph algorithm you need to convert
them so that your graph algorithms work seamlessly. For example checkout
[Find Nodes at K Distance](./13.find-nodes-at-k-distance.md#solution-using-adjacency-list).
