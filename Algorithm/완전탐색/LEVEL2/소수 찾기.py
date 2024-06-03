# numbers는 길이 1 이상 7 이하인 문자열
# numbers는 0 ~ 9까지 숫자만으로 이루어져 있음
# 소수 몇개 가능한가?
# "17"을 뽑았을 때
# 하나 뽑는 경우 1 7
# 두개 뽑는 경우 17 71

# "011"을 뽑았을 때
# 하나 뽑는 경우 0 1
# 두개 뽑는 경우 10 11
# 3개 뽑는 경우 101 110

#순열?

# from itertools import permutations
# a = [1,2,3]
# permute = permutations(a,2)
# print(list(permute))
# '''
# 결과
# '''
# [(1,2),(1,3),(2,1),(2,3),(3,1),(3,2)]

# 나의 풀이
# 파이썬에서 제공하는 순열 라이브러리를 이용해서 완전 탐색
from itertools import permutations
import math


def is_prime(num):
  if num <= 1:
    return False

  for i in range(2, int(math.sqrt(num)) + 1):
    if num % i == 0:
      return False
  return True


def solution(numbers):
  number_set = set()
  for i in range(1, len(numbers) + 1):
    for member in list(permutations(numbers, i)):
      number_set.add(int("".join(member)))

  answer = 0

  for number in list(number_set):
    if is_prime(number):
      answer += 1

  return answer


print(solution("17"))
print(solution("011"))

# 다른 사람 풀이1
# 에라토스테네스의 체 이용
from itertools import permutations


def solution(n):
  a = set()
  for i in range(len(n)):
    a |= set(map(int, map("".join, permutations(list(n), i + 1))))

  a -= set(range(0, 2))  # 0, 1  제거

  # 에라토스테네스의 체
  # 주어진 수로 만들 수 있는 가장 큰 수보다 작은 소수들을 집합 a 에서 제거
  for i in range(2, int(max(a)**0.5) + 1):
    # 소수가 아닌 수를 걸러주는 과정
    a -= set(range(i * 2, max(a) + 1, i))
  return len(a)
