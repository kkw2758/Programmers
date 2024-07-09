# 참고 풀이
# 출처 : https://velog.io/@sugyeonghh/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-%EC%97%B0%EC%86%8D%EB%90%9C-%EB%B6%80%EB%B6%84-%EC%88%98%EC%97%B4%EC%9D%98-%ED%95%A9Python
def solution(sequence, k):
  l = r = 0
  answer = [0, len(sequence)]
  sum = sequence[0]

  while True:
    if sum < k:
      r += 1
      if r == len(sequence):
        break
      sum += sequence[r]
    else:
      if sum == k:
        if r - l < answer[1] - answer[0]:
          answer = [l, r]
      sum -= sequence[l]
      l += 1
  return answer


# https://butter-shower.tistory.com/226 를 참고한 투포인터 풀이
def solution(sequence, k):
  interval_sum = 0
  answer = [0, len(sequence)]
  end = 0

  for start in range(len(sequence)):
    while interval_sum < k and end < len(sequence):
      interval_sum += sequence[end]
      end += 1

    if interval_sum == k:
      if (end - start - 1) < answer[1] - answer[0]:
        answer = [start, end - 1]

    interval_sum -= sequence[start]
  return answer


print(solution([1, 1, 1, 2, 3, 4, 5], 5))
