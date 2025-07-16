## Interval Problems - Work in Progress

Lets talk about the interval problems, where you are given start and end times
of what represent intervals. Usually at the heart of the problem is around
overlaps. We obviously find overlaps using two for loops but this doesnt really
work for problems with a large input size, and this precisely is the tricky part
of this type of problems.

Just to setup a baseline understanding of datastrucutres, and to build towards
what datastructures we would need to solve problem pertaininig to Intervals,
Lets talk about that are the usecases of each of the datastrucutres.

1. Hashmaps : Mainly to remember things, hashmaps have keys that hash to a
   memory address and looking at whats stored at that address is instantaneous.

   Will it work here?

2. Heaps/Priority Queues : I like to think of priority queues as "live"
   datastructures they are like a little elf working to maintain the data
   structure and uphold its name: the top element is the smallest or the largest
   element based on the type of heap it is.

   Will it work here?

3. Stacks (Monotonic Stacks) :

Preprocessing

1. Somtimes you will get questions where the start and end times will be in
   seperate arrays.

2. Often times sorting the intervals based on start or end times ends up being a
   necessary step. In the context of [Meeting Rooms Problem](./meeting-rooms.md)
   where we are required to simply check if there's an overlap. There we simply
   sorted the intervals based on start times, and check if current interval
   starts before the previous one end. (More discussion in the link)
