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
