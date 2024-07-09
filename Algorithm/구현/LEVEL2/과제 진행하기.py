def minus(start, end):
  start_hour, start_minute = map(int, start.split(':'))
  end_hour, end_minute = map(int, end.split(':'))
  diff_hour = end_hour - start_hour
  diff_minute = end_minute - start_minute
  if diff_minute < 0:
    diff_hour -= 1
    diff_minute = 60 + diff_minute

  return 60 * diff_hour + diff_minute


def do_waiting_homeworks(time, waiting_homeworks):
  result = []
  if not waiting_homeworks:
    return result
  while time > 0 and waiting_homeworks:
    homework, remain_time = waiting_homeworks.pop()
    if time >= remain_time:
      time -= remain_time
      result.append(homework)
    else:
      remain_time -= time
      time = 0
      waiting_homeworks.append([homework, remain_time])
  return result


def solution(plans):
  answer = []
  # 과제 시작 시간순으로 정렬
  plans.sort(key=lambda x: x[1])
  before = plans[0][1]
  waiting_homeworks = [[plans[0][0], int(plans[0][2])]]
  for i in range(1, len(plans)):
    plan, start, time = plans[i]
    diff_time = minus(before, start)
    before = start
    answer += do_waiting_homeworks(diff_time, waiting_homeworks)
    waiting_homeworks.append([plan, int(time)])

  while waiting_homeworks:
    plan, time = waiting_homeworks.pop()
    answer.append(plan)
  return answer


print(
    solution([["korean", "11:40", "30"], ["english", "12:10", "20"],
              ["math", "12:30", "40"]]))

print(
    solution([["science", "12:40", "50"], ["music", "12:20", "40"],
              ["history", "14:00", "30"], ["computer", "12:30", "100"]]))

print(
    solution([["aaa", "12:00", "20"], ["bbb", "12:10", "30"],
              ["ccc", "12:40", "10"]]))

print(
    solution([["a", "09:00", "30"], ["b", "09:10", "20"], ["c", "09:15", "20"],
              ["d", "09:55", "10"], ["e", "10:50", "5"]]))
