from itertools import combinations
from math import sqrt


def solution(nums):

  def is_prime(num):
    for i in range(2, int(sqrt(num)) + 1):
      if num % i == 0:
        return False
    return True

  answer = 0
  candidates = list(combinations(nums, 3))

  for candidate in candidates:
    if is_prime(sum(candidate)):
      answer += 1
  return answer


print(solution([1, 2, 3, 4]))
print(solution([1, 2, 7, 6, 4]))
