def solution(t, p):
  answer = 0
  interval = len(p)
  pivot = int(p)

  for i in range(len(t) - interval + 1):
    if int(t[i:i + interval]) <= pivot:
      answer += 1

  return answer


print(solution("3141592", "271"))
