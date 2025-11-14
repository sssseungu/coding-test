"""
Date: 25.09.11
N으로 표현(DP)
URL
https://school.programmers.co.kr/learn/courses/30/lessons/42895
"""


def solution(N, number):

    # N을 count 개 사용한 모든 연산 결과를 담은 집합 반환
    def get_all_results(count):

        if count == 1:
            return {N}

        results = set()
        results.add(int(str(N) * count))  # N을 count번 붙인 수 저장

        # (1, count-1)이 아니라
        # 중간 분할도 고려해야함.. [(2, count-2), (3, count-3), ..., (count//2, count//2)]
        for i in range(1, count // 2 + 1):

            # 중간 분할 (i, count-i) 각각에 대한 모든 계산 결과 조합
            prev_results_1 = get_all_results(i)
            prev_results_2 = get_all_results(count - i)

            for num1 in prev_results_1:
                for num2 in prev_results_2:
                    results.add(num1 + num2)
                    results.add(num1 * num2)

                    results.add(num1 - num2)
                    results.add(num2 - num1)

                    if num2 != 0:
                        results.add(num1 // num2)
                    if num1 != 0:
                        results.add(num2 // num1)

        return results

    for i in range(1, 9):
        if number in get_all_results(i):
            return i

    return -1
