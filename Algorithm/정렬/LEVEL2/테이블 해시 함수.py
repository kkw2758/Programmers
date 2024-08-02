def solution(data, col, row_begin, row_end):
  answer = 0
  data.sort(key=lambda x: (x[col - 1], -x[0]))
  S_i_list = []
  for i in range(row_begin - 1, row_end):
    S_i = 0
    for member in data[i]:
      S_i += member % (i + 1)
    S_i_list.append(S_i)

  for S_i in S_i_list:
    answer ^= S_i
  return answer


print(solution(
    [[2, 2, 6], [1, 5, 10], [4, 2, 9], [3, 8, 3]],
    2,
    2,
    3,
))
