"""
DATE: 2025.10.13
메뉴 리뉴얼
URL
https://school.programmers.co.kr/learn/courses/30/lessons/72411
"""

orders = ["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"]  # 손님들이 주문한 단품메뉴들
course = [2, 3, 4]  # 코스요리를 구성하는 단품메뉴들의 개수
# result: 만들 코스요리의 메뉴 구성을 문자열로 담은 배열

# 각 손님별로 주문했던 메뉴들에 대해,
# 각각 course_size(course 리스트의 원소)만큼 짝지어 만들 수 있는 모든 코스메뉴 조합을 계산한다.
# 그 모든 조합을 하나의 리스트로 모아
# 각각의 코스메뉴가 등장하는 빈도를 체크했을 때
# 2번 이상 등장한다면, 그 코스메뉴는 두 명 이상의 손님이 주문한 메뉴임을 뜻한다.
# 그 중 가장 많이 등장한 메뉴만으로 코스메뉴판을 구성한다.
# 가장 많이, 그리고 동일한 빈도로 등장한 코스메뉴는 모두 포함한다.


def get_combinations(array, num_select):
    """array에서 num_select개를 선택하는 모든 조합 반환 (순서 고려 x, 중복 불가)

    Args:
        array (list): 입력 배열
        num_select (int): 입력 배열 내 원소 중에 선택하는 대상의 수

    Returns:
        combinations (list): array에서 num_select개를 선택한 모든 조합을 담은 리스트
    """
    combinations = []

    # 0개를 선택 -> 빈 조합 반환
    if num_select == 0:
        return [[]]

    # 선택할 개수보다 배열의 크기가 작음  불가능
    if len(array) < num_select:
        return []

    for idx in range(len(array)):
        element = array[idx]
        rest = array[idx + 1 :]
        for combination in get_combinations(rest, num_select - 1):
            combinations.append([element] + combination)

    return combinations


def solution(orders, course):
    result = []

    for course_size in course:

        all_combinations = []

        for order in orders:
            sorted_order = sorted(order)
            if len(sorted_order) >= course_size:
                combos = get_combinations(sorted_order, course_size)
                all_combinations.extend(["".join(combo) for combo in combos])

        count_dict = {}
        for combo in all_combinations:
            count_dict[combo] = count_dict.get(combo, 0) + 1

        if count_dict:
            max_count = max(count_dict.values())

            if max_count >= 2:
                result += [combo for combo, count in count_dict.items() if count == max_count]

    return sorted(result)
