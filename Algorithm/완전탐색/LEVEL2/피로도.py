# 나의 풀이1 - 오답
# 백트래킹


def solution(k, dungeons):
  count = 0
  # 더 이상 돌 수 있는 던전이 없으면
  if len(dungeons) == 0:
    return
  # # 지금 방문할 던전의 최소 필요 피로도가 현재 피로도보다 높다면
  # if k < dungeons[-1][0]:
  #   return

  for i in range(len(dungeons)):
    min_piro, use_piro = dungeons.pop()
    if min_piro <= k:
      solution(k - use_piro, dungeons)
      count += 1
    dungeons.append([min_piro, use_piro])

  return count


print(solution(80, [[80, 20], [50, 40], [30, 10]]))
print(solution(80, [[30, 10], [80, 20], [50, 40]]))


# 나의 풀이 2 - 정답
def solution(k, dungeons):
  print("k = ", k)
  print("dungeons = ", dungeons)
  answer = 0
  # 더 이상 돌 수 있는 던전이 없으면
  if len(dungeons) == 0:
    return answer

  for i in range(len(dungeons)):
    if dungeons[i][0] <= k:
      min_piro, use_piro = dungeons.pop(i)
      answer = max(answer, 1 + solution(k - use_piro, dungeons))
      dungeons.insert(i, [min_piro, use_piro])

  return answer


print(solution(80, [[80, 20], [60, 20]]))
print(solution(80, [[80, 20], [50, 40], [30, 10]]))

# 다른 사람 풀이
answer = 0


def dfs(k, cnt, dungeons, visited):
  global answer
  if cnt > answer:
    answer = cnt

  for i in range(len(dungeons)):
    if not visited[i] and k >= dungeons[i][0]:
      visited[i] = True
      dfs(k - dungeons[i][1], cnt + 1, dungeons, visited)
      visited[i] = False


def solution(k, dungeons):
  global answer
  visited = [False] * len(dungeons)
  dfs(k, 0, dungeons, visited)
  return answer


print(solution(80, [[80, 20], [50, 40], [30, 10]]))
