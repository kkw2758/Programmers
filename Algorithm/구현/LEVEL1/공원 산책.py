def solution(park, routes):
  w = len(park[0])
  h = len(park)
  direction = {'N': 0, 'S': 1, 'W': 2, 'E': 3}
  dx = [-1, 1, 0, 0]
  dy = [0, 0, -1, 1]
  for i in range(h):
    for j in range(w):
      if park[i][j] == 'S':
        x, y = i, j
  for route in routes:
    op, n = route.split()
    n = int(n)

    for i in range(n):
      nx = x + dx[direction[op]] * (i + 1)
      ny = y + dy[direction[op]] * (i + 1)
      if not (0 <= nx < h and 0 <= ny < w) or park[nx][ny] == 'X':
        break
    else:
      x = nx
      y = ny
  return [x, y]
