"""
DATE: 2025.10.23
영역구하기 (그래프탐색, BFS, DFS, 격자그래프, 플러드 필)
URL
https://www.acmicpc.net/problem/2583
"""

import sys
from collections import deque

input = sys.stdin.readline


def BFS(board, start_point):

    DIRECTIONS = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    queue = deque([start_point])
    start_x, start_y = start_point
    board[start_y][start_x] = 0
    cnt = 0

    while queue:
        x, y = queue.popleft()
        cnt += 1

        for direction in DIRECTIONS:
            dx, dy = direction
            next_x, next_y = x + dx, y + dy

            if not (0 <= next_x < n and 0 <= next_y < m):
                continue
            if not board[next_y][next_x]:
                continue

            board[next_y][next_x] = 0
            queue.append((next_x, next_y))

    return cnt


if __name__ == "__main__":
    with open("./coding_test/baekjun/input.txt", "r") as f:
        m, n, k = map(int, f.readline().split())  # n: 카드 개수, m: 합체 횟수
        rects = [tuple(map(int, f.readline().strip("\n").split())) for _ in range(k)]

    # m, n, k = map(int, input().split())
    # rects = [tuple(map(int, input().strip("\n").split())) for _ in range(k)]

    board = [[1] * n for _ in range(m)]

    for x in range(n):
        for y in range(m):

            for rect in rects:
                min_x, min_y, max_x, max_y = rect
                if min_x <= x < max_x and min_y <= y < max_y:
                    board[y][x] = 0

    cnt_list = []
    for x in range(n):
        for y in range(m):
            if board[y][x]:
                cnt = BFS(board, (x, y))
                cnt_list.append(cnt)

    cnt_list.sort()
    print(len(cnt_list))
    print(*cnt_list)
