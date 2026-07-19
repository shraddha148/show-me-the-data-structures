import heapq
import math
from typing import Optional


def heuristic(map, node, goal) -> float:
    """
    Calculate the Euclidean distance between two points.

    Args:
        a (tuple[float, float]): The coordinates of the first point (x1, y1).
        b (tuple[float, float]): The coordinates of the second point (x2, y2).

    Returns:
        float: The Euclidean distance between the two points.
    """
    x1, y1 = map.intersections[node]
    x2, y2 = map.intersections[goal]

    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def reconstruct_path(came_from: dict[int, int], current: int) -> list[int]:
    """
    Reconstruct the path from the start node to the goal node.

    Args:
        came_from (dict[int, int]): A dictionary mapping each node to the node it came from.
        current (int): The goal node.

    Returns:
        list[int]: The reconstructed path from the start node to the goal node.
    """
    path = [current]

    while current in came_from:
        current = came_from[current]
        path.append(current)

    path.reverse()
    return path

def shortest_path(map, start, goal):
    """
    Find the shortest path between two nodes in a map using the A* algorithm.

    Args:
        M (Map): The map containing the graph, intersections, and roads.
        start (int): The starting node.
        goal (int): The goal node.

    Returns:
        Optional[list[int]]: The shortest path from the start node to the goal node, or None if no path is found.
    """
    # Priority queue
    open_list = []
    heapq.heappush(open_list, (0, start))

    # Cost from start to each node
    g_cost = {start: 0}

    # Parent dictionary
    came_from = {}

    # Visited nodes
    visited = set()

    while open_list:

        current_cost, current = heapq.heappop(open_list)

        if current == goal:
            return reconstruct_path(came_from, current)

        if current in visited:
            continue

        visited.add(current)

        for neighbor in map.roads[current]:

            x1, y1 = map.intersections[current]
            x2, y2 = map.intersections[neighbor]

            distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

            new_cost = g_cost[current] + distance

            if neighbor not in g_cost or new_cost < g_cost[neighbor]:
                g_cost[neighbor] = new_cost

                priority = new_cost + heuristic(map, neighbor, goal)

                heapq.heappush(open_list, (priority, neighbor))

                came_from[neighbor] = current

    return []
