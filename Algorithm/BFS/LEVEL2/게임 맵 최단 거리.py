from collections import deque


def solution(maps):
  visited = [[-1] * len(maps[0]) for _ in range(len(maps))]

  def bfs(start_x, start_y):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    visited[start_x][start_y] = 1
    q = deque()
    q.append([start_x, start_y])

    while q:
      x, y = q.popleft()
      for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < len(maps) and 0 <= ny < len(maps[0]):
          if visited[nx][ny] == -1 and maps[nx][ny] == 1:
            visited[nx][ny] = visited[x][y] + 1
            q.append([nx, ny])

  bfs(0, 0)
  return visited[-1][-1]


print(
    solution([[1, 0, 1, 1, 1], [1, 0, 1, 0, 1], [1, 0, 1, 1, 1],
              [1, 1, 1, 0, 1], [0, 0, 0, 0, 1]]))
print(
    solution([[1, 0, 1, 1, 1], [1, 0, 1, 0, 1], [1, 0, 1, 1, 1],
              [1, 1, 1, 0, 0], [0, 0, 0, 0, 1]]))
