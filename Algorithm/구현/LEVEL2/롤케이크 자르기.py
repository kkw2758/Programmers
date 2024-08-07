# 나의 코드 - 시간 초과 발생
# 슬라이싱의 시간 복잡도를 고려하지 않은 풀이
# O(N^2)
def solution(topping):
  answer = 0

  # 슬라이싱 말고 어떤 방법?
  for i in range(len(topping)):
    left = set(topping[:i])
    right = set(topping[i:])

    if len(left) == len(right):
      answer += 1
  return answer


print(solution([1, 2, 1, 3, 1, 4, 1, 2]))


# -------------------
# 참고 : https://peace-log.tistory.com/entry/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-%EB%A1%A4%EC%BC%80%EC%9D%B4%ED%81%AC-%EC%9E%90%EB%A5%B4%EA%B8%B0-python
def solution(topping):
  answer = 0

  right_topping_dict = {}
  for t in topping:
    if t in right_topping_dict:
      right_topping_dict[t] += 1
    else:
      right_topping_dict[t] = 1

  left_tpping_dict = {}
  for t in topping:
    if len(left_tpping_dict) == len(right_topping_dict):
      answer += 1

    if t not in left_tpping_dict:
      left_tpping_dict[t] = 1

    right_topping_dict[t] -= 1

    if right_topping_dict[t] == 0:
      del right_topping_dict[t]

  return answer


print(solution([1, 2, 1, 3, 1, 4, 1, 2]))
# -------------------
from collections import defaultdict


def solution(topping):
  answer = 0

  right_topping_dict = defaultdict(int)
  for t in topping:
    right_topping_dict[t] += 1

  left_tpping_dict = defaultdict(int)
  for t in topping:
    if len(left_tpping_dict) == len(right_topping_dict):
      answer += 1

    if t not in left_tpping_dict:
      left_tpping_dict[t] += 1

    right_topping_dict[t] -= 1
    if right_topping_dict[t] == 0:
      del right_topping_dict[t]

  return answer


print(solution([1, 2, 1, 3, 1, 4, 1, 2]))
# -------------------
# 참고 : https://velog.io/@minmong/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-Lv.2-%EB%A1%A4%EC%BC%80%EC%9D%B4%ED%81%AC-%EC%9E%90%EB%A5%B4%EA%B8%B0-Python-velog
from collections import Counter


def solution(topping):
  right_topping_dict = Counter(topping)
  left_tpping_set = set()
  res = 0
  for i in topping:
    right_topping_dict[i] -= 1
    left_tpping_set.add(i)
    if right_topping_dict[i] == 0:
      right_topping_dict.pop(i)
    if len(right_topping_dict) == len(left_tpping_set):
      res += 1

  return res


print(solution([1, 2, 1, 3, 1, 4, 1, 2]))
