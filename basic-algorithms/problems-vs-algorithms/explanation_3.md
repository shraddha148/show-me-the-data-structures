<!--
Problem 3: Rearrange Array Digits

## Reasoning Behind Decisions:

I used Merge Sort because the problem does not allow Python's built-in sorting functions and requires O(n log n) time complexity. After sorting the digits in descending order, I alternately assign the digits to two numbers. This ensures that the largest digits occupy the highest place values in both numbers, maximizing their overall sum while keeping the number of digits balanced.

## Time Efficiency:

Merge Sort takes O(n log n) time, and creating the two numbers requires one additional pass through the sorted list (O(n)). Therefore, the overall time complexity is O(n log n).

## Space Efficiency:

Merge Sort requires additional space for the temporary arrays created during merging, resulting in a space complexity of O(n). 
The two output numbers use only constant extra space apart from the sorted array.