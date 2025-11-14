"""

URL
https://school.programmers.co.kr/learn/courses/30/lessons/60058?language=python3
"""

# 1. 입력이 빈 문자열인 경우, 빈 문자열을 반환합니다.
# 2. 문자열 w를 두 "균형잡힌 괄호 문자열" u, v로 분리합니다. 단, u는 "균형잡힌 괄호 문자열"로 더 이상 분리할 수 없어야 하며, v는 빈 문자열이 될 수 있습니다.
# 3. 문자열 u가 "올바른 괄호 문자열" 이라면 문자열 v에 대해 1단계부터 다시 수행합니다.
#   3-1. 수행한 결과 문자열을 u에 이어 붙인 후 반환합니다.
# 4. 문자열 u가 "올바른 괄호 문자열"이 아니라면 아래 과정을 수행합니다.
#   4-1. 빈 문자열에 첫 번째 문자로 '('를 붙입니다.
#   4-2. 문자열 v에 대해 1단계부터 재귀적으로 수행한 결과 문자열을 이어 붙입니다.
#   4-3. ')'를 다시 붙입니다.
#   4-4. u의 첫 번째와 마지막 문자를 제거하고, 나머지 문자열의 괄호 방향을 뒤집어서 뒤에 붙입니다.
#   4-5. 생성된 문자열을 반환합니다.

# "균형잡힌 괄호 문자열" p가 매개변수로 주어질 때,
# 주어진 알고리즘을 수행해 "올바른 괄호 문자열"로 변환한 결과를 return 하도록
# solution 함수를 완성해 주세요.


# "("와 ")" 개수 같으면 "균형잡힌"
# 균형잡혔고 짝까지 맞으면 "올바른"


def separate_uv(s):

    count = 0
    for i, char in enumerate(s):
        if char == "(":
            count += 1
        else:
            count -= 1

        if count == 0:
            u = s[: i + 1]
            v = s[i + 1 :]
            return u, v

    return s, ""


def is_correct(s):
    count = 0
    for char in s:
        if char == "(":
            count += 1
        else:
            count -= 1

        if count < 0:
            return False

    return count == 0


def reverse_parenthesis(s):
    w = ""
    for char in s:
        if char == "(":
            w += ")"
        else:
            w += "("
    return w


def solution(p):

    if not p:
        return ""

    if is_correct(p):
        return p

    u, v = separate_uv(p)

    if is_correct(u):
        return u + solution(v)

    else:
        tmp = "("
        tmp += solution(v)
        tmp += ")"
        tmp += reverse_parenthesis(u[1:-1])
        return tmp


print(solution(")("))
