# 나의 풀이 - 문제 해결 X
def solution(users, emoticons):
  global result
  answer = [0, 0]

  def back_tracking(min_discount_ratio, start_idx, price):
    global result
    if result < price:
      result = price
    for idx in range(start_idx, len(emoticons)):
      for discount_ratio in [10, 20, 30, 40]:
        if discount_ratio >= min_discount_ratio:
          back_tracking(min_discount_ratio, idx + 1,
                        price + emoticons[idx] * (100 - discount_ratio) / 100)

  for min_discont_ratio, target_price in users:
    result = 0
    back_tracking(min_discont_ratio, 0, 0)
    if result >= target_price:
      answer[0] += 1
    else:
      answer[1] += result
  return answer


print(solution([[40, 10000], [25, 10000]], [7000, 9000]))

# 참고 풀이 - DFS를 이용해 모든 경우를 구함과 동시에 정답을 갱신하는 함수 작성
# https://magentino.tistory.com/59
discounts = [10, 20, 30, 40]
answer = [-1, -1]


def solution(users, emoticons):
  n, m = len(users), len(emoticons)
  discount_list = [0] * m

  def search(idx):
    global answer
    if idx == m:
      sale_num, cost_num = 0, 0
      for i in range(n):
        tmp = 0
        for j in range(m):
          if users[i][0] <= discount_list[j]:
            tmp += emoticons[j] * (100 - discount_list[j]) // 100
        if tmp >= users[i][1]:
          sale_num += 1
        else:
          cost_num += tmp
      if sale_num > answer[0] or (sale_num == answer[0]
                                  and cost_num > answer[1]):
        answer = [sale_num, cost_num]
      return

    for i in range(4):
      discount_list[idx] = discounts[i]
      search(idx + 1)

  search(0)

  return answer


print(solution([[40, 10000], [25, 10000]], [7000, 9000]))


# 참고 풀이 - DFS 를 이용하여 모든 경우를 구해 리스트에 저장 한 뒤 문제 해결
# https://velog.io/@yohan11/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-Lv2.-%EC%9D%B4%EB%AA%A8%ED%8B%B0%EC%BD%98-%ED%95%A0%EC%9D%B8%ED%96%89%EC%82%AC-Python-%ED%8C%8C%EC%9D%B4%EC%8D%AC
def solution(users, emoticons):
  answer = [0, 0]
  data = [10, 20, 30, 40]
  discount = []

  # 이모티콘 할인율 구하기
  def dfs(temp, depth):
    if depth == len(temp):
      discount.append(temp[:])
      return
    for d in data:
      temp[depth] += d
      dfs(temp, depth + 1)
      temp[depth] -= d

  dfs([0] * len(emoticons), 0)

  print(len(discount))
  print(discount)

  for d in range(len(discount)):
    plus_user = 0
    profit = 0

    for user in users:
      emoticon_buy = 0
      for i in range(len(emoticons)):
        if discount[d][i] >= user[0]:
          emoticon_buy += emoticons[i] * ((100 - discount[d][i]) / 100)
      if user[1] <= emoticon_buy:
        plus_user += 1
      else:
        profit += emoticon_buy

    if answer[0] < plus_user:
      answer = [plus_user, int(profit)]
    elif answer[0] == plus_user:
      if answer[1] < profit:
        answer = [plus_user, int(profit)]

  return answer


print(solution([[40, 10000], [25, 10000]], [7000, 9000]))

# 중복 순열 이용한 풀이
from itertools import product


def solution(users, emoticons):
  discounts = [10, 20, 30, 40]
  answer = [0, 0]
  candidates = list(product(discounts, repeat=len(emoticons)))

  for candidate in candidates:
    plus_count = 0
    profit = 0

    for user in users:
      emoticon_price = 0
      for idx, discount_ratio in enumerate(candidate):
        if discount_ratio >= user[0]:
          emoticon_price += ((100 - discount_ratio) / 100) * emoticons[idx]
      if emoticon_price >= user[1]:
        plus_count += 1
      else:
        profit += int(emoticon_price)

    if answer[0] < plus_count:
      answer = [plus_count, profit]
    elif answer[0] == plus_count:
      if answer[1] < profit:
        answer = [plus_count, profit]
  return answer


print(solution([[40, 10000], [25, 10000]], [7000, 9000]))
