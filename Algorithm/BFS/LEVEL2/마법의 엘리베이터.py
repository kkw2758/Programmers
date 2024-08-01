def solution(storey):
  answer = []

  def dfs(storey, cnt):
    one = storey % 10
    up, down = 10 - one, one

    if storey == 0:
      answer.append(cnt)
      return

    if up < down:
      dfs(storey // 10 + 1, cnt + up)
    elif up > down:
      dfs(storey // 10, cnt + down)
    else:
      dfs(storey // 10 + 1, cnt + up)
      dfs(storey // 10, cnt + down)

  dfs(storey, 0)
  return min(answer)


print(solution(16))
