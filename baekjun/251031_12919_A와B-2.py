"""
DATE: 2025.10.31
A와 B 2
URL
https://www.acmicpc.net/problem/12919
"""

# import sys
# input = sys.stdin.readline


def backtrack(in_str: str):

    if len(in_str) == len(s):
        return 1 if in_str == s else 0

    l_char = in_str[0]
    r_char = in_str[-1]

    str_type = l_char + r_char
    if str_type == "AA":
        return backtrack(in_str[:-1])
    elif str_type == "BB":
        in_str = in_str[1:]
        return backtrack(in_str[::-1])
    elif str_type == "BA":
        in_str_tmp = in_str[1:]
        return backtrack(in_str[:-1]) or backtrack(in_str_tmp[::-1])
    else:
        return 0


if __name__ == "__main__":
    # s = input().strip()
    # t = input().strip()

    with open("./coding_test/baekjun/input.txt", "r") as f:
        s = f.readline().strip()
        t = f.readline().strip()

    print(backtrack(t))
