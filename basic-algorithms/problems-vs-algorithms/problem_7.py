"""
Problem 7: Request Routing in a Web Server with a Trie

This module implements an HTTPRouter using a Trie data structure.

The HTTPRouter takes a URL path like "/", "/about", or 
"/blog/2019-01-15/my-awesome-blog-post" and determines the appropriate handler 
to return. The Trie is used to efficiently store and retrieve handlers based on 
the parts of the path separated by slashes ("/").

The RouteTrie stores handlers under path parts, and the Router delegates adding 
and looking up handlers to the RouteTrie. The Router also includes a not found 
handler for paths that are not found in the Trie and handles trailing slashes 
to ensure requests for '/about' and '/about/' are treated the same.

You sould implement the function bodies the function signatures. Use the test 
cases provided below to verify that your algorithm is correct. If necessary, 
add additional test cases to verify that your algorithm works correctly.
"""

from typing import Optional

class RouteTrieNode:
    """
    A node in the RouteTrie, representing a part of a route.

    Attributes:
    children (dict): A dictionary mapping part of the route to the corresponding RouteTrieNode.
    handler (Optional[str]): The handler associated with this node, if any.
    """
    def __init__(self):
        """
        Initialize a RouteTrieNode with an empty dictionary for children and no handler.
        """

        self.children = {}
        self.handler = None

class RouteTrie:
    """
    A trie (prefix tree) for storing routes and their handlers.

    Attributes:
    root (RouteTrieNode): The root node of the trie.
    """
    def __init__(self, root_handler: str):

        # Root node represents "/"
        self.root = RouteTrieNode()
        self.root.handler = root_handler

    def insert(self, parts, handler: str) -> None:
        """
               Add a path and its handler to the trie.

               Args:
                   parts (list): List of path parts.
                   handler (str): Handler for the path.
               """
        current = self.root

        for part in parts:
            if part not in current.children:
                current.children[part] = RouteTrieNode()

            current = current.children[part]

        current.handler = handler



    def find(self, path_parts: list[str]) ->  Optional[str]:

        """
                Find and return the handler for a path.

                Args:
                    parts (list): List of path parts.

                Returns:
                    handler if found, otherwise None.
                """
        current = self.root

        for part in path_parts:
            if part not in current.children:
                return None

            current = current.children[part]

        return current.handler

class Router:
    """
    A router to manage routes and their handlers using a RouteTrie.

    Attributes:
    route_trie (RouteTrie): The trie used to store routes and handlers.
    not_found_handler (str): The handler to return when a route is not found.
    """
    def __init__(self, root_handler, not_found_handler):
        """
        Create a router with root and 404 handlers.
        """
        self.router = RouteTrie(root_handler)
        self.not_found_handler = not_found_handler

    def add_handler(self, path, handler):
        """
        Add a handler for a path.
        """
        parts = self.split_path(path)
        self.router.insert(parts, handler)

    def lookup(self, path):
        """
        Return the handler for a given path.
        """
        parts = self.split_path(path)

        # Root path
        if len(parts) == 0:
            return self.router.root.handler

        handler = self.router.find(parts)

        if handler is None:
            return self.not_found_handler

        return handler

    def split_path(self, path):
        """
        Split the path into components.

        Examples:
        "/" -> []
        "/home/about" -> ["home", "about"]
        "/home/about/" -> ["home", "about"]
        """
        return [part for part in path.strip("/").split("/") if part]

## Test cases and expected outputs
## create the router and add a route

router = Router("root handler", "not found handler") # remove the 'not found handler' if you did not implement this
router.add_handler("/home/about", "about handler")  # add a route

## some lookups with the expected output
print(router.lookup("/")) # should print 'root handler'
print(router.lookup("/home")) # should print 'not found handler' or None if you did not implement one
print(router.lookup("/home/about")) # should print 'about handler'
print(router.lookup("/home/about/")) # should print 'about handler' or None if you did not handle trailing slashes
print(router.lookup("/home/about/me")) # should print 'not found handler' or None if you did not implement one
