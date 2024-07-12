import math

result = int(1e9)


def solution(picks, minerals):
  global result
  mineral_dict = {"diamond": 0, "iron": 1, "stone": 2}
  # table[i][j] -> i 곡괭이로 j 광물 캘때 피로도
  table = [[1, 1, 1], [5, 1, 1], [25, 5, 1]]

  target_count = math.ceil(len(minerals) / 5)

  def back_tracking(pick_count, pirodo):
    global result
    # picks 최신화
    if pick_count == target_count or not (sum(picks)):
      result = min(pirodo, result)
      return

    for i in range(3):
      if picks[i]:
        picks[i] -= 1
        additional_pirodo = 0
        for mineral in minerals[pick_count * 5:(pick_count + 1) * 5]:
          additional_pirodo += table[i][mineral_dict[mineral]]
        back_tracking(pick_count + 1, pirodo + additional_pirodo)
        picks[i] += 1

  back_tracking(0, 0)
  return result


# print(
#     solution([1, 3, 2], [
#         "diamond", "diamond", "diamond", "iron", "iron", "diamond", "iron",
#         "stone"
#     ]))

print(
    solution([0, 1, 1], [
        "diamond", "diamond", "diamond", "diamond", "diamond", "iron", "iron",
        "iron", "iron", "iron", "diamond"
    ]))

# 다른풀이 - 구현, 정렬


def solution(picks, minerals):
  sum = 0
  for x in picks:
    sum += x

  # 캘 수 있는 광물의 개수
  num_min = sum * 5
  if len(minerals) > num_min:
    minerals = minerals[:num_min]

  # 광물 조사
  cnt_min = [[0, 0, 0] for x in range(10)] # dia, iron, stone
  for i in range(len(minerals)):
    if minerals[i] == "diamond":
      cnt_min[i//5][0] += 1
    elif minerals[i] == "iron":
      cnt_min[i//5][1] += 1
    else:
      cnt_min[i//5][2] += 1

  # 피로도가 높은 순서대로 광물 정렬
  sorted_cnt_min = sorted(cnt_min, key = lambda x: (-x[0], -x[1], -x[2]))

  # 피로도 계산
  answer = 0
  for mineral in sorted_cnt_min:
    d, i, s = mineral
    for p in range(len(picks)):
      if p == 0 and picks[0] > 0: # dia 곡괭이
        picks[p] -= 1
        answer += d + i + s
        break
      elif p == 1 and picks[p] > 0: # iron 곡괭이
        picks[p] -= 1
        answer += 5 * d + i + s
        break
      elif p == 2 and picks[p] > 0:
        picks[p] -= 1
        answer += 25*d + 5 * i + s
        break

  return answer