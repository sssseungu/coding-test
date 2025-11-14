"""
Date: 25.09.09
전화번호 목록(hash)
URL
https://school.programmers.co.kr/learn/courses/30/lessons/42577
"""

# solution 1 Hash 이용하지 않은 풀이


def solution(phone_book):
    phone_book.sort()  # 정렬 먼저. (사전순으로 정렬됨.)
    for i in range(len(phone_book) - 1):
        if phone_book[i + 1].startswith(phone_book[i]):  # 인접한 두 전화번호만 비교.
            return False
    return True


# # solution 2 Hash 이용한 풀이

# def solution(phone_book):

#     # hash 테이블 만들기 (key-value)
#     # 전화번호-hash값은 1-1 매핑됨. (동일하지 않은 모든 객체는 서로 다른 hash값을 가진다고 함.)
#     phone_hash = {hash(phone_num): phone_num for phone_num in phone_book}

#     # 전화번호부의 모든 전화번호에 대해 탐색.
#     for phone_num in phone_book:
#         L = len(phone_num)

#         # 각 전화번호의 prefix 길이는 1부터 (L-1)까지
#         for prefix_len in range(1, L):

#             prefix = phone_num[:prefix_len] # prefix
#             prefix_hash = hash(prefix)      # prefix에 대한 hash값(고유함).

#             # phone_hash에서 prefix_hash에 대응되는 전화번호 찾기
#             if prefix_hash in phone_hash:
#                 return False # 하나라도 존재하면 False 반환 후 종료

#     return True # 하나도 없으면 True
