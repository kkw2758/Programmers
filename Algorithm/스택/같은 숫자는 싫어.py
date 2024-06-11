def solution(arr):
  answer = [-1]
  for i in range(len(arr)):
    if arr[i] != answer[-1]:
      answer.append(arr[i])
  return answer[1:]


print(solution([1, 1, 3, 3, 0, 1, 1]))
