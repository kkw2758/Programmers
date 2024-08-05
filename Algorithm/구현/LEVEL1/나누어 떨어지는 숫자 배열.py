def solution(arr, divisor):
  answer = []
  for member in arr:
    if member % divisor == 0:
      answer.append(member)

  if not answer:
    return [-1]

  answer.sort()

  return answer
