import sys
import heapq

INF = int(1e9)

def dijkstra(start, n, graph):
    distance = [INF] * (n + 1)
    distance[start] = 0
    pq = []
    heapq.heappush(pq, (0, start))
    
    while pq:
        dist, now = heapq.heappop(pq)
        if dist > distance[now]:
            continue
        for next_node, cost in graph[now]:
            new_cost = dist + cost
            if new_cost < distance[next_node]:
                distance[next_node] = new_cost
                heapq.heappush(pq, (new_cost, next_node))
    
    return distance

# Input
input = sys.stdin.read
lines = input().splitlines()

# First line: number of nodes and edges
n, e = map(int, lines[0].split())

graph = [[] for _ in range(n + 1)]

# Next `e` lines: edges and their weights
for i in range(1, e + 1):
    a, b, c = map(int, lines[i].split())
    graph[a].append((b, c))
    graph[b].append((a, c))

# Last line: mandatory nodes
v1, v2 = map(int, lines[e + 1].split())

# Calculate shortest paths
distance_from_start = dijkstra(1, n, graph)
distance_from_v1 = dijkstra(v1, n, graph)
distance_from_v2 = dijkstra(v2, n, graph)

# Calculate paths
path1 = distance_from_start[v1] + distance_from_v1[v2] + distance_from_v2[n]
path2 = distance_from_start[v2] + distance_from_v2[v1] + distance_from_v1[n]

# Check for valid paths
shortest_path = min(path1, path2)

# Output the result
if shortest_path >= INF:
    print(-1)
else:
    print(shortest_path)
