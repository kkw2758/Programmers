# 나의 풀이
# 정답 판정은 받았지만 불필요한 부분이 많다.
def solution(tickets):
  answer = []
  tickets.sort(key=lambda x: x[1])

  def covert_course_to_list(course):
    result = []
    interval = 3
    for i in range(len(course) // interval):
      result.append(course[i * interval:i * interval + interval])

    return result

  def dfs(start, course, used_ticket):

    if len(used_ticket) == len(tickets):
      answer.append(covert_course_to_list(course))
      return

    for i in range(len(tickets)):
      if start == tickets[i][0] and i not in used_ticket:
        used_ticket.add(i)
        course += tickets[i][1]
        dfs(tickets[i][1], course, used_ticket)
        course = course[:-3]
        used_ticket.remove(i)

  dfs("ICN", "ICN", set())
  return answer[0]


print(solution([["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]))
print(
    solution([["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"],
              ["ATL", "SFO"]]))


# 다른 풀이
# 모든 경우를 구하는 과정에서 티켓 사용 여부를 관리하는 used 집합을 이용해서 해결
def solution(tickets):
  answer = []

  def dfs(airport, path, used):
    if len(path) == len(tickets) + 1:
      answer.append(path)
      return

    for idx, ticket in enumerate(tickets):
      if airport == ticket[0] and idx not in used:
        used.add(idx)
        dfs(ticket[1], path + [ticket[1]], used)
        used.remove(idx)

  dfs("ICN", ["ICN"], set())

  answer.sort()

  return answer[0]


# 오답 코드 1
# dfs 함수에서 경로 값 (course)를 넘기는 과정에서 똑같은 주소의 list를 재귀함수의 인자 값으로 넘기고 함수 내에서 course를 변경하는 로직이 포함되어 있어 answer에 담긴 course 값들이 마음대로 바뀌는 문제 발생
def solution(tickets):
  answer = []
  tickets.sort(key=lambda x: x[1])

  def dfs(start, course, used_ticket):

    if len(used_ticket) == len(tickets):
      answer.append(course)
      print(answer)
      return

    for a, b in tickets:
      if start == a and [a, b] not in used_ticket:
        used_ticket.append([a, b])
        course.append(b)
        dfs(b, course, used_ticket)
        print("answer : ", answer)
        course.pop()
        used_ticket.pop()

  dfs("ICN", ["ICN"], [])
  return answer


print(solution([["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]))


# 오답 코드 2
# 모든 경우를 고려하지 않은 코드
def solution(tickets):
  answer = ["ICN"]
  tickets.sort(key=lambda x: x[1])
  used_ticket = []

  def dfs(start):

    if len(used_ticket) == len(tickets):
      return

    for ticket in tickets:
      if start == ticket[0] and ticket not in used_ticket:
        used_ticket.append(ticket)
        answer.append(ticket[1])
        dfs(ticket[1])

  dfs("ICN")
  return answer


print(solution([["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]))
print(
    solution([["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"],
              ["ATL", "SFO"]]))
