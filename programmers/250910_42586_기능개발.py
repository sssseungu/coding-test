"""
Date: 25.09.10
기능개발(stack/queue)
URL
https://school.programmers.co.kr/learn/courses/30/lessons/42586
"""

from math import ceil


def solution(progresses, speeds):
    deployment_cnts = []

    # 각 기능 개발까지 걸리는 일수
    days_to_complete = [ceil((100 - progress) / speed) for progress, speed in zip(progresses, speeds)]
    total_tasks = len(progresses)

    task_idx = 0
    while task_idx < total_tasks:

        current_day = days_to_complete[task_idx]  # 기준 배포일
        release_cnt = 1  # 현재 배포시 포함될 기능 수

        other_task_idx = task_idx + 1
        while other_task_idx < total_tasks and days_to_complete[other_task_idx] <= current_day:
            release_cnt += 1
            other_task_idx += 1

        deployment_cnts.append(release_cnt)
        task_idx = other_task_idx

    return deployment_cnts
