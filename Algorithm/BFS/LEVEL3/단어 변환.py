from collections import deque

answer = 0

def get_different_count(word1, word2):
  count = 0
  for i in range(len(word1)):
    if word1[i] != word2[i]:
      count += 1

  return count

def solution(begin, target, words):

  def bfs(begin, target, words, cnt):
    global answer
    q = deque()
    q.append([begin, 0])
    visited = set()
    visited.add(begin)

    while q:
      now, count = q.popleft()
      if now == target:
        answer = count
        return
      for word in words:
        if word not in visited and get_different_count(word, now) == 1:
          q.append([word, count + 1])
          visited.add(word)

  bfs(begin, target, words, 0)
  return answer

print(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]))

from collections import deque

answer = 0


def get_different_count(word1, word2):
  count = 0
  for i in range(len(word1)):
    if word1[i] != word2[i]:
      count += 1

  return count


def solution(begin, target, words):
  global answer
  q = deque()
  q.append([begin, 0])
  visited = set()
  visited.add(begin)

  while q:
    now, count = q.popleft()
    if now == target:
      answer = count
      break
    for word in words:
      if word not in visited and get_different_count(word, now) == 1:
        q.append([word, count + 1])
        visited.add(word)

  return answer


print(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]))
