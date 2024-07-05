# 나의 풀이
# 실행 결과는 올바르게 나오지만 시간초과 발생
import sys
from collections import deque

input = sys.stdin.readline


def solution(land):
  answer = 0

  n = len(land)
  m = len(land[0])

  def dfs(start_x, start_y):
    q = deque()
    q.append([start_x, start_y])

    visited[start_x][start_y] = True

    count = 1
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    while q:
      x, y = q.popleft()
      for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and land[nx][
            ny] == 1:
          visited[nx][ny] = True
          count += 1
          q.append([nx, ny])

    return count

  for col in range(m):
    visited = [[False] * m for _ in range(n)]
    temp = 0
    for row in range(n):
      if land[row][col] == 1 and not visited[row][col]:
        temp += dfs(row, col)
    answer = max(temp, answer)

  return answer


print(
    solution([[0, 0, 0, 1, 1, 1, 0, 0], [0, 0, 0, 0, 1, 1, 0, 0],
              [1, 1, 0, 0, 0, 1, 1, 0], [1, 1, 1, 0, 0, 0, 0, 0],
              [1, 1, 1, 0, 0, 0, 1, 1]]))

print(
    solution([[1, 0, 1, 0, 1, 1], [1, 0, 1, 0, 0, 0], [1, 0, 1, 0, 0, 1],
              [1, 0, 0, 1, 0, 0], [1, 0, 0, 1, 0, 1], [1, 0, 0, 0, 0, 0],
              [1, 1, 1, 1, 1, 1]]))

# 참고 풀이 1
from collections import deque

def solution(land):
  answer = 0
  n = len(land)
  m = len(land[0])
  dx = [-1, 1, 0, 0]
  dy = [0, 0, -1, 1]
  result = [0 for m in range(m)]
  visited = [[0] * m for _ in range(n)]

  def bfs(a, b):
    count = 0
    visited[a][b] = 1
    q = deque()
    q.append((a, b))
    min_y, max_y = b, b
    while q:
      x, y = q.popleft()
      min_y = min(min_y, y)
      max_y = max(max_y, y)
      count += 1
      for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or ny < 0 or nx >= n or ny >= m:
          continue
        if visited[nx][ny] == 0 and land[nx][ny] == 1:
          visited[nx][ny] = 1
          q.append((nx, ny))
    for i in range(min_y, max_y + 1):
      result[i] += count

  for i in range(n):
    for j in range(m):
      if visited[i][j] == 0 and land[i][j] == 1:
        bfs(i, j)

  answer = max(result)

  return answer


# 참고 풀이 2

import sys
from collections import deque, defaultdict

input = sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(i, j, n, m, oil, land):
  amount = 1
  land[i][j] = oil
  q = deque()
  q.append((i, j))

  while q:
    x, y = q.popleft()
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      if 0 <= nx < n and 0 <= ny < m and land[nx][ny] == 1:
        amount += 1
        land[nx][ny] = oil
        q.append((nx, ny))

  return amount


def solution(land):
  answer, oil = 0, 2
  n, m = len(land), len(land[0])
  amount_of = defaultdict(int)

  for i in range(n):
    for j in range(m):
      if land[i][j] == 1:
        amount_of[oil] = bfs(i, j, n, m, oil, land)
        oil += 1

  for j in range(m):
    oil_types = set([land[i][j] for i in range(n)])
    amount = 0
    for oil in oil_types:
      amount += amount_of[oil]
    answer = max(amount, answer)

  return answer


print(
    solution([[0, 0, 0, 1, 1, 1, 0, 0], [0, 0, 0, 0, 1, 1, 0, 0],
              [1, 1, 0, 0, 0, 1, 1, 0], [1, 1, 1, 0, 0, 0, 0, 0],
              [1, 1, 1, 0, 0, 0, 1, 1]]))

print(
    solution([[1, 0, 1, 0, 1, 1], [1, 0, 1, 0, 0, 0], [1, 0, 1, 0, 0, 1],
              [1, 0, 0, 1, 0, 0], [1, 0, 0, 1, 0, 1], [1, 0, 0, 0, 0, 0],
              [1, 1, 1, 1, 1, 1]]))

# 참고 풀이 3
from collections import deque, defaultdict


def solution(land):
  answer = 0
  n = len(land)
  m = len(land[0])
  oil = 2
  amount_of = defaultdict(int)

  dx = [-1, 1, 0, 0]
  dy = [0, 0, -1, 1]

  def bfs(start_x, start_y, oil):
    q = deque()
    q.append([start_x, start_y])
    count = 1
    land[start_x][start_y] = oil

    while q:
      x, y = q.popleft()
      for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < m and land[nx][ny] == 1:
          land[nx][ny] = oil
          q.append([nx, ny])
          count += 1

    return count

  for i in range(n):
    for j in range(m):
      if land[i][j] == 1:
        amount_of[oil] = bfs(i, j, oil)
        oil += 1

  for col in range(m):
    oil_types = set([land[row][col] for row in range(n)])
    amount = 0
    for oil in oil_types:
      amount += amount_of[oil]

    answer = max(answer, amount)

  return answer


print(
    solution([[0, 0, 0, 1, 1, 1, 0, 0], [0, 0, 0, 0, 1, 1, 0, 0],
              [1, 1, 0, 0, 0, 1, 1, 0], [1, 1, 1, 0, 0, 0, 0, 0],
              [1, 1, 1, 0, 0, 0, 1, 1]]))

print(
    solution([[1, 0, 1, 0, 1, 1], [1, 0, 1, 0, 0, 0], [1, 0, 1, 0, 0, 1],
              [1, 0, 0, 1, 0, 0], [1, 0, 0, 1, 0, 1], [1, 0, 0, 0, 0, 0],
              [1, 1, 1, 1, 1, 1]]))
