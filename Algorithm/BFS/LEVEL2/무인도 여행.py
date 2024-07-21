from collections import deque


def solution(maps):
  answer = []
  h = len(maps)
  w = len(maps[0])
  visited = [[False for _ in range(w)] for _ in range(h)]
  dx = [-1, 1, 0, 0]
  dy = [0, 0, -1, 1]

  def bfs(start_x, start_y):
    result = 0
    result += int(maps[start_x][start_y])
    visited[start_x][start_y] = True

    q = deque()
    q.append([start_x, start_y])
    while q:
      x, y = q.popleft()
      for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < h and 0 <= ny < w:
          if not visited[nx][ny] and maps[nx][ny].isdigit():
            visited[nx][ny] = True
            result += int(maps[nx][ny])
            q.append([nx, ny])
    return result

  for i in range(h):
    for j in range(w):
      if maps[i][j] != 'X' and not visited[i][j]:
        answer.append(bfs(i, j))
  if answer:
    answer.sort()
  else:
    answer = [-1]
  return answer


print(solution(["X591X", "X1X5X", "X231X", "1XXX1"]))
print(solution(["XXX", "XXX", "XXX"]))
