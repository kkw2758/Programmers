def solution(targets):
  targets.sort(key=lambda x: x[1], reverse=True)
  start = 0
  end = 0
  pivot = 0
  answer = 0

  while targets:
    start, end = targets.pop()
    if not start < pivot < end:
      pivot = end - 0.5
      answer += 1
  return answer


print(solution([[4, 5], [4, 8], [10, 14], [11, 13], [5, 12], [3, 7], [1, 4]]))
