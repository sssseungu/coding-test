"""
Date: 25.09.02
타겟넘버 (DFS/BFS)
URL
https://school.programmers.co.kr/learn/courses/30/lessons/43165
"""


def solution(numbers, target):

    n = len(numbers)
    total_cases = 2**n

    sign_combinations = []

    for i in range(total_cases):
        binary_pattern = bin(i)[2:].zfill(n)
        signs = [1 if bit == "0" else -1 for bit in binary_pattern]
        sign_combinations.append(signs)

    num_counts = 0
    for signs in sign_combinations:
        total = sum(num * sign for num, sign in zip(numbers, signs))
        if total == target:
            num_counts += 1

    return num_counts
