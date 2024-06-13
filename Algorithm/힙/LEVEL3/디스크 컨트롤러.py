# 다른 사람 풀이
import heapq


def solution(jobs):
  answer = 0
  total_work_time = 0  # 작업의 요청부터 종료까지 걸린 시간의 합
  now_time = 0  # 현재 시각
  start = -1  # 최근 작업 시작 시간
  finish_cnt = 0
  heap = []

  while finish_cnt < len(jobs):
    for job in jobs:
      if start < job[0] <= now_time:
        # 소요 시간이 작은 친구들 먼저 사용하기 위해 현재 시작이 가능한 작업을 넣어준다.
        heapq.heappush(heap, [job[1], job[0]])

    if heap:
      current = heapq.heappop(heap)
      start = now_time
      now_time += current[0]
      finish_cnt += 1
      total_work_time += now_time - current[1]
    else:
      now_time += 1

  answer = total_work_time // len(jobs)

  return answer
