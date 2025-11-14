"""
Date: 2025.10.21
틱택토 (구현, 많은 조건 분기)
URL
https://www.acmicpc.net/problem/7682
"""

import sys


def check_win(game, marker):

    # 가로 체크
    for row in range(3):
        if all(game[row * 3 + col] == marker for col in range(3)):
            return True

    # 세로 체크
    for col in range(3):
        if all(game[row * 3 + col] == marker for row in range(3)):
            return True

    # 대각선 체크
    if all(game[n * 3 + n] == marker for n in range(3)) or all(game[n * 3 + (2 - n)] == marker for n in range(3)):
        return True

    return False


def is_valid(game: str):

    x_cnt = game.count("X")
    o_cnt = game.count("O")

    # "X"가 먼저 시작하므로, "X"의 개수는 항상 "O"의 개수보다 1개 크거나 같음
    if x_cnt > o_cnt + 1 or x_cnt < o_cnt:
        return False

    x_win = check_win(game, "X")
    o_win = check_win(game, "O")

    # 동시에 이기는 것은 불가능
    if x_win and o_win:
        return False

    # "O"가 이겼을 경우엔 반드시 "X"와 개수가 같아야 함
    if o_win and o_cnt != x_cnt:
        return False

    # "X"가 이겼을 경우엔 반드시 "O"보다 개수 1 커야함
    if x_win and x_cnt != o_cnt + 1:
        return False

    # 아직 끝까지 게임을 진행하지 않은 경우는 invalid
    if not (x_win or o_win) and x_cnt + o_cnt < 9:
        return False

    return True


if __name__ == "__main__":
    # with open("./coding_test/baekjun/input.txt", "r") as f:
    #     games = [row.strip("\n") for row in f.readlines()]
    #     del games[-1]

    input = sys.stdin.readline
    games = []
    while True:
        line = input().strip("\n")
        if line == "end":
            break
        else:
            games.append(line)

    for game in games:
        if is_valid(game):
            print("valid")
        else:
            print("invalid")
