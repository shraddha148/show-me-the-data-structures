## Reasoning Behind Decisions:
A recursive Depth-First Search (DFS) approach is used because a group can contain both users and other groups.
The function first checks whether the user exists in the current group's user list.
If the user is not found, it recursively searches each child group.
The search stops immediately and returns True as soon as the user is found, avoiding unnecessary traversal.
Edge cases such as a None user, a None group, and an empty group are handled by returning False.
Time Efficiency:
In the worst case, every group and every user is visited once.
If the user is found early, the search stops immediately.

## Overall Time Complexity: O(G + U)

where:

G = total number of groups.
U = total number of users across all groups.
Space Efficiency:
The recursive function uses the call stack to traverse nested groups.
The maximum recursion depth depends on the depth of the group hierarchy.

## Overall Space Complexity: O(H)

where:

H = maximum depth (height) of the group hierarchy.

In the worst case, if all groups are nested inside one another, H can be equal to the total number of groups.