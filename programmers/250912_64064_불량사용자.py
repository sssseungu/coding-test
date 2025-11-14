"""
Date: 25.09.12
불량 사용자(2019 Kakao Winter Internship)
URL
https://school.programmers.co.kr/learn/courses/30/lessons/64064
"""

import itertools


def solution(user_id, banned_id):

    # {(0,"fr*d*"): [], (1,"*rodo"):[], (2,"******"):[], (3,"******"):[]}
    ban_candidates = {(idx, ban_pattern): [] for idx, ban_pattern in enumerate(banned_id)}

    # 각 ban_pattern에 맞는 user_id 리스트를 ban_candidates에 담기
    for idx, ban_pattern in enumerate(banned_id):
        for user in user_id:
            if len(user) != len(ban_pattern):  # 길이 다른 경우는 고려하지 않음.
                continue
            elif ban_pattern == "*" * len(user):  # ban_pattern: '******'꼴
                ban_candidates[(idx, ban_pattern)].append(user)
            else:  # ban_pattern: '******'꼴 외
                matched_char_count = 0  # ban 패턴에 매칭되는 문자 수
                for char_idx in range(len(user)):
                    if ban_pattern[char_idx] == user[char_idx] or ban_pattern[char_idx] == "*":
                        matched_char_count += 1

                if matched_char_count == len(user):  # 매칭 문자 수 == 아이디 길이
                    ban_candidates[(idx, ban_pattern)].append(user)

    # ban_candidate에 있는 user_id의 조합 구하기.
    combinations = {
        tuple(sorted(combo)) for combo in itertools.product(*ban_candidates.values()) if len(set(combo)) == len(combo)
    }

    return len(combinations)


# if __name__ == "__main__":
user_id = ["frodo", "fradi", "crodo", "abc123", "frodoc"]
banned_id = ["fr*d*", "*rodo", "******", "******"]
assert solution(user_id, banned_id) == 3
