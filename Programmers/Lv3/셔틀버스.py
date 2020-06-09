# Solve
'''
    timetable 오름차순 정렬
    timetable 요소 "00:00"이거나 "24:00" 인 경우 삭제, 각각의 요소 datetime 객체로 변환
    for i in 셔틀운행횟수:
        출발시간 = 9:00 + i * m
        탑승가능_list = [timetable 중 출발 시간 이하인 값]

        if 마지막 운행:
            if len(탑승가능_list) >= m:
                return m개의 탑승가능_list 중 가장 늦은 탑승 시간 - 1분
            else:
                break
        else:
            if len(탑승가능_list) > 0:
                if len(탑승가능_list) > m:
                    timetable 앞에서 m개 자르기
                else:
                    timetable 앞에서 len(탑승가능_list)개 자르기

    return 출발시간                
'''
# 풀이 1 - 정확성 100
import datetime
def solution(n, t, m, timetable):
    initial_t = datetime.datetime.strptime("09:00", '%H:%M')
    leave_t = None
    timetable.sort()
    timetable = [datetime.datetime.strptime(i, '%H:%M') for i in timetable if i != "00:00" and i != "24:00"]

    for i in range(n):
        leave_t = initial_t + i* datetime.timedelta(minutes = t)
        candidate = list(filter(lambda x: x<= leave_t, timetable))
    
        if i == n-1:
            if len(candidate) >= m:
                return (max(candidate[:m]) - datetime.timedelta(minutes = 1)).strftime("%H:%M")
            else:
                break
        else:
            if len(candidate) > 0:
                if len(candidate) > m:
                    timetable=timetable[m:]
                else:
                    timetable=timetable[len(candidate):]
    return leave_t.strftime("%H:%M")

# 풀이2 정확성 95.8 (테스트 22 런타임 에러)
import datetime
def solution(n, t, m, timetable):
    initial_t = datetime.datetime.strptime("09:00", '%H:%M')
    leave_t = None
    timetable.sort()
    timetable = [datetime.datetime.strptime(i, '%H:%M') for i in timetable]
    for i in range(n):
        leave_t = initial_t + i* datetime.timedelta(minutes = t)
        count = 0
        if i == n-1:
            idx = 0
            candidate = list(filter(lambda x: x<= leave_t, timetable))
            if not candidate:
                break
            while count < m:
                time = candidate[idx]
                time_count = candidate.count(time)
                if count + time_count >= m:
                    return (time - datetime.timedelta(minutes = 1)).strftime("%H:%M")
                else:
                    idx += time_count
                    count += time_count
                
                if idx >= len(candidate):
                    break
        else:
            if min(timetable) <= leave_t:
                for v in timetable:
                    if v > leave_t or count >= m:
                        break
                    else:
                        count += 1
                timetable = timetable[count:]
    return leave_t.strftime("%H:%M")

# 풀이 3 정확성 95.8 (테스트 22 런타임 에러)
import datetime
def solution(n, t, m, timetable):
    initial_t = datetime.datetime.strptime("09:00", '%H:%M')
    leave_t = None
    timetable.sort()
    timetable = [datetime.datetime.strptime(i, '%H:%M') for i in timetable]
    for i in range(n):
        leave_t = initial_t + i* datetime.timedelta(minutes = t)
        candidate = list(filter(lambda x: x<= leave_t, timetable))
        count = 0
        if i == n-1:
            if not candidate:
                break
            if len(candidate) >= m:
                return (max(candidate[:m]) - datetime.timedelta(minutes = 1)).strftime("%H:%M")
            else:
                break
        else:
            if len(candidate) > 0:
                if len(candidate) > m:
                    timetable=timetable[m:]
                else:
                    timetable=timetable[len(candidate):]
    return leave_t.strftime("%H:%M")