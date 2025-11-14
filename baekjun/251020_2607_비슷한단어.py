"""
Date: 2025.10.20
비슷한 단어 (구현, 문자열)
URL
https://www.acmicpc.net/problem/2607
"""

# import sys


# 단어의 문자 구성 반환
def count_chars(word):
    count_dict = {}
    for char in word:
        count_dict[char] = count_dict.get(char, 0) + 1
    return count_dict


# 구성이 같으면 True
def has_same_components(count_dict1, count_dict2):
    return count_dict1 == count_dict2


# 두 단어가 비슷한 단어인지 검사
def is_similar(word1, word2):
    count_dict1 = count_chars(word1)
    count_dict2 = count_chars(word2)

    # 구성이 같으면 비슷함
    if has_same_components(count_dict1, count_dict2):
        return True

    # 구성이 다를 경우: 두 단어의 문자 하나만 차이나는 경우
    for char in count_dict2:
        tmp_count_dict2 = count_dict2.copy()

        # word2의 문자 하나 지우기
        tmp_count_dict2[char] -= 1
        if tmp_count_dict2[char] == 0:
            del tmp_count_dict2[char]

        # word1과 문자 하나 없앤 word2의 구성 비교
        if has_same_components(count_dict1, tmp_count_dict2):
            return True

    for char in count_dict1:
        tmp_count_dict1 = count_dict1.copy()

        # word1의 문자 하나 지우기
        tmp_count_dict1[char] -= 1
        if tmp_count_dict1[char] == 0:
            del tmp_count_dict1[char]

        # 문자 하나 없앤 word1과 word2의 구성 비교
        if has_same_components(tmp_count_dict1, count_dict2):
            return True

    for char1 in count_dict1:
        for char2 in [chr(i) for i in range(65, 90 + 1)]:  # "A"~"Z" - ASCII code(65~90)
            if char1 != char2:
                tmp_count_dict1 = count_dict1.copy()

                # word1의 문자 하나 지우기
                tmp_count_dict1[char1] -= 1
                if tmp_count_dict1[char1] == 0:
                    del tmp_count_dict1[char1]

                # 지운 문자와 다른 새로운 문자 추가 (기존 문자를 교체)
                tmp_count_dict1[char2] = tmp_count_dict1.get(char2, 0) + 1

                # 문자 하나 교체한 word1과 word2의 구성 비교
                if has_same_components(tmp_count_dict1, count_dict2):
                    return True


if __name__ == "__main__":
    with open("./coding_test/baekjun/input.txt", "r") as f:
        num_words = int(f.readline().strip())
        word0 = f.readline().strip("\n")
        words = [row.strip("\n") for row in f.readlines()]

    # input = sys.stdin.readline
    # num_words = int(input())
    # word0 = input().strip("\n")
    # words = [input().strip("\n") for _ in range(num_words - 1)]

    similar_cnt = 0
    for word in words:
        if is_similar(word0, word):
            similar_cnt += 1

    print(similar_cnt)
