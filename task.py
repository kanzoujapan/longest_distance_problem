import sys
from collections import defaultdict

sys.setrecursionlimit(120000)

def element_split(lines):
    station_graph = defaultdict(list)
    for line in lines:
        start, end, distance = line.split(',')
        start = int(start)
        end = int(end)
        distance = float(distance)

        station_graph[start].append((end, distance))
        station_graph[end].append((start, distance))

    return station_graph




def dfs(current, graph, visited, path, total_distance):
    visited[current] = True
    path.append(current)

    global max_distance, best_path
    if total_distance > max_distance:
        max_distance = total_distance
        best_path = path.copy()

    for neighbor, weight in graph[current]:
        if not visited.get(neighbor, False):
            dfs(neighbor, graph, visited, path, total_distance + weight)

    visited[current] = False
    path.pop()


def find_longest_path(graph):
    global max_distance, best_path
    max_distance = 0
    best_path = []

    for start in graph.keys():
        visited = {}
        dfs(start, graph, visited, [], 0)

    return best_path


if __name__ == '__main__':
    lines = []
    for line in sys.stdin:
        lines.append(line.strip())

    graph = element_split(lines)
    longest_path = find_longest_path(graph)

    for node in longest_path:
        print(node)












