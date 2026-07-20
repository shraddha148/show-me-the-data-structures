import heapq
import math

def shortest_path(M, start, goal):
    if start == goal:
        return [start]

    open_set = []
    heapq.heappush(open_set, (0, start))

    came_from = {}
    g_score = {start: 0}

    def heuristic(node):
        x1, y1 = M.intersections[node]
        x2, y2 = M.intersections[goal]
        return math.sqrt((x1 - x2)**2 + (y1 - y2)**2)

    while open_set:
        _, current = heapq.heappop(open_set)

        if current == goal:
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            path.append(start)
            path.reverse()
            return path

        for neighbor in M.roads[current]:
            x1, y1 = M.intersections[current]
            x2, y2 = M.intersections[neighbor]
            distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

            tentative_g = g_score[current] + distance

            if neighbor not in g_score or tentative_g < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g

                f_score = tentative_g + heuristic(neighbor)
                heapq.heappush(open_set, (f_score, neighbor))

    return []