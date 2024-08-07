def solution(k, ranges):
  answer = []
  x_cordinates = [k]
  while k != 1:
    if k % 2 == 0:
      k //= 2
    else:
      k = k * 3 + 1
    x_cordinates.append(k)

  n = len(x_cordinates)
  for rng in ranges:
    start = rng[0]
    end = n + rng[1] - 1
    if start == end:
      answer.append(0.0)
    elif start > end:
      answer.append(-1.0)
    else:
      tmp = 0
      for i in range(start, end):
        tmp += max(x_cordinates[i], x_cordinates[
            i + 1]) - abs(x_cordinates[i] - x_cordinates[i + 1]) * 0.5
      answer.append(tmp)
  return answer


print(solution(5, [[0, 0], [0, -1], [2, -3], [3, -3]]))
