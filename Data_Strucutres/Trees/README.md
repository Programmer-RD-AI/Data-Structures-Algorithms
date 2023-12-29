# Introduction

Higherarical structure, zero or more child nodes. Every child descents from a parent, there is also child parent relationships which are from parent to child

# Binary Trees

Type of tree with rules:

- each node can have 0,1,2 nodes
- Each child can only have one parent

Types of Trees:

- Perfect Binary Tree (all the leaf nodes are full and there is no node that has only 1 child) // hella efficent
- Full Binary Tree (a node has either zero or 2 children) // hella inefficient
  - the number of leaf nodes are == to the number of other nodes + 1

# O(log N)

half the number of possibilities, halfing of the possible outcomes (n/2 == 1)

Level 0: 2^0 = 1
Level 1: 2^1 = 2
Level 2: 2^2 = 4
Level 3: 2^3 = 8

no. of nodes = 2^h - 1

log nodes = height

Divide and Conquering until you get to that specific node

# Binary Search Trees

.right increases the value
.left decreases the value

# Balanced vs Unbalanced BST

There are balanced and non balanced tress, which in turn acts as a long linked list and the time complexity takes a hit going from O(log(n)) -> O(n)
To balance use: AVL / Red Black Trees

# BST Pros & Cons

## Pros

- Better than O(n)
- Ordered
- Flexible Size

## Cons

- No O(1) operations

# Heap

## Binary Heap

lookup is O(n)
Less ordered than binary tree
The factor that the element right is higher than the root and the other way around is not applied here..., and values are added kinda rdmly...

## Priority Queue

Parent is always bigger than the children
Priotirty Queue is where the order doesnt matter but the element with the highest priority is serverd first

## Pros and Cons

Better than O(n)
Priority
Flexible Size
Fast Insert

Slow lookup

# Trie

# Red Black Trees

## Introduction

Nodes are either red or black
Leaves are black
If node a is red, the childeren are black
All paths from a node to its NIL ()
Nodes require one storage bit to keep track of color

## Rotations

Caused due to Insert and Remove operations

1. aletrs the structure of a tree by rearranging subtrees
2. goal is to decrease the height of the tree
   - dont effect the order of the elements

## Insertions

### Strategy

Insert Z and color it red
Recolor and rotate nodes to fix violation

1. Z = root -> color black
2. z.uncle = red -> recolor
3. Z.uncle = black(traingle) -> rotate.z.parent
4. Z.uncle = black(link) -> rotate.z.grandparent and also recolor

### Examples

# AVL Trees

self balancing binary search tree
similar to red blacktrees
perform fixes after insert and delete
Guarantees specific time compliexities
height = # of nodes on the longest path to the leaf
