class Node:
    def __init__(self, key: int, value: int) -> None:
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache(object):
    """
    A class to represent a Least Recently Used (LRU) cache.

    Attributes:
    -----------
    capacity : int
       The maximum number of items the cache can hold.
    cache : OrderedDict[int, Any]
        The ordered dictionary to store cache items.
    """

    def __init__(self, capacity: int) -> None:
        """
        Constructs all the necessary attributes for the LRU_Cache object.

        Parameters:
        -----------
        capacity : int
            The maximum number of items the cache can hold.
        """
        self.capacity = capacity
        self.cache = {}

        #dummy head and tail
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head

        #remove node form LinkedList

    @staticmethod
    def remove(node):
        prev_node = node.prev
        next_node = node.next
        prev_node.next = next_node
        next_node.prev = prev_node

        #add a node right after head
    def insert(self, node) -> None:
        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node


    def get(self, key: int):
        """
        Get the value of the key if the key exists in the cache, otherwise return -1.

        Parameters:
        -----------
        key : int
            The key to be accessed in the cache.
        Returns:
        --------
        Optional[Any]
            The value associated with the key if it exists, otherwise -1.
        """
        if key not in self.cache:
            return -1
        node = self.cache[key]

        # Move node to front (recently used)
        self.remove(node)
        self.insert(node)

        return node.value

    def set(self, key, value) -> None:
        """
        Set or insert the value if the key is not already present. When the cache reaches 
        its capacity, it should invalidate the least recently used item before inserting 
        a new item.

        Parameters:
        -----------
        key : int
            The key to be inserted or updated in the cache.
        value : Any
            The value to be associated with the key.
        """
        if self.capacity <= 0:
            return
        if key in self.cache:
            node = self.cache[key]
            node.value = value

            self.remove(node)
            self.insert(node)
        else:
            if len(self.cache) == self.capacity:
                # Remove least recently used node
                lru = self.tail.prev

                self.remove(lru)
                del self.cache[lru.key]

            new_node = Node(key, value)

            self.cache[key] = new_node
            self.insert(new_node)


if __name__ == '__main__':
    # Testing the LRU_Cache class

    # Test Case 1: Basic functionality
    print("Test Case 1")

    our_cache = LRUCache(5)
    our_cache.set(1, 1)
    our_cache.set(2, 2)
    our_cache.set(3, 3)
    our_cache.set(4, 4)
    print(our_cache.get(1))     # Returns 1
    print(our_cache.get(2))   # Returns 2
    print(our_cache.get(9))  # Returns -1 because 9 is not in the cache

    our_cache.set(5, 5)
    our_cache.set(6, 6)  # This should evict key 3
    assert our_cache.get(3) == -1  # Returns -1, 3 was evicted

##Test Case 2

print("Test Case 2")

cache = LRUCache(2)

cache.set(1, 10)
cache.set(2, 20)

print(cache.get(1))   # 10

cache.set(3, 30)   ##removes least used cache (2,20) and add new (3,30)

print(cache.get(2))   # -1 since 2 is removed
print(cache.get(3))   # 30

#Test Case 3

print("Test Case 3")

cache = LRUCache(0)

cache.set(1, 100)

print(cache.get(1))
