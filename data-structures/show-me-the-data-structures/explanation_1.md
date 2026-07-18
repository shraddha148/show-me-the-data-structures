# Reasoning Behind Decisions:
A dictionary (cache) is used for O(1) lookup of keys.
A doubly linked list is used to keep track of the order in which items are used.
The most recently used (MRU) item is always placed right after the dummy head.
The least recently used (LRU) item is always just before the dummy tail.
When a key is accessed using get() or updated using set(), its node is moved to the front of the linked list.
When the cache reaches its capacity, the node before the tail (the least recently used node) is removed from both the linked list and the dictionary.

# Time Efficiency:
get(key): O(1)
Dictionary lookup takes O(1).
Removing and inserting a node in the doubly linked list also takes O(1).
set(key, value): O(1)
Dictionary insertion/update is O(1).
Adding, removing, or moving nodes in the linked list is O(1).
Evicting the least recently used node is also O(1).

# Overall Time Complexity: O(1) for both get() and set() operations.

# Space Efficiency:
The dictionary stores at most capacity key-node pairs.
The doubly linked list also stores at most capacity nodes (plus two dummy nodes).

Overall Space Complexity: O(capacity) (or simply O(n), where n is the cache capacity).