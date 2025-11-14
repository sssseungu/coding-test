"""
DATE: 2025.10.29
광고삽입
URL
https://school.programmers.co.kr/learn/courses/30/lessons/72414
"""


def time2sec(time):
    time_list = list(map(int, time.split(":")))
    hour2sec = time_list[0] * 3600
    min2sec = time_list[1] * 60
    sec = time_list[2]
    return hour2sec + min2sec + sec


def sec2time(sec):

    min_tmp, sec_out = divmod(sec, 60)
    hour_out, min_out = divmod(min_tmp, 60)

    return f"{hour_out:02d}:{min_out:02d}:{sec_out:02d}"


def solution(play_time, adv_time, logs):

    playtime_sec = time2sec(play_time)
    advtime_sec = time2sec(adv_time)

    if playtime_sec == advtime_sec:
        return "00:00:00"

    logs_list = []
    for log in logs:
        log_split = log.split("-")
        log_tmp = []
        for t in log_split:
            log_tmp.append(time2sec(t))
        logs_list.append(tuple(log_tmp))

    logs_list = sorted(logs_list)
    time_sum = [0] * len(logs_list)

    for i in range(len(logs_list)):

        adv_start = logs_list[i][0]
        adv_end = min(adv_start + advtime_sec, playtime_sec)

        for log_tuple in logs_list:
            log_start, log_end = log_tuple

            # 광고와 겹치지 않음
            if adv_end < log_start or adv_start > log_end:
                continue

            # 겹침 시간 구하기
            if adv_start >= log_start:
                if adv_end >= log_end:  # lg_st ad_st lg_end ad_end
                    overlap = log_end - adv_start
                else:  # lg_st ad_st ad_end lg_end
                    overlap = adv_end - adv_start
            else:
                if adv_end >= log_end:  # ad_st lg_st lg_end ad_end
                    overlap = log_end - log_start
                else:  # ad_st lg_st ad_end lg_end
                    overlap = adv_end - log_start

            time_sum[i] += overlap

    print(time_sum)
    return sec2time(logs_list[time_sum.index(max(time_sum))][0])
