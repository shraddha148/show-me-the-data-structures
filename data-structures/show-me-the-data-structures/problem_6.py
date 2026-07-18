from typing import Optional


class Node:
    """
    A class to represent a node in a linked list.
    """

    def __init__(self, value: int) -> None:
        self.value: int = value
        self.next: Optional['Node'] = None

    def __repr__(self) -> str:
        return str(self.value)


class LinkedList:
    """
    A class to represent a singly linked list.
    """

    def __init__(self) -> None:
        self.head: Optional[Node] = None

    def __str__(self) -> str:
        cur_head = self.head
        out_string = ""

        while cur_head:
            out_string += str(cur_head.value) + " -> "
            cur_head = cur_head.next

        return out_string

    def append(self, value: int) -> None:
        if self.head is None:
            self.head = Node(value)
            return

        node = self.head
        while node.next:
            node = node.next

        node.next = Node(value)

    def size(self) -> int:
        size = 0
        node = self.head

        while node:
            size += 1
            node = node.next

        return size


def union(llist_1, llist_2):
    values = set()

    node = llist_1.head
    while node:
        values.add(node.value)
        node = node.next

    node = llist_2.head
    while node:
        values.add(node.value)
        node = node.next

    result = LinkedList()

    for value in values:
        result.append(value)

    return result


def intersection(llist_1, llist_2):
    set1 = set()

    node = llist_1.head
    while node:
        set1.add(node.value)
        node = node.next

    result = LinkedList()

    node = llist_2.head
    while node:
        if node.value in set1:
            result.append(node.value)
            set1.remove(node.value)   # Prevent duplicates
        node = node.next

    return result


if __name__ == "__main__":

    # Test Case 1
    linked_list_1 = LinkedList()
    linked_list_2 = LinkedList()

    element_1 = [3, 2, 4, 35, 6, 65, 6, 4, 3, 21]
    element_2 = [6, 32, 4, 9, 6, 1, 11, 21, 1]

    for i in element_1:
        linked_list_1.append(i)

    for i in element_2:
        linked_list_2.append(i)

    print("Test Case 1:")
    print("Union:", union(linked_list_1, linked_list_2))                #output - Union: 32 -> 65 -> 2 -> 35 -> 3 -> 4 -> 6 -> 1 -> 9 -> 11 -> 21 ->
    print("Intersection:", intersection(linked_list_1, linked_list_2))  #output - Intersection: 6 -> 4 -> 21 ->

    # Test Case 2
    linked_list_3 = LinkedList()
    linked_list_4 = LinkedList()

    element_1 = [3, 2, 4, 35, 6, 65, 6, 4, 3, 23]
    element_2 = [1, 7, 8, 9, 11, 21, 1]

    for i in element_1:
        linked_list_3.append(i)

    for i in element_2:
        linked_list_4.append(i)

    print("\nTest Case 2:")
    print("Union:", union(linked_list_3, linked_list_4)                  #output - 1 -> 2 -> 3 ->
    print("Intersection:", intersection(linked_list_3, linked_list_4))   #output - blank

    # Test Case 3 (One Empty List)
    linked_list_5 = LinkedList()
    linked_list_6 = LinkedList()

    linked_list_6.append(1)
    linked_list_6.append(2)
    linked_list_6.append(3)

    print("\nTest Case 3:")
    print("Union:", union(linked_list_5, linked_list_6)                 #output - 1 -> 2 -> 3 ->
    print("Intersection:", intersection(linked_list_5, linked_list_6)   #output - blank

    # Test Case 4 (Both Lists Empty)
    linked_list_7 = LinkedList()
    linked_list_8 = LinkedList()

    print("\nTest Case 4:")
    print("Union:", union(linked_list_7, linked_list_8))                #output - blank
    print("Intersection:", intersection(linked_list_7, linked_list_8))  #output - blank