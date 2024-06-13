# 나의 풀이 1
import heapq


def solution(scoville, K):
  heap = []
  for i in range(len(scoville)):
    heapq.heappush(heap, scoville[i])

  answer = 0
  while len(heap) >= 2:
    if all(member >= K for member in heap):
      return answer
    first = heapq.heappop(heap)
    second = heapq.heappop(heap)
    mix_scoville = first + second * 2
    heapq.heappush(heap, mix_scoville)
    answer += 1

  if heapq.heappop(heap) < K:
    answer = -1

  return answer


print(solution([1, 2, 3, 9, 10, 12], 7))

# 나의 풀이 2
import heapq


def solution(scoville, K):
  heap = []
  for i in range(len(scoville)):
    heapq.heappush(heap, scoville[i])

  answer = 0
  while any(member < K for member in heap):
    if len(heap) < 2:
      if not (heapq.heappop(heap) >= K):
        answer = -1
      break
    first = heapq.heappop(heap)
    second = heapq.heappop(heap)
    mix_scoville = first + second * 2
    heapq.heappush(heap, mix_scoville)
    answer += 1

  return answer


print(solution([1, 2, 3, 9, 10, 12], 7))
