"""
Date: 25.09.19
귀여운 라이언(슬라이딩 윈도우, 두 포인터)
URL
https://www.acmicpc.net/problem/15565
"""

import sys


def shortest_ryan_set(doll_seq, n, k):

    l_end, r_end = 0, 0
    ryan_cnt = 1 if doll_seq[l_end] == "1" else 0
    minimum_len = float("inf")

    while r_end < n:

        if l_end > r_end:
            break

        if ryan_cnt < k:
            if r_end == n - 1:
                break
            r_end += 1
            ryan_cnt += 1 if doll_seq[r_end] == "1" else 0

        else:
            len_subseq = r_end - l_end + 1
            minimum_len = min(minimum_len, len_subseq)
            ryan_cnt -= 1 if doll_seq[l_end] == "1" else 0
            l_end += 1

    return -1 if minimum_len == float("inf") else minimum_len


if __name__ == "__main__":
    n, k = tuple(map(int, sys.stdin.readline().split()))
    doll_seq = sys.stdin.readline().rstrip().replace(" ", "")
    print(shortest_ryan_set(doll_seq, n, k))


# ----- 시간초과로 실패 ----- #

# import sys
# import heapq


# def shortest_ryan_set(doll_seq, n, k):

#     len_heap = []
#     l_end, r_end = 0, k

#     while r_end <= n:

#         sub_seq = doll_seq[l_end:r_end]  # slicing도 메모리 순회하므로 크기만큼 복잡해짐.
#         ryan_cnt = sub_seq.count("1")  # O(n) <<
#         if ryan_cnt < k:
#             r_end += 1

#         elif ryan_cnt == k:
#             if len(sub_seq) == k:  # sub_seq = "111"
#                 return k
#             else:
#                 heapq.heappush(len_heap, len(sub_seq))  # O(logn) <<
#                 # l_end += 1
#                 left_ryan_idx = sub_seq.find("1")
#                 l_end += sub_seq[left_ryan_idx + 1 :].find("1")
#         else:
#             print("something's wrong.")

#     if not len_heap:
#         return -1
#     else:
#         return heapq.heappop(len_heap)


# n, k = tuple(map(int, sys.stdin.readline().split()))
# doll_seq = sys.stdin.readline().rstrip().replace(" ", "")
# print(shortest_ryan_set(doll_seq, n, k))
