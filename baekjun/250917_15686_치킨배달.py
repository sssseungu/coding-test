"""
Date: 25.09.17
치킨 배달(백트래킹, 브루트포스)
URL
https://www.acmicpc.net/problem/15686
"""

import sys
from itertools import combinations


def min_chick_distance(N, M, city_map):
    # N: 도시 면적의 크기
    # M: 도시에 남길 치킨집 수

    # 집과 치킨집의 좌표를 저장
    houses = []
    shops = []

    for i in range(N):
        for j in range(N):
            if city_map[i][j] == 1:  # 1: house
                houses.append((i, j))
            elif city_map[i][j] == 2:  # 2: shop
                shops.append((i, j))

    # 치킨집 중에서 M개를 선택하는 모든 조합에 대해 치킨 거리 계산
    min_chicken_distance = float("inf")

    # 치킨집 중에서 M개 선택하는 모든 경우의 수 -> combinations
    for selected_shops in combinations(shops, M):
        # 현재 선택된 치킨집들에 대해 도시의 '치킨 거리' 계산
        total_distance = 0

        for house in houses:
            house_row, house_col = house
            # 각 집에서 가장 가까운 치킨집까지의 거리
            min_distance = float("inf")

            for shop in selected_shops:
                shop_row, shop_col = shop
                distance = abs(house_row - shop_row) + abs(house_col - shop_col)
                min_distance = min(min_distance, distance)

            total_distance += min_distance

        min_chicken_distance = min(min_chicken_distance, total_distance)

    return min_chicken_distance


# input = sys.stdin.readline
# N, M = map(int, input().split())
# city_map = [list(map(int, input().split())) for _ in range(N)]

sys.stdin = open(
    "/Users/Seungwoo/Library/CloudStorage/OneDrive-Personal/Documents/0 PROJECT/AIT8_w01-03_coding-test/baekjun/15686_input.txt"
)
N, M = map(int, sys.stdin.readline().split())
city_map = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
print(min_chick_distance(N, M, city_map))
