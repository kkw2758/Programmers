# DFS
# def solution(n, k, enemy):
#   global answer
#   answer = 0

#   def dfs(n, round, k):
#     global answer
#     if round == len(enemy) or (n < enemy[round] and k == 0):
#       answer = max(answer, round)
#       return

#     if k > 0:
#       # 무적권 사용 가능
#       dfs(n, round + 1, k - 1)

#     # 무적권 사용 X
#     if n >= enemy[round]:
#       dfs(n - enemy[round], round + 1, k)

#   dfs(n, 0, k)
#   return answer

# print(solution(7, 3, [4, 2, 4, 5, 3, 3, 1]))
# print(solution(2, 4, [3, 3, 3, 3]))

# BFS
# from collections import deque


# def solution(n, k, enemy):
#   q = deque()
#   q.append([n, k, 0])

#   while q:
#     remain_soldier, remain_chance, round = q.popleft()
#     if round >= len(enemy):
#       break

#     # 무적권 쓸 수 있으면
#     if remain_chance > 0:
#       q.append([remain_soldier, remain_chance - 1, round + 1])
#       if remain_soldier - enemy[round] >= 0:
#         q.append([remain_soldier - enemy[round], remain_chance, round + 1])
#     else:
#       if remain_soldier - enemy[round] >= 0:
#         q.append([remain_soldier - enemy[round], remain_chance, round + 1])

#   return round


# print(solution(7, 3, [4, 2, 4, 5, 3, 3, 1]))
# print(solution(2, 4, [3, 3, 3, 3]))


import heapq

def solution(n, k, enemy):
  if k >= len(enemy):
    return len(enemy)

  # 최대 몇 라운드 까지 갈 수 있느지를 구해야함.
  answer = 0
  num = 0
  hq = []

  for e in enemy:
    heapq.heappush(hq, -e)
    num += e
    if num > n:
      if not k:
        break

      k -= 1
  
      num += heapq.heappop(hq)
    answer += 1

  return answer

print(solution(7, 3, [4, 2, 4, 5, 3, 3, 1]))
print(solution(2, 4, [3, 3, 3, 3]))