"""
Date: 2025.10.22
카드 합체 놀이 (자료 구조, 그리디 알고리즘, 우선순위 큐)
URL
https://www.acmicpc.net/problem/15903
"""

import heapq
import sys

input = sys.stdin.readline


def game(m: int, num_list: list[int]):

    heap = num_list.copy()
    heapq.heapify(heap)

    for _ in range(m):
        x = heapq.heappop(heap)
        y = heapq.heappop(heap)

        heapq.heappush(heap, x + y)
        heapq.heappush(heap, x + y)

    return sum(heap)


if __name__ == "__main__":
    # with open("./coding_test/baekjun/input.txt", "r") as f:
    #     n, m = map(int, f.readline().split())  # n: 카드 개수, m: 합체 횟수
    #     nums = list(map(int, f.readline().split()))

    n, m = map(int, input().split())
    nums = list(map(int, input().split()))

    print(game(m, nums))
