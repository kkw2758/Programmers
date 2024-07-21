from collections import deque


def solution(x, y, n):
  global answer
  visited = set()

  def bfs(x):
    visited.add(x)
    q = deque()
    q.append([x, 0])

    while q:
      now, cnt = q.popleft()
      if now == y:
        return cnt
      for nx in [now * 2, now * 3, now + n]:
        if nx not in visited and nx <= y:
          visited.add(nx)
          q.append([nx, cnt + 1])

    return -1

  return bfs(x)


print(solution(10, 40, 5))
