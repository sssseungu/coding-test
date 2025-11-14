"""
Date: 25.10.11
DFS와BFS
그래프이론, 그래프탐색, 너비우선탐색, 깊이우선탐색
URL:
https://www.acmicpc.net/problem/1260
"""

# 그래프를 DFS로 탐색한 결과와 BFS로 탐색한 결과를 출력하는 프로그램을 작성하시오.
# 단, 방문할 수 있는 정점이 여러 개인 경우에는 정점 번호가 작은 것을 먼저 방문하고,
# 더 이상 방문할 수 있는 점이 없는 경우 종료한다.
# 정점 번호는 1번부터 N번까지이다.

# 첫째 줄에 DFS를 수행한 결과를, 그 다음 줄에는 BFS를 수행한 결과를 출력한다.
# V부터 방문된 점을 순서대로 출력하면 된다.

# import sys
from collections import deque


# DFS: stack이나 recursive funtion을 이용
def dfs(graph, start_vertex):

    visited = []
    visited_set = set()
    stack = [start_vertex]

    while stack:
        vertex = stack.pop()
        if vertex in visited_set:
            continue

        visited.append(vertex)
        visited_set.add(vertex)

        # stack 구조를 구현하기 위해 reversed() 사용 (Last In First Out)
        for next_vertex in reversed(graph[vertex]):
            if next_vertex not in visited_set:
                stack.append(next_vertex)

    return visited


# BFS: queue나 linked list를 이용
def bfs(graph, start_vertex):

    visited = []
    visited_set = set([start_vertex])
    queue = deque([start_vertex])

    while queue:
        vertex = queue.popleft()
        visited.append(vertex)

        for next_vertex in graph[vertex]:
            if next_vertex not in visited_set:
                visited_set.add(next_vertex)
                queue.append(next_vertex)

    return visited


if __name__ == "__main__":

    with open("./coding_test/baekjun/input.txt", "r") as f:
        num_v, num_e, start_v = map(int, f.readline().split())
        edges = [tuple(map(lambda x: x - 1, map(int, f.readline().split()))) for _ in range(num_e)]

    # input = sys.stdin.readline
    # num_v, num_e, start_v = map(int, input().split())
    # edges = [tuple(map(lambda x: x - 1, map(int, input().split()))) for _ in range(num_e)]

    start_v -= 1
    g = [[] for _ in range(num_v)]  # graph

    for edge in edges:
        v1, v2 = edge
        g[v1].append(v2)
        g[v2].append(v1)

    g = [sorted(v_list) for v_list in g]

    visited_v_dfs = dfs(g, start_v)
    visited_v_dfs = [vertex + 1 for vertex in visited_v_dfs]

    visited_v_bfs = bfs(g, start_v)
    visited_v_bfs = [vertex + 1 for vertex in visited_v_bfs]

    print(" ".join(map(str, visited_v_dfs)))
    print(" ".join(map(str, visited_v_bfs)))
