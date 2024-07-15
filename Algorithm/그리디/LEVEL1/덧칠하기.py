def solution(n, m, section):
  answer = 0
  # n 벽의 길이
  # m 롤러 길이
  # section 다시 칠해야하는 구역의 번호
  now = 0
  for num in section:
    # 아직 안칠해졌으면
    if now < num:
      # 칠하고
      answer += 1
      if num + m - 1 > n:
        break
      else:
        now = num + m - 1
  return answer


print(solution(8, 4, [2, 3, 6]))
print(solution(5, 4, [1, 3]))
print(solution(4, 1, [1, 2, 3, 4]))
