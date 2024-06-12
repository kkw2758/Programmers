from collections import deque


def solution(bridge_length, weight, truck_weights):
  answer = 0
  q = deque([0 for _ in range(bridge_length)])
  truck_weights = deque(truck_weights)

  current_weight = 0
  while q:
    answer += 1
    out_truck_weight = q.popleft()
    current_weight -= out_truck_weight

    if truck_weights:
      if current_weight + truck_weights[0] <= weight:
        in_truck_weight = truck_weights.popleft()
        q.append(in_truck_weight)
        current_weight += in_truck_weight

      else:
        q.append(0)

  return answer


print(solution(2, 10, [7, 4, 5, 6]))
print(solution(100, 100, [10]))
print(solution(100, 100, [10, 10, 10, 10, 10, 10, 10, 10, 10, 10]))

from collections import deque


def solution(bridge_length, weight, truck_weights):
  time = 0
  bridge = deque([0] * bridge_length)
  truck_weights = deque(truck_weights)

  currentWeight = 0
  while len(truck_weights) != 0:
    time += 1
    currentWeight -= bridge.popleft()
    if currentWeight + truck_weights[0] <= weight:
      currentWeight += truck_weights[0]
      bridge.append(truck_weights.popleft())
    else:
      bridge.append(0)

  time += bridge_length
  return time


print(solution(2, 10, [7, 4, 5, 6]))
print(solution(100, 100, [10]))
print(solution(100, 100, [10, 10, 10, 10, 10, 10, 10, 10, 10, 10]))
