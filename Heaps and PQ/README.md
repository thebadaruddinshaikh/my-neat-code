# Heaps & Priority Queues

- Situations that require heap often have a "live" aspect to them, they are
  dynamic and they are changing. Heaps help us get the information from the
  noise of all the changes.

Look at the question [Kth Largest Element](1.Kth-largest-element.md) where the
program is supposed to return the kth largest element while processing a stream
of operations.

### Deep Dive - Good to know.

Heaps are abstract Data Structures that have a contract with the user and they
always maintain it, there are two types of them 1. I will always give you the
minimum/maximum element of all the element you gave me and they do it
efficiently. They are also Abstract Data Structures meaning that they can be
implemented using different data structures i.e using an array or Linked List
(type with more fields like leftChild, rightChild, parent). In most
implementations you will see an array being used and thats what we will use too.

- You should ideally ask why arrays and not LinkedList, my answer would be - its
  easier. Lets look at the operation we will want to our heap to have.

What are the types of operation you usually need to do when working with Heaps.

1. Inserting nodes in the Heap. : Add to the end then bubble up based on the
   max/min heap condition.
2. Popping the Head : Swap with leaf , remove root that is at the leaf, simmer
   the new root down to find its place in the heap.
3. Checking the size of the Heap: Maintain a count of elements as you add and
   remove them from the structure.

**Heapify Logic - MaxHeap**

```python
def heapify(index, array):
    leftChild = 2 * index + 1
    rightChild = 2 * index + 2

    maxIndex = index
    if leftChild < len(array) and \
        array[leftChild] > array[maxIndex]:
        maxIndex = leftChild

    if rightChild < len(array) and \
        array[rightChild] > array[maxIndex]:
        maxIndex = rightChild

    if maxIndex != index:
        array[index], array[maxIndex] = array[maxIndex], array[index]
        heapify(maxIndex, array)
```

Now lets say we had to make an array into heap, this is how it would work.
Interesting to note that we start at min point of the array.

```python
def buildHeap(array):
    for ind in range((len(array)- 2)//2, -1,-1):
        heapify(ind, array)
```

Now that we have heap lets talk about poppoing element in and out of the heap.

**Popping Head**

```python
def pop(array):
    array[-1] , array[0] = array[0], array[-1]
    res = array.pop()
    heapify(0, array)
    return res
```

**Note:** We want to make full use of how arrays expand, so instead of taking
the last element from the array, which can be None/Default value, we actively
store the size of the heap. The size of heap and the size of underlying element
can be different. Why? Checkout
[Arrays and Hashing](../Arrays%20and%20Hashing/Readme.md)
