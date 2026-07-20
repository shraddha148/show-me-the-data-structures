<!--
Problem 2: Search in a Rotated Sorted Array

## Reasoning Behind Decisions:

I used a modified binary search because the array is sorted but rotated. At each step, one half of the array is always sorted. By identifying the sorted half and checking whether the target lies within it, I can safely discard the other half. This maintains the efficiency of binary search while correctly handling the rotation.

## Time Efficiency:
The algorithm halves the search space in every iteration, resulting in a time complexity of O(log n).

## Space Efficiency:

The algorithm uses only a few variables (left, right, and mid) and does not require any additional data structures. 
Therefore, the space complexity is O(1).