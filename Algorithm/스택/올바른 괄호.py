# 나의 풀이 1
# 큐를 이용한 풀이
from collections import deque


def solution(s):
  q = deque(s)
  result = 0
  for _ in range(len(q)):
    now = q.popleft()
    if now == '(':
      result += 1
    else:
      result -= 1
    if result < 0:
      return False

  if result != 0:
    return False

  return True


print(solution("()()"))
print(solution("(()("))


# 나의 풀이 2
# 스택을 이용한 풀이
def solution(s):
  array = list(s)
  result = 0
  for _ in range(len(array)):
    now = array.pop()
    if now == '(':
      result += 1
    else:
      result -= 1
    if result > 0:
      return False

  if result != 0:
    return False

  return True


print(solution("()()"))
print(solution("(()("))


# 다른 사람 풀이
def solution(s):
  stack = []
  for i in s:
    if i == '(':  # '('는 stack에 추가
      stack.append(i)
    else:  # i == ')'인 경우
      if stack == []:  # 괄호 짝이 ')'로 시작하면 False 반환
        return False
      else:
        stack.pop()  # '('가 ')'와 짝을 이루면 stack에서 '(' 하나 제거

  return stack == []
