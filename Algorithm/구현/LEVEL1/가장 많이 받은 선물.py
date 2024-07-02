def solution(friends, gifts):
  mapping_info = dict()
  for i, friend in enumerate(friends):
    mapping_info[friend] = i

  graph = []

  for i in range(len(friends)):
    graph.append([0] * len(friends))

  for i in range(len(friends)):
    graph[i][i] = -1

  for gift in gifts:
    A, B = gift.split()
    graph[mapping_info[A]][mapping_info[B]] += 1

  present_points = []
  for i in range(len(friends)):
    give_cnt = 0
    receive_cnt = 0
    for j in range(len(friends)):
      if graph[i][j] != -1:
        give_cnt += graph[i][j]
    for j in range(len(friends)):
      if graph[j][i] != -1:
        receive_cnt += graph[j][i]
    present_point = give_cnt - receive_cnt
    present_points.append(present_point)

  result = [0] * len(friends)
  for i in range(len(friends)):
    for j in range(len(friends)):
      if i != j:
        # i 가 j 한테 준 선물이 j가 i 한테 준 선물보다 많다면
        if graph[i][j] > graph[j][i]:
          result[i] += 1
        elif graph[i][j] == graph[j][i]:
          if present_points[i] > present_points[j]:
            result[i] += 1

  return max(result)


print(
    solution(["muzi", "ryan", "frodo", "neo"], [
        "muzi frodo", "muzi frodo", "ryan muzi", "ryan muzi", "ryan muzi",
        "frodo muzi", "frodo ryan", "neo muzi"
    ]))
