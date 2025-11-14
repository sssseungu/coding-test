"""
DATE: 2025.10.24
두 동전 (그래프 이론, BFS)
URL
https://www.acmicpc.net/problem/16197
"""

import sys
from collections import deque

input = sys.stdin.readline


def BFS(board, coins_pos):

    move_cnt = 0
    r0, c0 = coins_pos[0]  # 0번 coin의 위치
    r1, c1 = coins_pos[1]  # 1번 coin의 위치
    queue = deque([(r0, c0, r1, c1, move_cnt)])

    visited = set()
    visited.add((r0, c0, r1, c1))

    DIRECTIONS = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    while queue:
        r0, c0, r1, c1, move_cnt = queue.popleft()

        if move_cnt >= 10:
            continue

        for dr, dc in DIRECTIONS:
            next_r0, next_c0 = r0 + dr, c0 + dc
            next_r1, next_c1 = r1 + dr, c1 + dc

            out0 = not (0 <= next_r0 < n and 0 <= next_c0 < m)
            out1 = not (0 <= next_r1 < n and 0 <= next_c1 < m)

            if out0 and out1:
                continue

            if out0 or out1:
                return move_cnt + 1

            if board[next_r0][next_c0] == "#":
                next_r0, next_c0 = r0, c0
            if board[next_r1][next_c1] == "#":
                next_r1, next_c1 = r1, c1

            if (next_r0, next_c0, next_r1, next_c1) not in visited:
                visited.add((next_r0, next_c0, next_r1, next_c1))
                queue.append((next_r0, next_c0, next_r1, next_c1, move_cnt + 1))

    return -1


if __name__ == "__main__":

    # with open("./coding_test/baekjun/input.txt", "r") as f:
    #     n, m = map(int, f.readline().strip("\n").split())
    #     board = [list(f.readline().strip("\n")) for _ in range(n)]

    n, m = map(int, input().rstrip("\n").split())
    board = [list(input().rstrip("\n")) for _ in range(n)]

    # 동전 위치 저장
    coins = []
    for i in range(n):
        for j in range(m):
            if board[i][j] == "o":
                coins.append((i, j))

    print(BFS(board, coins))
