example = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]


def rotate_90(array):
  n = len(array)
  m = len(array[0])
  result = [[0 for _ in range(n)] for _ in range(m)]
  for i in range(n):
    for j in range(m):
      result[j][n - 1 - i] = array[i][j]

  return result


def slice_list(target_list, x1, y1, x2, y2):
  result = []
  for x in range(x1, x2 + 1):
    result.append(target_list[x][y1:y2 + 1])

  return result


def is_match(empty_space, puzzle):
  n = len(empty_space)
  m = len(empty_space[0])
  if n != len(puzzle) or m != len(puzzle[0]):
    return False
  for i in range(n):
    for j in range(m):
      if empty_space[i][j] + puzzle[i][j] != 1:
        return False
  return True


# print("result")
# print(
#     is_match([[0, 0, 1], [1, 0, 1], [1, 0, 0]],
#              [[1, 1, 0], [0, 1, 0], [0, 1, 1]]))


def solution(game_board, table):
  answer = 0
  n = len(game_board)
  gmae_board_visited = [[False for _ in range(n)] for _ in range(n)]
  table_visited = [[False for _ in range(n)] for _ in range(n)]
  dx = [-1, 1, 0, 0]
  dy = [0, 0, -1, 1]

  def game_board_dfs(x, y):
    stack = []
    stack.append((x, y))
    gmae_board_visited[x][y] = True
    min_x = x
    max_x = x
    min_y = y
    max_y = y

    while stack:
      x, y = stack.pop()

      for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < n and not gmae_board_visited[nx][
            ny] and game_board[nx][ny] == 0:

          min_x, max_x = min(min_x, nx), max(max_x, nx)
          min_y, max_y = min(min_y, ny), max(max_y, ny)

          gmae_board_visited[nx][ny] = True
          stack.append((nx, ny))
    return min_x, min_y, max_x, max_y

  def table_dfs(x, y):
    stack = []
    stack.append((x, y))
    table_visited[x][y] = True
    min_x = x
    max_x = x
    min_y = y
    max_y = y

    while stack:
      x, y = stack.pop()

      for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < n and not table_visited[nx][ny] and table[
            nx][ny] == 1:

          min_x, max_x = min(min_x, nx), max(max_x, nx)
          min_y, max_y = min(min_y, ny), max(max_y, ny)

          table_visited[nx][ny] = True
          stack.append((nx, ny))
    return min_x, min_y, max_x, max_y

  empty_spaces = []

  for i in range(n):
    for j in range(n):
      if not gmae_board_visited[i][j] and game_board[i][j] == 0:
        x1, y1, x2, y2 = game_board_dfs(i, j)
        empty_spaces.append(slice_list(game_board, x1, y1, x2, y2))

  # for empty_space in empty_spaces:
  #   print("empty_space", empty_space)
  #   for _ in empty_space:
  #     print(_)
  #   print()
  # print("-" * 50)

  puzzles = []

  for i in range(n):
    for j in range(n):
      if not table_visited[i][j] and table[i][j] == 1:
        x1, y1, x2, y2 = table_dfs(i, j)
        puzzles.append(slice_list(table, x1, y1, x2, y2))

  used_puzzles = set()
  used_empty_spaces = set()
  for i in range(len(empty_spaces)):
    for j in range(len(puzzles)):
      if j not in used_puzzles and i not in used_empty_spaces:
        for _ in range(4):
          puzzles[j] = rotate_90(puzzles[j])
          if is_match(empty_spaces[i], puzzles[j]):
            used_puzzles.add(j)
            used_empty_spaces.add(i)
            break

  for idx in list(used_puzzles):
    for i in range(len(puzzles[idx])):
      for j in range(len(puzzles[idx][0])):
        if puzzles[idx][i][j] == 1:
          answer += 1

  # for puzzle in puzzles:
  #   print("puzzle", puzzle)
  #   for _ in puzzle:
  #     print(_)
  #   print()

  # print()
  # print(used_puzzles)
  return answer


print(
    solution([[1, 1, 0, 0, 1, 0], [0, 0, 1, 0, 1, 0], [0, 1, 1, 0, 0, 1],
              [1, 1, 0, 1, 1, 1], [1, 0, 0, 0, 1, 0], [0, 1, 1, 1, 0, 0]],
             [[1, 0, 0, 1, 1, 0], [1, 0, 1, 0, 1, 0], [0, 1, 1, 0, 1, 1],
              [0, 0, 1, 0, 0, 0], [1, 1, 0, 1, 1, 0], [0, 1, 0, 0, 0, 0]]))

#------------------------------------------------------

from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


# board와 puzzle의 각각 빈공간과 블럭을 찾는 함수 BFS
def find_block(board, f):
  empty_board_list = []
  visited = [[False] * len(board[0]) for _ in range(len(board))]

  for i in range(len(board)):
    for j in range(len(board[i])):
      if not visited[i][j] and board[i][j] == f:
        queue = deque([(i, j)])
        board[i][j] = f ^ 1
        visited[i][j] = True
        lst = [(i, j)]

        while queue:
          x, y = queue.popleft()
          for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if nx < 0 or nx > len(board) - 1 or ny < 0 or ny > len(board) - 1:
              continue
            elif board[nx][ny] == f:
              queue.append((nx, ny))
              board[nx][ny] = f ^ 1
              visited[nx][ny] = True
              lst.append((nx, ny))
        empty_board_list.append(lst)
  return empty_board_list


def make_table(block):
  x, y = zip(*block)
  c, r = max(x) - min(x) + 1, max(y) - min(y) + 1
  table = [[0] * r for _ in range(c)]

  for i, j in block:
    i, j = i - min(x), j - min(y)
    table[i][j] = 1
  return table


def rotate(puzzle):
  rotate = [[0] * len(puzzle) for _ in range(len(puzzle[0]))]
  count = 0
  for i in range(len(puzzle)):
    for j in range(len(puzzle[i])):
      if puzzle[i][j] == 1:
        count += 1
      rotate[j][len(puzzle) - 1 - i] = puzzle[i][j]
  return rotate, count


def solution(game_board, table):
  answer = 0
  empty_blocks = find_block(game_board, 0)
  puzzles = find_block(table, 1)

  for empty in empty_blocks:
    filled = False
    table = make_table(empty)

    for puzzle_origin in puzzles:
      if filled:
        break

      puzzle = make_table(puzzle_origin)
      for i in range(4):
        puzzle, count = rotate(puzzle)

        if table == puzzle:
          answer += count
          puzzles.remove(puzzle_origin)
          filled = True
          break

  return answer
