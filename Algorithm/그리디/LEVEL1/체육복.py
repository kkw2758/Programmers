# 답안 풀이
# 그리디 알고리즘
def solution(n, lost, reserve):

  reserve = set(reserve)
  lost = set(lost)
  same = reserve & lost
  reserve = reserve - same
  lost = lost - same

  for num in reserve:
    if num - 1 in lost:
      lost.remove(num - 1)
    elif num + 1 in lost:
      lost.remove(num + 1)
  return n - len(lost)
