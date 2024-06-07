# [1, 1, 1, 1, 1]
# 3

answer = 0


def solution(numbers, target):

  def dfs(value, idx):

    global answer
    # 이미 마지막 인덱스 까지 오면 종료
    if idx == len(numbers):
      if value == target:
        answer += 1
      return
    dfs(value + numbers[idx], idx + 1)
    dfs(value - numbers[idx], idx + 1)

  dfs(0, 0)
  return answer


print(solution([1, 1, 1, 1, 1], 3))
print(solution([4, 1, 2, 1], 4))
