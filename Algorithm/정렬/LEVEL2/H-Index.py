# 나의 풀이
# 정렬 후 완전 탐색
def solution(citations):

  def count_higher_value(pivot, target_list):
    count = 0
    for value in target_list:
      if pivot <= value:
        break
      count += 1
    return len(target_list) - count

  answer = 0
  citations.sort()
  n = len(citations)
  for h in range(n + 1):
    higher = count_higher_value(h, citations)
    if higher >= h:
      answer = h
  return answer


print(solution([3, 0, 6, 1, 5]))
print(solution([3, 4]))
print(solution([0, 0]))


# H-index를 구하는 방법 참고한 풀이
# https://www.ibric.org/bric/trend/bio-series.do?mode=series_view&newsArticleNo=8802417&articleNo=8882714&beforeMode=latest_list#!/list
def solution(citations):

  citations.sort(reverse=True)

  for i in range(len(citations)):
    if i >= citations[i]:
      return i

  return len(citations)
