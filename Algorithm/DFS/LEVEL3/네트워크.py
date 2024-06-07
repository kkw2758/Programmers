# DFS를 이용한 풀이


def solution(n, computers):
  visited = [False] * n

  def dfs(start):

    stack = [start]
    visited[start] = True
    while stack:
      now = stack.pop()
      for i in range(n):
        if not visited[i] and computers[now][i] == 1:
          visited[i] = True
          stack.append(i)

  answer = 0

  for i in range(n):
    if not visited[i]:
      dfs(i)
      answer += 1

  return answer


print(solution(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]]))
print(solution(3, [[1, 1, 0], [1, 1, 1], [0, 1, 1]]))

# BFS를 이용한 풀이

import heapq


def solution(n, computers):
  visited = [False] * n

  def bfs(start):
    q = []
    heapq.heappush(q, start)
    visited[start] = True
    while q:
      now = heapq.heappop(q)
      for i in range(n):
        if not visited[i] and computers[now][i] == 1:
          visited[i] = True
          heapq.heappush(q, i)

  answer = 0

  for i in range(n):
    if not visited[i]:
      bfs(i)
      answer += 1

  return answer


print(solution(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]]))
print(solution(3, [[1, 1, 0], [1, 1, 1], [0, 1, 1]]))
