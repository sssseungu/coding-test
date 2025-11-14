"""
Date: 25.09.08
프로세스(stack/queue)
URL
https://school.programmers.co.kr/learn/courses/30/lessons/42587
"""

from collections import deque


def solution(priorities, location):

    queue = deque(enumerate(priorities))  # enumerate로 우선순위와 위치정보 묶기

    num_of_processed = 0  # 현재까지 실행된 process 수
    while queue:

        max_priority = max(priority for _, priority in queue)
        process, priority = queue.popleft()  # process 꺼내기

        if priority < max_priority:
            queue.append((process, priority))  # process 실행 안하고 다시 넣기

        else:
            num_of_processed += 1
            if process == location:  # 실행한 process가 location에 해당하면 return
                return num_of_processed
