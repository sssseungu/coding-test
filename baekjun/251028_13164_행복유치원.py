"""
DATE: 2025.10.28
행복유치원
URL
https://www.acmicpc.net/problem/13164
"""

# K개의 조로 나누고 조별로 단체 티셔츠를 맞추는데,
# 티셔츠를 맞추는 비용은 키가 가장 큰 원생과 작은 원생의 차이만큼이다.
# K개 조에 대해 티셔츠 만드는 비용의 합을 최소로 하고자 하려면 어떻게 해야할까?

import sys

input = sys.stdin.readline

if __name__ == "__main__":
    # with open("./coding_test/baekjun/input.txt", "r") as f:
    #     n, k = map(int, f.readline().rstrip().split())
    #     nums = list(map(int, f.readline().rstrip().split()))

    n, k = map(int, input().rstrip().split())
    nums = list(map(int, input().rstrip().split()))

    # k개의 조로 나누는 것은 (k-1)개의 칸막이를 두는 것과 동치.

    # 이웃 항과의 차를 담은 리스트 diffs를 정의했을 때,
    # (k-1)개의 칸막이를 두는 것은 diff 원소 중 (k-1)개의 원소가 삭제되는 것과 동치
    # nums  [1 3] | [5 6] | [10]
    # diffs   2   2   1   4
    #         X       X

    diffs = [0] * (n - 1)
    for i in range(1, n):
        diffs[i - 1] = nums[i] - nums[i - 1]

    # diffs 값 중 가장 큰 (k-1)개의 값을 제거했을 때,
    # 티셔츠 비용이 최소가 된다.

    sorted_diffs = sorted(diffs, reverse=True)
    print(sum(sorted_diffs[k - 1 :]))
