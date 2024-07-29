# weights의 길이가 100,000이 될 수도 있으므로 O(N^2) 은 힘들 것 같다.

# 참고 풀이 1
from collections import Counter


def solution(weights):
  answer = 0

  # 1:1
  counter = Counter(weights)
  for k, v in counter.items():
    if v >= 2:
      answer += v * (v - 1) // 2
  weights = set(weights)

  # 2:3, 2:4, 3:4 비율 가지면 짝궁 가능함.
  for w in weights:
    if w * 2 / 3 in weights:
      answer += counter[w * 2 / 3] * counter[w]
    if w * 2 / 4 in weights:
      answer += counter[w * 2 / 4] * counter[w]
    if w * 3 / 4 in weights:
      answer += counter[w * 3 / 4] * counter[w]
  return answer


# 참고 풀이 2
# 참고 풀이 1 과 아이디어는 동일하나 Counter 대신 defaultdict 이용
from collections import defaultdict


def solution(weights):
  answer = 0
  length = len(weights)
  weight_dict = defaultdict(int)

  for weight in weights:
    weight_dict[weight] += 1

  for key, val in weight_dict.items():
    if val > 1:
      answer += val * (val - 1) // 2
    if key * 2 in weight_dict:
      answer += val * weight_dict[key * 2]
    if key * 3 % 2 == 0 and key * 3 // 2 in weight_dict:
      answer += val * weight_dict[key * 3 // 2]
    if key * 4 % 3 == 0 and key * 4 // 3 in weight_dict:
      answer += val * weight_dict[key * 4 // 3]

  return answer
