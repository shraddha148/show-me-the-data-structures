<!--
Problem 7: Request Routing in a Web Server with a Trie

## Reasoning Behind Decisions:

I used a Trie (prefix tree) because it is well suited for storing and searching hierarchical URL paths efficiently. 
Each node represents a part of the URL, and the handler is stored only at the final node of the route. 
A dictionary is used to store child nodes, allowing fast lookups. The Router class separates URL processing from the Trie logic by splitting paths into components before insertion and lookup. 
Trailing slashes are handled by normalizing the path, so /home/about and /home/about/ return the same handler.

## Time Efficiency:

Both adding a route and looking up a route require traversing the path once. 
If the path contains m parts, the time complexity is O(m).

## Space Efficiency:

The Trie stores one node for each unique path component. 
Therefore, the space complexity is O(n), where n is the total number of nodes created for all routes.
Each node stores only a dictionary of child nodes and an optional handler, making the solution memory efficient for shared path prefixes.