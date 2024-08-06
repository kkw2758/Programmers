def solution(k, m, score):
  answer = 0
  score.sort()
  n = len(score)
  for i in range(n // m):
    tmp = []
    for j in range(m):
      tmp.append(score.pop())
    answer += min(tmp) * m
  return answer


print(solution(3, 4, [1,2,3,1,2,3,1]))
print(solution(4,3, [4,1,2,2,4,4,4,4,1,2,4,2]))