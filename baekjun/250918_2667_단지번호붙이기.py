"""
Date: 25.09.18
단지번호붙이기(그래프, DFS/BFS, Grid)
URL
https://www.acmicpc.net/problem/2667
"""

import sys
from collections import deque


def find_apt(cur_row, cur_col):
    # (cur_row, cur_col)을 포함하는 단지의 크기를 반환하는 함수

    queue = deque([(cur_row, cur_col)])  # 단지에 속한 집의 좌표를 저장하는 queue
    visited[cur_row][cur_col] = 1  # 이 지점은 탐색한 것으로 표기
    count = 0  # 단지의 크기

    while queue:  # 탐색을 진행할 좌표가 남아있을 동안 순회
        cur_row, cur_col = queue.popleft()  # 탐색을 진행할 cur_row, cur_col을 업데이트
        count += 1
        for direction in DIRECTIONS:
            d_row, d_col = direction
            new_row = cur_row + d_row
            new_col = cur_col + d_col

            # 탐색할 좌표가 지도 범위를 벗어나지 않으면서,
            # 탐색할 좌표에 집이 있고, 과거에 그 곳을 탐색한 적 없으면:
            if 0 <= new_row < n and 0 <= new_col < n:
                if apt_map[new_row][new_col] and not visited[new_row][new_col]:
                    queue.append((new_row, new_col))  # 추후에 탐색을 이어갈 좌표 저장
                    visited[new_row][new_col] = 1  # 이 지점은 탐색한 것으로 표기

    return count


if __name__ == "__main__":

    # input
    input = sys.stdin.readline
    n = int(input())
    apt_map = [list(map(int, input().strip())) for _ in range(n)]

    DIRECTIONS = [(0, 1), (-1, 0), (0, -1), (1, 0)]  # (d_row, d_col)
    visited = [[0] * n for _ in range(n)]  # 중복해서 세는 것 방지하기 위한 2D list

    size_of_apts = []  # 단지의 크기를 저장하는 리스트
    for row in range(n):
        for col in range(n):
            if apt_map[row][col] and not visited[row][col]:
                size_of_apt = find_apt(cur_row=row, cur_col=col)
                size_of_apts.append(size_of_apt)

    num_apts = len(size_of_apts)
    size_of_apts.sort()

    # output
    print(num_apts)
    for size_of_apt in size_of_apts:
        print(size_of_apt)
