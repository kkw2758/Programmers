import heapq


def solution(k, score):
  answer = []
  q = []
  for s in score:
    if len(q) < k:
      heapq.heappush(q, s)
    else:
      min_value = heapq.heappop(q)
      if min_value < s:
        heapq.heappush(q, s)
      else:
        heapq.heappush(q, min_value)

    answer.append(min(q))

  return answer
