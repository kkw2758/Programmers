from collections import deque


def solution(board):
  answer = -1
  board = [list(row) for row in board]
  dx = [-1, 1, 0, 0]
  dy = [0, 0, -1, 1]
  start_x, start_y, end_x, end_y = 0, 0, 0, 0
  h = len(board)
  w = len(board[0])
  for i in range(h):
    for j in range(w):
      if board[i][j] == 'R':
        start_x, start_y = i, j
      if board[i][j] == 'G':
        end_x, end_y = i, j

  def get_move_cnt(x, y, direction):
    move_cnt = 0
    while True:
      x = x + dx[direction]
      y = y + dy[direction]
      # 범위 밖이거나 장애물을 만나면
      if not (0 <= x < h and 0 <= y < w) or board[x][y] == 'D':
        return move_cnt
      move_cnt += 1

  q = deque()
  q.append([start_x, start_y])
  board[start_x][start_y] = 0

  while q:
    x, y = q.popleft()
    for i in range(4):
      move_cnt = get_move_cnt(x, y, i)
      if move_cnt != 0:
        nx = x + dx[i] * move_cnt
        ny = y + dy[i] * move_cnt
        if str(board[nx][ny]).isdigit():
          continue
        board[nx][ny] = board[x][y] + 1
        q.append([nx, ny])

  if board[end_x][end_y] != "G":
    answer = board[end_x][end_y]
  return answer


print(solution(["...D..R", ".D.G...", "....D.D", "D....D.", "..D...."]))
print(solution([".D.R", "....", ".G..", "...D"]))
