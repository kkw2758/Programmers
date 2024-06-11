from collections import deque


def has_higher_priority(priority_dict, target):
  for key in priority_dict.keys():
    if priority_dict[target] < priority_dict[key]:
      return True

  return False


def solution(priorities, location):
  result = []
  priority_dict = {}

  q = deque()
  for i in range(len(priorities)):
    q.append(chr(i + 65))
    priority_dict[chr(i + 65)] = priorities[i]
  while q:
    now = q.popleft()
    # 우선 순서가 더 높은 프로세스가 있다면
    if has_higher_priority(priority_dict, now):
      q.append(now)
    else:
      del priority_dict[now]
      result.append(now)
  answer = result.index(chr(location + 65)) + 1
  return answer


print(solution([2, 1, 3, 2], 2))
print(solution([1, 1, 9, 1, 1, 1], 0))


def solution(priorities, location):
  queue = [(idx, p) for idx, p in enumerate(priorities)]
  answer = 0
  while True:
    now = queue.pop(0)
    if any(now[1] < q[1] for q in queue):
      queue.append(now)
    else:
      answer += 1
      if now[0] == location:
        return answer


print(solution([2, 1, 3, 2], 2))
print(solution([1, 1, 9, 1, 1, 1], 0))
