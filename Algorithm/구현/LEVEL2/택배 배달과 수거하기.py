# 나의 풀이
def solution(cap, n, deliveries, pickups):
  answer = 0

  # 들러야할 장소 중에서 가장 멀리 있는 위치의 인덱스를 반환한다.
  # 추가적으로 가장 멀리 있는 위치의 인덱스부터 배열을 거꾸로 순회하면서 용량(cap) 만큼 배열에서 값을 빼준다.
  def find_not_zero_biggest_index(li, cap):
    result = -1
    for i in range(len(li)):
      if li[i] != 0:
        result = i

    cnt = 0
    index = result
    while index >= 0 and cnt < cap:
      if li[index] != 0:
        if cap - cnt >= li[index]:
          cnt += li[index]
          li[index] = 0
        else:
          li[index] -= (cap - cnt)
          break
      index -= 1

    return result

  while True:
    max_delivery_idx = find_not_zero_biggest_index(deliveries, cap)
    max_pickup_idx = find_not_zero_biggest_index(pickups, cap)

    # 더이상 배달하거나 수거할 택배 상자가 없을 때
    if max_delivery_idx == -1 and max_pickup_idx == -1:
      break

    # 문제에서 구해야하는 값은 인덱스가 아니라 거리이기 때문에 + 1 을 해줌
    answer += max(max_delivery_idx + 1, max_pickup_idx + 1) * 2
  return answer


print(solution(4, 5, [1, 0, 3, 1, 2], [0, 3, 0, 4, 0]))

# 참고 풀이
# https://oh2279.tistory.com/147
# 한번에 최대한 멀리가서 멀리 있는 곳들의 작업을 먼저 끝내야지 이동횟수를 최소한으로 만들 수 있다.
# 한번 가면 다시 물류창고로 되돌아와야 함


def solution(cap, n, deliveries, pickups):
  deliveries = deliveries[::-1]
  pickups = pickups[::-1]
  answer = 0

  have_to_deli = 0
  have_to_pick = 0

  for i in range(n):
    have_to_deli += deliveries[i]
    have_to_pick += pickups[i]

    # have_to_~ 의 값이 음수라면 해당 위치의 배달/픽업 값이 한번에 실어 나를 수 있는 용량(cap)보다 적은 것이므로, 오가는 길에 추가적으로 배달/픽업이 가능하다.
    # have_to_deli, have_to_pick의 값이 양수가 되기 전까지는 이동이 필요 없고, 이 두 값 중 하나라도 양수가 될 때만 해당 위치로 이동해주면 된다.
    while have_to_deli > 0 or have_to_pick > 0:
      have_to_deli -= cap
      have_to_pick -= cap
      answer += (n - i) * 2

  return answer
