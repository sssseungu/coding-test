"""
DATE: 25.11.05
물대기
URL
https://www.acmicpc.net/problem/1368
"""

# 선주는 자신이 운영하는 N개의 논에 물을 대려고 한다.
# 물을 대는 방법은 두 가지가 있는데 하나는 직접 논에 우물을 파는 것이고,
# 다른 하나는 이미 물을 대고 있는 다른 논으로부터 물을 끌어오는 법이다.

# 각각의 논에 대해 우물을 파는 비용과 논들 사이에 물을 끌어오는 비용들이 주어졌을 때,
# 최소의 비용으로 모든 논에 물을 대는 것이 문제이다.
import sys

input = sys.stdin.readline


# with open("./baekjun/input.txt", "r") as f:

#     num_paddy = int(f.readline().strip())  # 논의 수
#     costs_to_make_well = list(int(f.readline().strip()) for _ in range(num_paddy))
#     costs_to_connect = [list(map(int, f.readline().strip().split())) for _ in range(num_paddy)]

num_paddy = int(input().strip())
costs_to_make_well = list(int(input().strip()) for _ in range(num_paddy))
costs_to_connect = [list(map(int, input().strip().split())) for _ in range(num_paddy)]

# **알고리즘을 잘 몰라서, 해답을 참고하여 작성하였음**

# Kruscal algorithm
# Edge 중심으로 접근하는 알고리즘
# 모든 edge를 weight(cost)값 기준으로 오름차순 정렬 후,
# weight가 작은 edge부터 선택하면서 tree를 구성
# 단, loop가 형성되는 edge는 제외해야하므로, 이를 위해 "union-find" 자료 구조를 이용한다.
# 모든 v개의 node가 연결될 때까지 = (v-1)개의 edge가 연결될 때까지 반복.

# 가상의 vertex 0를 추가하고,
# 논에 우물을 파는 것을 가상의 vertex 0과 논을 연결한 edge로 간주한다.
# (cost, start_vertex, end_vertex)

edges = []
for i in range(num_paddy):
    edges.append((costs_to_make_well[i], 0, i + 1))
    for j in range(num_paddy):
        if i < j:
            edges.append((costs_to_connect[i][j], i + 1, j + 1))

edges.sort()

# union-find를 위한 부모 배열
# [i]번째 원소의 값은 [i]-node의 부모 node의 index값임.
parent: list[int] = [i for i in range(num_paddy + 1)]


# find 함수 (경로 압축: 탐색에 드는 계산 복잡도가 O(1) 수준으로 감소)
# [i]번째 node의 최상단 parent node를 반환함
def find_parent(node):
    if parent[node] != node:
        parent[node] = find_parent(parent[node])
    return parent[node]


# union 함수
def union(a, b):
    a_root = find_parent(a)
    b_root = find_parent(b)

    if a_root < b_root:
        parent[b_root] = a_root
    else:
        parent[a_root] = b_root


total_cost = 0
edge_count = 0

for cost, start, end in edges:
    # 두 정점이 이미 연결되어 있는지 확인
    if find_parent(start) != find_parent(end):
        union(start, end)
        total_cost += cost
        edge_count += 1

        # n개의 논과 1개의 가상 정점 [0]을 연결하려면 n개의 간선이 필요
        if edge_count == num_paddy:
            break

print(total_cost)
