"""
DATE: 2025.10.27
레이저통신 (그래프이론, 너비우선탐색, 최단경로, 데이크스트라, 격자그래프)
URL
https://www.acmicpc.net/problem/6087
"""

import sys
from collections import deque

input = sys.stdin.readline


def is_available(board, x, y):
    if 0 <= x < w and 0 <= y < h and board[y][x] != "*":
        return True
    return False


def BFS(board, c_positions, min_mircnt):

    mir_cnt = 0
    start_x, start_y = c_positions[0]
    end_x, end_y = c_positions[1]
    DIRECTIONS = [(1, 0), (0, 1), (-1, 0), (0, -1)]

    queue = deque()
    for dir_idx in range(4):
        queue.append((start_x, start_y, dir_idx, mir_cnt))
        min_mircnt[(start_x, start_y)][dir_idx] = 0

    while queue:
        cur_x, cur_y, cur_diridx, cur_mircnt = queue.popleft()
        for dir_idx in range(4):

            if abs(dir_idx - cur_diridx) == 2:  # 반대 방향은 고려 대상이 아님
                continue

            if cur_mircnt > min_mircnt[(cur_x, cur_y)][dir_idx]:
                continue

            dx, dy = DIRECTIONS[dir_idx]
            next_x, next_y = cur_x + dx, cur_y + dy

            if dir_idx == cur_diridx:  # 같은 방향일 경우
                if is_available(board, next_x, next_y):
                    if cur_mircnt < min_mircnt[(next_x, next_y)][dir_idx]:
                        # (next_x, next_y) 도달하기 위해 필요한 최소 거울 수 업데이트
                        min_mircnt[(next_x, next_y)][dir_idx] = cur_mircnt
                        # 같은 방향을 우선 처리하도록 appendleft
                        queue.appendleft((next_x, next_y, dir_idx, cur_mircnt))

            else:  # 다른 방향일 경우
                if is_available(board, next_x, next_y):
                    next_mircnt = cur_mircnt + 1
                    if next_mircnt < min_mircnt[(next_x, next_y)][dir_idx]:
                        # (next_x, next_y) 도달하기 위해 필요한 최소 거울 수 업데이트
                        min_mircnt[(next_x, next_y)][dir_idx] = next_mircnt
                        # 다른 방향은 나중에 처리하도록 append
                        queue.append((next_x, next_y, dir_idx, next_mircnt))

    return min(min_mircnt[(end_x, end_y)])


if __name__ == "__main__":

    with open("./coding_test/baekjun/input.txt", "r") as f:
        w, h = map(int, f.readline().rstrip().split())
        board = [list(f.readline().rstrip()) for _ in range(h)]
        board = board[::-1]

    # w, h = map(int, input().rstrip().split())
    # board = [list(input().rstrip()) for _ in range(h)]
    # board = board[::-1]

    INF = float("inf")
    c_positions = [(x, y) for x in range(w) for y in range(h) if board[y][x] == "C"]
    min_mircnt = {}
    for x in range(w):
        for y in range(h):
            min_mircnt[(x, y)] = min_mircnt.get((x, y), [float("inf")] * 4)

    print(BFS(board, c_positions, min_mircnt))
