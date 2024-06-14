# 나의 풀이 1
# 최소 힙, 최대 힙 이용
import heapq


def solution(operations):
  min_heap = []
  max_heap = []
  answer = []

  for operation in operations:
    flag, value = operation.split()
    value = int(value)
    if operation[0] == "I":
      heapq.heappush(min_heap, value)
      heapq.heappush(max_heap, value * -1)
    elif operation[0] == "D" and min_heap:
      if value == 1:  # 최댓값 제거 - 최소 힙 사용
        heapq.heappop(max_heap)
        min_heap = []
        for member in max_heap:
          heapq.heappush(min_heap, member * -1)
      elif value == -1:  # 최솟값 제거 - 최대 힙 사용
        heapq.heappop(min_heap)
        max_heap = []
        for member in min_heap:
          heapq.heappush(max_heap, member * -1)

  if min_heap:
    answer.append(max(min_heap))
    answer.append(min(min_heap))
  else:
    answer.append(0)
    answer.append(0)
  return answer


print(solution(["I 16", "I -5643", "D -1", "D 1", "D 1", "I 123", "D -1"]))
print(
    solution([
        "I -45", "I 653", "D 1", "I -642", "I 45", "I 97", "D 1", "D -1",
        "I 333"
    ]))

# 나의 풀이 2
# 최소 힙, 최대 힙 이용
# 코드를 좀더 깔끔하게 개선
import heapq


def solution(operations):
  min_heap = []
  max_heap = []

  for operation in operations:
    flag, value = operation.split()
    value = int(value)

    if flag == "I":
      heapq.heappush(min_heap, value)
      heapq.heappush(max_heap, value * -1)
    elif flag == "D" and min_heap and max_heap:
      if value == 1:  # 최대값 삭제
        max_value = heapq.heappop(max_heap)
        min_heap.remove(max_value * -1)
      elif value == -1:  # 최소값 삭제
        min_value = heapq.heappop(min_heap)
        max_heap.remove(min_value * -1)

  if min_heap and max_heap:
    max_value = heapq.heappop(max_heap) * -1
    min_value = heapq.heappop(min_heap)
    return [max_value, min_value]
  else:
    return [0, 0]


print(solution(["I 16", "I -5643", "D -1", "D 1", "D 1", "I 123", "D -1"]))
print(
    solution([
        "I -45", "I 653", "D 1", "I -642", "I 45", "I 97", "D 1", "D -1",
        "I 333"
    ]))
