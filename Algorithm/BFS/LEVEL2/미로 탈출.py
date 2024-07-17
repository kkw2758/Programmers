from collections import deque


def solution(maps):
  start_x, start_y = 0, 0
  lever_x, lever_y = 0, 0
  exit_x, exit_y = 0, 0
  for i in range(len(maps)):
    for j in range(len(maps[0])):
      if maps[i][j] == 'L':
        lever_x, lever_y = i, j
      if maps[i][j] == 'E':
        exit_x, exit_y = i, j
      if maps[i][j] == 'S':
        start_x, start_y = i, j

  def bfs(start_x, start_y, end_x, end_y):
    q = deque()
    q.append([start_x, start_y])

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    visited = [[-1 for _ in range(len(maps[0]))] for _ in range(len(maps))]

    visited[start_x][start_y] = 0

    while q:
      x, y = q.popleft()
      if (x, y) == (end_x, end_y):
        return visited[x][y]
      for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < len(maps) and 0 <= ny < len(maps[0]):
          if maps[nx][ny] != 'X' and visited[nx][ny] == -1:
            visited[nx][ny] = visited[x][y] + 1
            q.append([nx, ny])
    return -1

  start_to_lever = bfs(start_x, start_y, lever_x, lever_y)
  lever_to_exit = bfs(lever_x, lever_y, exit_x, exit_y)
  if start_to_lever == -1 or lever_to_exit == -1:
    return -1
  return start_to_lever + lever_to_exit


print(solution(["SOOOL", "XXXXO", "OOOOO", "OXXXX", "OOOOE"]))
