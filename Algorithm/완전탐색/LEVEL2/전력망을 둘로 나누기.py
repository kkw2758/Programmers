def solution(n, wires):
  answer = 101
  graph = [[] for _ in range(n + 1)]
  # 양방향 그래프 생성
  for wire in wires:
    graph[wire[0]].append(wire[1])
    graph[wire[1]].append(wire[0])

  for wire in wires:
    answer = min(answer, abs(get_connected_node(1, graph, wire) * 2 - n))

  return answer


def get_connected_node(start, graph, wire):
  stack = [start]
  visited = [False] * len(graph)
  visited[start] = True

  while stack:
    now = stack.pop()
    for node in graph[now]:
      if not visited[node] and [now, node] not in (wire, wire[::-1]):
        stack.append(node)
        visited[node] = True

  result = 0
  for i in range(1, len(visited)):
    if visited[i]:
      result += 1
  return result


print(
    solution(9,
             [[1, 3], [2, 3], [3, 4], [4, 5], [4, 6], [4, 7], [7, 8], [7, 9]]))
print(solution(4, [[1, 2], [2, 3], [3, 4]]))
print(solution(7, [[1, 2], [2, 7], [3, 7], [3, 4], [4, 5], [6, 7]]))

# 다른 사람 풀이
# BFS를 이용한 풀이, 파이썬 중첩 함수 사용

from collections import deque


def solution(n, wires):
  graph = [[] for _ in range(n + 1)]
  for a, b in wires:
    graph[a].append(b)
    graph[b].append(a)

  def bfs(start):
    visited = [0] * (n + 1)
    q = deque([start])
    visited[start] = 1
    cnt = 1
    while q:
      s = q.popleft()
      for i in graph[s]:
        if not visited[i]:
          q.append(i)
          visited[i] = 1
          cnt += 1

    return cnt

  res = n
  for a, b in wires:
    graph[a].remove(b)
    graph[b].remove(a)

    res = min(abs(bfs(a) - bfs(b)), res)

    graph[a].append(b)
    graph[b].append(a)

  return res


print(
    solution(9,
             [[1, 3], [2, 3], [3, 4], [4, 5], [4, 6], [4, 7], [7, 8], [7, 9]]))
print(solution(4, [[1, 2], [2, 3], [3, 4]]))
print(solution(7, [[1, 2], [2, 7], [3, 7], [3, 4], [4, 5], [6, 7]]))
