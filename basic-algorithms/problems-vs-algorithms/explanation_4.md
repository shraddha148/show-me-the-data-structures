
## Reasoning Behind Decisions:

I used the Dutch National Flag algorithm because it sorts an array containing only 0s, 1s, and 2s in a single traversal, which is a key requirement of the problem. The algorithm uses three pointers (low, mid, and high) to place each element in its correct position without requiring an additional array or a sorting function.

## Time Efficiency:

Each element is processed at most once, so the algorithm runs in O(n) time, where n is the number of elements in the array.

## Space Efficiency:

The algorithm sorts the array in place using only three pointer variables. 
Therefore, the space complexity is O(1) since no extra data structures proportional to the input size are used.