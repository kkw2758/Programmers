from collections import deque


def solution(rectangle, characterX, characterY, itemX, itemY):
  answer = 0
  graph = [[-1 for _ in range(102)] for _ in range(102)]
  visited = [[1 for _ in range(102)] for _ in range(102)]
  dx = [-1, 1, 0, 0]
  dy = [0, 0, -1, 1]
  q = deque()

  for r in rectangle:
    x1, y1, x2, y2 = map(lambda x: x * 2, r)
    for i in range(x1, x2 + 1):
      for j in range(y1, y2 + 1):
        if x1 < i < x2 and y1 < j < y2:
          graph[i][j] = 0
        elif graph[i][j] != 0:
          graph[i][j] = 1

  cx, cy, ix, iy = 2 * characterX, 2 * characterY, 2 * itemX, 2 * itemY

  q.append((cx, cy))

  while q:
    x, y = q.popleft()
    if x == ix and y == iy:
      answer = visited[x][y] // 2
      break

    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      if graph[nx][ny] == 1 and visited[nx][ny] == 1:
        visited[nx][ny] = visited[x][y] + 1
        q.append((nx, ny))
  return answer


# [[1,1,7,4],[3,2,5,5],[4,3,6,9],[2,6,8,8]]	1	3	7	8	17
print(
    solution([[1, 1, 7, 4], [3, 2, 5, 5], [4, 3, 6, 9], [2, 6, 8, 8]], 1, 3, 7,
             8))
