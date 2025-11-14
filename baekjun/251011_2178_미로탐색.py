"""
Date: 2025.10.12
미로탐색 (그래프 이론, 그래프 탐색, 너비 우선 탐색, 격자 그래프)
URL
https://www.acmicpc.net/problem/2178
"""

import sys
from collections import deque


def bfs(maze, start_pos):

    queue = deque([(*start_pos, 1)])
    visited = [start_pos]

    DIRECTIONS = [(0, 1), (-1, 0), (0, -1), (1, 0)]
    while queue:
        # print(queue)
        cur_row, cur_col, dist = queue.popleft()
        if (cur_row, cur_col) == (n - 1, m - 1):
            return dist

        for direction in DIRECTIONS:
            d_row, d_col = direction
            next_row, next_col = cur_row + d_row, cur_col + d_col
            if (
                0 <= next_row < n
                and 0 <= next_col < m
                and maze[next_row][next_col]
                and (next_row, next_col) not in visited
            ):
                queue.append((next_row, next_col, dist + 1))
                visited.append((next_row, next_col))

    return -1


if __name__ == "__main__":

    # with open("./coding_test/baekjun/input.txt", "r") as f:
    #     n, m = map(int, f.readline().split())
    #     str_list = list(f.readline().strip() for _ in range(n))
    #     maze = [[int(digit) for digit in num_str] for num_str in str_list]

    input = sys.stdin.readline
    n, m = map(int, input().split())
    str_list = list(input().strip() for _ in range(n))
    maze = [[int(digit) for digit in num_str] for num_str in str_list]

    start_pos = (0, 0)
    # print(f"Maze size: {n}x{m}")
    print(bfs(maze, start_pos))
