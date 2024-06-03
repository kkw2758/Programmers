# 나의 풀이 1
# defaultdict를 이용한 풀이
from collections import defaultdict


def solution1(answers):
  array = [[1, 2, 3, 4, 5], [2, 1, 2, 3, 2, 4, 2, 5],
           [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]]
  result_dict = defaultdict(int)
  for i in range(len(answers)):
    for j in range(3):
      if answers[i] == array[j][i % len(array[j])]:
        result_dict[j + 1] += 1

  answer = []
  max_count = 0
  result = list(result_dict.items())

  for index, count in result:
    max_count = max(max_count, count)

  for index, count in result:
    if count == max_count:
      answer.append(index)

  answer.sort()
  return answer


print(solution1([1, 2, 3, 4, 5]))
print(solution1([1, 3, 2, 4, 2]))


# 나의 풀이 2
# 딕셔너리를 사용하지 않은 풀이
def solution2(answers):
  array = [[1, 2, 3, 4, 5], [2, 1, 2, 3, 2, 4, 2, 5],
           [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]]
  temp = []
  for i in range(3):
    temp.append([i + 1, 0])

  for i in range(len(answers)):
    for j in range(3):
      if answers[i] == array[j][i % len(array[j])]:
        temp[j][1] += 1

  answer = []
  max_count = 0

  for index, count in temp:
    max_count = max(max_count, count)

  for index, count in temp:
    if count == max_count:
      answer.append(index)

  answer.sort()
  return answer


print(solution2([1, 2, 3, 4, 5]))
print(solution2([1, 3, 2, 4, 2]))


# 다른 사람 풀이
# 파이썬에서 제공하는 enumerate 기능을 잘 활용한 코드
def solution(answers):
  pattern1 = [1, 2, 3, 4, 5]
  pattern2 = [2, 1, 2, 3, 2, 4, 2, 5]
  pattern3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
  score = [0, 0, 0]
  result = []

  for idx, answer in enumerate(answers):
    if answer == pattern1[idx % len(pattern1)]:
      score[0] += 1

    if answer == pattern2[idx % len(pattern2)]:
      score[1] += 1

    if answer == pattern3[idx % len(pattern3)]:
      score[2] += 1

  max_score = max(score)
  for idx, s in enumerate(score):
    if s == max_score:
      result.append(idx + 1)

  return result
