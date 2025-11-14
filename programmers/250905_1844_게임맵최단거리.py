"""
Date: 25.09.05
게임 맵 최단거리(DFS/BFS)
URL
https://school.programmers.co.kr/learn/courses/30/lessons/1844
"""

from collections import deque


def solution(maps):

    NUM_ROW = len(maps)
    NUM_COL = len(maps[0])

    # (d_row, d_col)
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    # row, column, length_of_trace
    queue = deque([(0, 0, 1)])

    visited = [[0] * NUM_COL for _ in range(NUM_ROW)]
    visited[0][0] = 1

    while queue:

        row, col, len_trace = queue.popleft()

        if row == NUM_ROW - 1 and col == NUM_COL - 1:
            return len_trace

        for d_row, d_col in directions:
            new_row = row + d_row
            new_col = col + d_col

            if (
                0 <= new_row < NUM_ROW
                and 0 <= new_col < NUM_COL
                and maps[new_row][new_col]
                and not visited[new_row][new_col]
            ):

                visited[new_row][new_col] = 1
                queue.append((new_row, new_col, len_trace + 1))

    return -1
