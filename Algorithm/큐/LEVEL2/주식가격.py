# 나의 풀이 1
# 시간 초과
from collections import deque


def solution(prices):
  answer = []
  prices = deque(prices)

  while prices:
    now = prices.popleft()
    cnt = 0
    for i in range(len(prices)):
      cnt += 1
      if prices[i] < now:
        break
    answer.append(cnt)
  return answer


print(solution([1, 2, 3, 2, 3]))

from collections import deque


def solution(prices):
  queue = deque(prices)
  answer = []

  while queue:
    price = queue.popleft()
    cnt = 0
    for q in queue:
      cnt += 1
      if price > q:
        break
    answer.append(cnt)
  return answer


print(solution([1, 2, 3, 2, 3]))
