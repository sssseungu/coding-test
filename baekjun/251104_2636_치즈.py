"""
DATE: 2025.11.04
치즈
URL
https://www.acmicpc.net/problem/2636

문제 설명

아래 <그림 1>과 같이 정사각형 칸들로 이루어진 사각형 모양의 판이 있고,
그 위에 얇은 치즈(회색으로 표시된 부분)가 놓여 있다.
판의 가장자리(<그림 1>에서 네모 칸에 X친 부분)에는 치즈가 놓여 있지 않으며 치즈에는 하나 이상의 구멍이 있을 수 있다.

이 치즈를 공기 중에 놓으면 녹게 되는데 공기와 접촉된 칸은 한 시간이 지나면 녹아 없어진다.
치즈의 구멍 속에는 공기가 없지만 구멍을 둘러싼 치즈가 녹아서 구멍이 열리면 구멍 속으로 공기가 들어가게 된다.
<그림 1>의 경우, 치즈의 구멍을 둘러싼 치즈는 녹지 않고 ‘c’로 표시된 부분만 한 시간 후에 녹아 없어져서 <그림 2>와 같이 된다.
('c'로 표시된 부분: 공기와 접촉한 치즈 칸)

다시 한 시간 후에는 <그림 2>에서 ‘c’로 표시된 부분이 녹아 없어져서 <그림 3>과 같이 된다.

<그림 3>은 원래 치즈의 두 시간 후 모양을 나타내고 있으며,
남은 조각들은 한 시간이 더 지나면 모두 녹아 없어진다.
그러므로 처음 치즈가 모두 녹아 없어지는 데는 세 시간이 걸린다.
<그림 3>과 같이 치즈가 녹는 과정에서 여러 조각으로 나누어 질 수도 있다.

입력으로 사각형 모양의 판의 크기와 한 조각의 치즈가 판 위에 주어졌을 때,
공기 중에서 치즈가 모두 녹아 없어지는 데 걸리는 시간과
모두 녹기 한 시간 전에 남아있는 치즈조각이 놓여 있는 칸의 개수를 구하는 프로그램을 작성하시오.
"""

import sys
from collections import deque

input = sys.stdin.readline


def find_cheese_outside_air_and_mark(cheese_map):

    visited = [[0] * w for _ in range(h)]
    queue = deque([(0, 0)])
    visited[0][0] = 1

    DIRECTIONS = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    while queue:
        cur_row, cur_col = queue.popleft()

        for direction in DIRECTIONS:
            d_row, d_col = direction
            next_row, next_col = cur_row + d_row, cur_col + d_col

            if 0 <= next_row < h and 0 <= next_col < w and not visited[next_row][next_col]:

                if cheese_map[next_row][next_col] == 0:
                    queue.append((next_row, next_col))
                    visited[next_row][next_col] = 1

                if cheese_map[next_row][next_col]:
                    cheese_map[next_row][next_col] = 2  # 녹을 치즈: 2로 마킹
                    visited[next_row][next_col] = 1  # 중복 마킹 방지


def count_cheese_melted(cheese_map):
    melt_count = 0
    for row in range(h):
        for col in range(w):
            if cheese_map[row][col] == 2:
                cheese_map[row][col] = 0
                melt_count += 1
    return melt_count


# with open("./coding_test/baekjun/input.txt", "r") as f:
#     h, w = map(int, f.readline().split())
#     cheese_map = [list(map(int, f.readline().split())) for _ in range(h)]

h, w = map(int, input().split())
cheese_map = [list(map(int, input().split())) for _ in range(h)]

time_to_melt = 0
last_melt_count = 0

while True:

    find_cheese_outside_air_and_mark(cheese_map)
    melted_count = count_cheese_melted(cheese_map)

    if melted_count == 0:
        break

    last_melt_count = melted_count
    time_to_melt += 1

print(time_to_melt)
print(last_melt_count)
