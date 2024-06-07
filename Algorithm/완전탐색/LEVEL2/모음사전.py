# 다른 풀이 1
# 중복 순열 라이브러리를 이용해 답이 될 수 있는 후보를 list에 담은 뒤 찾고자 하는 인덱스 값을 찾아서 반환
from itertools import product


def solution(word):
  candidates = set()

  for i in range(1, 6):
    for candidate in product("AEIOU", repeat=i):
      candidates.add("".join(candidate))

  candidates = list(candidates)
  candidates.sort()

  return candidates.index(word) + 1


print(solution("AAAAE"))


# 다른 풀이 2
# DFS를 이용해 답이 될 수 있는 후보를 list에 담은 뒤 찾고자하는 인덱스 값을 찾아서 반환
def solution(word):
  vowels = "AEIOU"
  candidates = []

  def dfs(s):
    global cnt
    if len(s) > 5:
      return
    candidates.append(s)
    for vowel in vowels:
      dfs(s + vowel)

  dfs("")
  candidates.sort()
  # dfs 함수의 시작값이 공백이므로 +1을 해줄 필요가 없다.
  return candidates.index(word)


# 다른 풀이 3
# DFS와 전역변수를 사용한 풀이
cnt = -1
answer = 0


def solution(word):
  vowels = "AEIOU"

  def dfs(count, s):
    global cnt, answer
    if len(s) > 5:
      return

    cnt += 1
    if s == word:
      answer = cnt
    for vowel in vowels:
      dfs(cnt, s + vowel)

  dfs(0, "")
  return answer


print(solution("EIO"))
