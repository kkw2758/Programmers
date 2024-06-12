# 나의 풀이
def solution(progresses, speeds):
    answer = []
    q = []

    for progress in progresses:
        q.append(progress)

    while q:
        count = 0
        for i in range(len(q)):
            q[i] += speeds[i]

        for _ in range(len(q)):
            if q[0] >= 100:
                count += 1
                q.pop(0)
                speeds.pop(0)
            else:
                break

        if count:
            answer.append(count)

    return answer


# 다른 풀이
def solution(progresses, speeds):
    answer = []
    days = 0
    # 현재 배포할 수 있는 기능 수
    cnt = 0
    while len(progresses) > 0:
        if (progresses[0] + days * speeds[0] >= 100):
            progresses.pop(0)
            speeds.pop(0)
            cnt += 1
        else:
            if cnt > 0:
                answer.append(cnt)
            else:
                days += 1

    answer.append(cnt)
    return answer
