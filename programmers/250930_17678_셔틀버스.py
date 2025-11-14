"""
Date: 25.09.30
셔틀버스
URL
https://school.programmers.co.kr/learn/courses/30/lessons/17678
"""

"""
입출력 예제
n 	t 	m 	timetable 	answer
1 	1 	5 	["08:00", "08:01", "08:02", "08:03"] 	"09:00"
2 	10 	2 	["09:10", "09:09", "08:00"] 	"09:09"
2 	1 	2 	["09:00", "09:00", "09:00", "09:00"] 	"08:59"
1 	1 	5 	["00:01", "00:01", "00:01", "00:01", "00:01"] 	"00:00"
1 	1 	1 	["23:59"] 	"09:00"
10 	60 	45 	["23:59","23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59"] 	"18:00"
"""
# ---  my code --- #


def timestr2int(str_time):
    """시간 문자열을 분 단위 정수로 변환"""
    hour, minute = map(int, str_time.split(":"))
    return hour * 60 + minute


def timeint2str(int_time):
    """분 단위 정수를 시간 문자열로 변환"""
    hour = int_time // 60
    minute = int_time % 60
    return f"{hour:02d}:{minute:02d}"


def solution(n, t, m, timetable):

    crew_times = sorted([timestr2int(time) for time in timetable])
    shuttle_times = [540 + i * t for i in range(n)]  # 540 = "09:00"

    crew_idx = 0

    for shuttle_time in shuttle_times:
        boarding = []

        while (
            crew_idx < len(crew_times)
            and len(boarding) < m
            and crew_times[crew_idx] <= shuttle_time
        ):
            boarding.append(crew_times[crew_idx])
            crew_idx += 1

        last_boarding = boarding

    last_shuttle_time = shuttle_times[-1]

    if len(last_boarding) < m:
        con_time = last_shuttle_time
    else:
        con_time = last_boarding[-1] - 1

    return timeint2str(con_time)


n = 2
t = 10
m = 2
timetable = ["09:10", "09:09", "08:00"]
print(solution(n, t, m, timetable))
