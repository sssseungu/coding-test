"""
Date: 25.09.15
가장 큰 증가하는 부분 수열(DP)
URL
https://www.acmicpc.net/problem/11055
"""

# test case 1
# sequence = [1, 100, 2, 50, 60, 3, 5, 6, 7, 8]
# n = len(sequence)

# test case 2
# sequence = [10, 13, 1, 3, 7, 6]
# n = len(sequence)

# test case 3
# sequence = [1, 100, 13, 50, 200, 300, 7, 6]
# n = len(sequence)

# test case 4
# sequence = [1, 1, 2, 3]
# n = len(sequence)

# test case 5
# sequence = [5, 1, 10]
# n = len(sequence)


def max_subsum(len_series, series):

    # max_incr_subsums_end_at[i]: 반드시 series[i]에서 끝나는 증가 부분수열들의 합 중 최댓값.

    # k < i인 k에 대해,
    # series[k] < series[i]를 만족하는 가장 큰 series[k]를 찾아
    # max_incr_subsums_end_at[k] + series[i]를 하면
    # max_incr_subsums_end_at[i]를 구할 수 있음.

    max_incr_subsums_end_at = series[:]
    for i in range(1, len_series):
        for k in range(i):  # i보다 작은 k에 대해 순회.
            if series[k] < series[i]:
                # max_incr_subsums_end_at[i] 업데이트.
                max_incr_subsums_end_at[i] = max(max_incr_subsums_end_at[i], max_incr_subsums_end_at[k] + series[i])


# n = int(input())
# sequence = list(map(int, input().split()))
sequence = [1, 100, 13, 50, 200, 300, 7, 6]
n = len(sequence)
answer = max_subsum(n, sequence)


"""
문제를 잘 이해하지 못하고 푼 풀이.
"연속하는" 부분 증가수열의 합을 최대화하는 것으로 착각하였음.

def max_subsum(len_series, series):

    start_idx, end_idx = 0, 0
    subseries_list = []
    sub_sums = []
    cnt = -1
    while end_idx < len_series - 1:
        cur_value = series[end_idx]
        next_value = series[end_idx + 1]
        if cur_value < next_value:
            end_idx += 1
            continue
        else:
            # subseries_list.extend(series[start_idx:end_idx+1])
            subseries_list.append(series[start_idx : end_idx + 1])
            cnt += 1
            start_idx = end_idx + 1
            end_idx = start_idx
            # sub_sums.append(sum(subseries_list))
            sub_sums.append(sum(subseries_list[cnt]))
            # subseries_list = []

    # print(subseries_list)
    # print(sub_sums)
"""


"""
문제를 이해하고 다시 푼 첫 풀이. k 탐색을 내림차순으로 진행했음
test case 3: [1, 100, 13, 50, 200, 300, 7, 6] 을 통과하지 못해서 버림.

def max_subsum(len_series, series):

    max_incr_subsums_end_at = series[:]
    for i in range(1, len_series):
        for k in range(i-1, -1, -1):
            a_i = series[i]
            a_k = series[k]
            if series[i] <= series[k]:
                if k == 0:
                    max_incr_subsums_end_at[i] = series[i]
                continue
            else:
                max_incr_subsums_end_at[i] = max_incr_subsums_end_at[k] + series[i]
                break
"""
