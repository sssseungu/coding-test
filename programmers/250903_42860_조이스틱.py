"""
Date: 25.09.03
조이스틱(Greedy)
URL
https://school.programmers.co.kr/learn/courses/30/lessons/42860
"""


def solution(name):

    def command_num_to_find_char(c):
        # 'A'에서 원하는 문자 c로 바꾸기 위해 필요한 최소 조작 횟수 return
        # ord(): 문자를 ASCII 코드로 변환
        return min(ord(c) - ord("A"), ord("Z") - ord(c) + 1)

    name_len = len(name)
    command_cnt = 0
    move_len = name_len - 1

    for current_idx in range(name_len):

        current_char = name[current_idx]
        command_cnt += command_num_to_find_char(current_char)

        # 스캔할 구간 [index_1 ~ index_0] 정하기
        index_0 = current_idx
        index_1 = index_0 + 1

        # index_0 오른쪽에 처음으로 'A'가 아닌 문자가 나오는 index_1 구하기
        while index_1 < name_len and name[index_1] == "A":
            index_1 += 1

        # move_len 업데이트
        dist = min(index_0, name_len - index_1)
        move_len = min(move_len, index_0 + (name_len - index_1) + dist)

    command_cnt += move_len

    return command_cnt
