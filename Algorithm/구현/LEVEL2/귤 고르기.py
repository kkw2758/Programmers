# tangerine의 원소가 최대 10,000,000 이므로 조합을 이용하면 시간 초과
# 딕셔너리를 이용해서 특정 숫자가 몇번 나오는지 세어보자


def solution(k, tangerine):
  answer = 0
  number_cnt = {}
  for number in tangerine:
    if number in number_cnt:
      number_cnt[number] += 1
    else:
      number_cnt[number] = 1

  number_cnt = list(number_cnt.items())
  number_cnt.sort(key=lambda x: -x[1])

  temp = 0
  for number, cnt in number_cnt:
    temp += cnt
    answer += 1
    if temp >= k:
      break
  return answer


print(solution(6, [1, 3, 2, 5, 4, 2, 5, 2, 3]))
