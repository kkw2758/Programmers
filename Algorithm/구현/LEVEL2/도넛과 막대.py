def solution(edges):

  def count_edges(edges):
    edge_counts = {}
    for a, b in edges:
      if a not in edge_counts:
        edge_counts[a] = [0, 0]
      if b not in edge_counts:
        edge_counts[b] = [0, 0]
      # [in, out]
      edge_counts[a][1] += 1
      edge_counts[b][0] += 1
    return edge_counts

  def check_answer(edge_counts):
    answer = [0, 0, 0, 0]
    for key, counts in edge_counts.items():
      # 생성된 정점의 번호 확인
      if counts[1] >= 2 and counts[0] == 0:
        answer[0] = key
      # 막대 모양 그래프의 수 확인 in = 1 out = 0
      elif counts[0] > 0 and counts[1] == 0:
        answer[2] += 1
      # 8자 모양 그래프의 수 확인
      elif counts[0] >= 2 and counts[1] >= 2:
        answer[3] += 1
    # 도넛 모양 그래프의 수 확인
    answer[1] = (edge_counts[answer[0]][1] - answer[2] - answer[3])

    return answer

  edge_counts = count_edges(edges)
  answer = check_answer(edge_counts)

  return answer


print(solution([[2, 3], [4, 3], [1, 1], [2, 1]]))
