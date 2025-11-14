"""
DATE: 2025.11.03
극장좌석
URL
https://www.acmicpc.net/problem/2302
"""

import sys

input = sys.stdin.readline

if __name__ == "__main__":

    # vip 입장권은 반드시 자기 좌석에만 앉아야 하고,
    # 일반 입장권은 자신의 바로 왼쪽 혹은 오른쪽 좌석으로 자리를 옮길 수 있음.

    # with open("./coding_test/baekjun/input.txt", "r") as f:
    #     num_seats = int(f.readline().strip())  # 전체 좌석의 개수
    #     num_vips = int(f.readline().strip())  # vip 좌석의 개수
    #     vip_seats = list(int(f.readline().strip()) for _ in range(num_vips))  # vip 좌석의 위치

    # 1. 전체 좌석을 vip 좌석을 기준으로 구간 나누기
    # 2. 각 구간마다 피보나치 수열을 이용해 각 구간의 경우의 수 계산하기
    # 3. 각 구간의 경우의 수를 모두 곱해서 총 경우의 수 계산

    num_seats = int(input().strip())  # 전체 좌석의 개수
    num_vips = int(input().strip())  # vip 좌석의 개수
    vip_seats = [int(input().strip()) for _ in range(num_vips)]  # vip 좌석의 위치

    # 좌석 구간 나누기
    seat_sections = []  # vip 좌석을 기준으로 나눈 구간의 좌석 수
    prev_vip = 0
    for vip in vip_seats:
        seat_sections.append(vip - prev_vip - 1)
        prev_vip = vip
    seat_sections.append(num_seats - prev_vip)

    # 구간의 길이가 n일 때, 제일 왼쪽에 있는 좌석[i]을 기준으로 경우를 나눠 보면
    # 1) 그 좌석에 앉는 경우 (i번째 사람이 그 좌석에 앉는 경우)
    #     그 다음 좌석에는 앉을 수 없으므로 나머지 n-1 개의 좌석의 경우의 수를 고려
    # 2) 그 좌석에 앉지 않는 경우
    #     다음 좌석번호[i+1]의 사람이 반드시 [i]에 앉아야 하므로
    #     나머지 n-2 개의 좌석의 경우의 수를 고려
    # 따라서, A[n] = A[n-1] + A[n-2]: 피보나치 수열

    # 피보나치 수열로 경우의 수 계산
    max_section_length = max(seat_sections)
    fibonacci = [0] * (max_section_length + 2)  # max_section_length가 0인 경우를 대비하여 +2
    fibonacci[0] = 1
    fibonacci[1] = 1
    for i in range(2, max_section_length + 2):
        fibonacci[i] = fibonacci[i - 1] + fibonacci[i - 2]

    total_ways = 1
    for section in seat_sections:
        total_ways *= fibonacci[section]
    print(total_ways)
