"""
DATE: 2025.11.16
줄세우기
URL
https://www.acmicpc.net/problem/2252
"""

import sys
from collections import deque

input = sys.stdin.readline
n, m = map(int, input().strip().split())

graph = [[] for _ in range(n + 1)]
indegree = [0] * (n + 1)

for _ in range(m):
    a, b = map(int, input().strip().split())
    graph[a].append(b)  # a -> b
    indegree[b] += 1  # node b로 들어오는 (a -> b) edge 개수 (node의 차원 수)

queue = deque()
for i in range(1, n + 1):
    if indegree[i] == 0:  # 들어오는 edge가 없는 node 먼저 배치
        queue.append(i)

print(f"graph: {graph}")
print(f"indegree: {indegree}")
print(f"queue: {list(queue)}")

result = []
while queue:
    node = queue.popleft()
    result.append(node)

    for next_node in graph[node]:
        indegree[next_node] -= 1
        if indegree[next_node] == 0:
            queue.append(next_node)

print(" ".join(map(str, result)))
