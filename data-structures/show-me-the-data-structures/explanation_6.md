## Union Function
# Reasoning Behind Decisions:
A set is used to store all unique values from both linked lists because sets automatically remove duplicates.
The first linked list is traversed and all its values are added to the set.
The second linked list is then traversed and its values are also added to the same set.
Finally, a new linked list is created by appending each unique value from the set.

# Time Efficiency:
Traversing the first linked list: O(n)
Traversing the second linked list: O(m)
Creating the result linked list: O(u), where u is the number of unique elements.

# Overall Time Complexity: O(n + m)

# Space Efficiency:
The set stores all unique values from both linked lists.
A new linked list is created to store the union.

# Overall Space Complexity: O(n + m)

## Intersection Function
# Reasoning Behind Decisions:
A set is created from the values of the first linked list for fast lookups.
The second linked list is traversed, and each value is checked against the set.
If a value exists in the set, it is added to the result linked list and removed from the set to prevent duplicates in the output.
A new linked list is returned containing only the common elements.

# Time Efficiency:
Traversing the first linked list to build the set: O(n)
Traversing the second linked list and checking set membership: O(m)

# Overall Time Complexity: O(n + m)

where:

n = number of nodes in the first linked list.
m = number of nodes in the second linked list.

# Space Efficiency:
A set is used to store the values from the first linked list.
A new linked list stores the common elements.

# Overall Space Complexity: O(n)