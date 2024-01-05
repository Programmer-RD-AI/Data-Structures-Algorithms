# Breadth First Search (BFS)

An algorithm for searching a graph
Breadth means broad / wide
We use a queue to track verttices (the ones to be visited)
Time Complexity: O(|V| + |E|) -> (Vertices + Edges)

# Depth First Search (DFS)

Follows one branch of a tree until the target node or the end is reached then it goes back and goes to the next branch.
Lower Memory requirements, because we dont need to keep child pointers
We need to go deep as possible and then start going to the right until the traversal of the tree is completed

## Implementation methods

//       9
//    4     20
//   1 6  15  170
PreOrder - [9,4,1,6,20,15,170] // Used to recreate trees
InOrder - [1,4,6,9,15,20,170]
PostOrder - [1,6,4,15,170,20,9]

# BFS vs DFS

Breadth first search is like water flooding from the top, breadth first search is like water flooding in streams from the top and going to the right.
They both do the same thing but they are used for different reasons.

## BFS

Shortest Path, Closer Node: Pros
More Memory: Cons

If an value is in the top of the tree then this is useful because this gets to each level first

## DFS

Less Memory, Does Path Exist?: Pros
Can Get Slow: Cons
