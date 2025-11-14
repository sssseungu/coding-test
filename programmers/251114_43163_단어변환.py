"""
DATE: 2025.11.14
단어변환
URL
https://school.programmers.co.kr/learn/courses/30/lessons/43163?language=python3
"""

from collections import deque


# 두 단어가 한 글자 이하로 차이가 나면 True, 그렇지 않으면 False
def is_similar(word1: str, word2: str) -> bool:
    if len(word1) != len(word2):
        return False

    diff_count = 0
    for idx, char1 in enumerate(word1):
        if char1 != word2[idx]:
            diff_count += 1
        if diff_count > 1:
            return False

    return True


def BFS(begin_word: str, target_word: str, words: list[str]):

    count = 0
    queue = deque([[begin_word]])
    visited = [False] * len(words)

    # words 내에 begin_word가 있을 경우, 그 단어는 제외 (이미 방문한 것으로 간주)
    if begin_word in words:
        visited[words.index(begin_word)] = True

    next_words = []  # 단계별로 count를 업데이트하기 위해 next_words라는 리스트 선언 후 tuple로 묶음
    while queue:

        cur_words = queue.popleft()
        if target_word in cur_words:
            return count

        for idx, word in enumerate(words):

            # words 내 단어 중 아직 탐색하지 않은 단어들만 고려
            if visited[idx]:
                continue

            # 현 단계의 단어들에 대해
            for cur_word in cur_words:
                if is_similar(cur_word, word):
                    next_words.append(word)
                    visited[idx] = True

        queue.append(next_words)
        next_words = []
        count += 1

    return 0


def solution(begin, target, words):

    if target not in words:
        return 0

    return BFS(begin, target, words)
