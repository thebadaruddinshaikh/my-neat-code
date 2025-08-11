# Arrays and Hashing.

**Note :** <br> One thing to note is that this folder will also contain question
that are from queue and stack, as long as teh underlyting datastructure will be
an array they will ge dealt like the same, . Primarily when you seit in an
interview y all you see is a one dimensional datastructure holding some data, an
you will no where find atag saying thta it s a stack questin or a queue
question. so in my very humble opinion its best to club all arryy bsed quetion
together and them buidl patterns and technique to determine what to use and how
to use

Arrays are simple datascturctures , one Dimensional (some questions will require
you to deal with 2D arrays), and since there isn't a lot of complexity in the
way the data is stored, question here will usually require some mental
gynastics. Most question will require some kind of remembering and or Travesal
techniques. Often with array question there is a brute force solution which is
very straight forward, then the optimiszation expeteced are with time and space.
In most interviews you will face arrays , since the tricky questions really need
you to know other datastructures.

It is a remembering question when the answer to the question you are trying
solve depends on some sort of information ahead of you from the current position
or behind you. Most commons ways that you would remember this information is by
using some sort of data structure. Below are the commonly used datastructures
for "remebering". Depending on the problem we either use one or a combination.

- Hashtable
- HashSet
- Array - (Prefix, Suffix, Bucketing)
- Heap
- Bitmap
- Stack / Monotonic Stack

**Sorting**

1. Bubble Sort.
2. Insertion Sort.
3. Merge Sort.
4. Heap Sort.
5. Quick Sort. (+Randomized)
6. Bucket Sort.
7. Radix Sort.

**Searching**

1. 1D binary Search.
2. 2D binary Search.

**Traversing**

1. Two Pointers.
2. Sliding Window

Its a traversal type question when the array some how find the longest subarray
where a condition is met

## Monotonic Stack

This technique was harder from me to grasp as this isn't super straight forward
and takes a minute for one to have their head around it.

**Whats a Monotonic Stack**<br> A stack where the items are decreasing or
increasing (mostly strictly). This technique is mostly used when the question
you are dealing with requires you to know "perv/next element larger/smaller than
current" and the way the desing of the algorithm works, have the knowledge of
next and previous "smaller/greater" element. This is pretty cool!

Here are few questions that can be solved with the monotonic stack technique.

1. [11. Next Greater I](./11.next_greater_1.md)
2. [10. Daily Temperatures](./10.daily_temperatures.md)
3. [12.Trapping Rain Water](./12.trapping_rain_water.md)

## Two Pointers

## Sliding Window

## Deep Dive
