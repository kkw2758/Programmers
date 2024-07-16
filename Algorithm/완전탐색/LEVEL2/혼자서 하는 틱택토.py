def get_end_count(board, symbol):
  count = 0
  # 행 검사
  for row in range(3):
    if "".join(board[row]) == symbol:
      count += 1

  # 열 검사
  for col in range(3):
    temp_col = ""
    for row in range(3):
      temp_col += board[row][col]
    if temp_col == symbol:
      count += 1

  # 대각선 검사
  left_to_right = ""
  right_to_left = ""
  for i in range(3):
    left_to_right += board[i][i]
    right_to_left += board[i][2 - i]

  if left_to_right == symbol:
    count += 1

  if right_to_left == symbol:
    count += 1

  return count

def get_symbol_count(board, symbol):
  count = 0
  for i in range(3):
    for j in range(3):
      if board[i][j] == symbol:
        count += 1
  return count


def solution(board):
  O_end_count = get_end_count(board, "OOO")
  X_end_count = get_end_count(board, "XXX")
  end_count = O_end_count + X_end_count
  X_count = get_symbol_count(board, "X")
  O_count = get_symbol_count(board, "O")

  if not (O_count == X_count or O_count == X_count + 1):
    return 0

  # O 혹은 X만 승리조건을 만족해야 함.
  if O_end_count and X_end_count:
    return 0

  # O가 승리했다면 o_count == x_count + 1이어야 함.
  if O_end_count and O_count != X_count + 1:
    return 0

  # X가 승리했다면 o_count == x_count 여야 함.
  if X_end_count and O_count != X_count:
    return 0

  return 1
