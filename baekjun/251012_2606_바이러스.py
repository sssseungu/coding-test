"""
Date: 25.10.12
바이러스 (그래프 이론, 그래프 탐색, 너비우선탐색, 깊이우선탐색)
URL
https://www.acmicpc.net/problem/2606
"""

# 컴퓨터의 수와 네트워크 상에서 서로 연결되어 있는 정보가 주어질 때,
# 1번(index 0번) 컴퓨터를 통해 웜 바이러스에 걸리게 되는 컴퓨터의 수를 출력하는 프로그램을 작성하시오.

import sys
from collections import deque


def bfs(network, start_com):

    queue = deque([start_com])
    visited_set = set()

    while queue:
        cur_com = queue.popleft()
        visited_set.add(cur_com)

        for next_com in network[cur_com]:
            if next_com not in visited_set:
                queue.append(next_com)

    return len(visited_set) - 1


if __name__ == "__main__":

    # with open("./coding_test/baekjun/input.txt", "r") as f:
    #     num_coms = int(f.readline().strip())
    #     num_links = int(f.readline().strip())
    #     links = [tuple(map(int, f.readline().split())) for _ in range(num_links)]

    input = sys.stdin.readline
    num_coms = int(input().strip())
    num_links = int(input().strip())
    links = [tuple(map(int, input().split())) for _ in range(num_links)]

    nw = [[] for _ in range(num_coms)]
    for com1, com2 in links:
        nw[com1 - 1].append(com2 - 1)
        nw[com2 - 1].append(com1 - 1)

    print(bfs(nw, 0))
