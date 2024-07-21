# https://magentino.tistory.com/71
def time_convert(string):
  h, m = map(int, string.split(":"))
  return h * 60 + m


def solution(book_time):
  answer = 0
  check_change_list = list()
  for start, end in book_time:
    check_change_list.append((time_convert(start), 1))
    check_change_list.append((time_convert(end) + 10, 0))

  check_change_list.sort()
  print(check_change_list)
  tmp = 0
  for t, chk in check_change_list:
    if chk == 1:
      tmp += 1
    elif chk == 0:
      tmp -= 1
    answer = max(answer, tmp)
  return answer


print(
    solution(([["15:00", "17:00"], ["16:40", "18:20"], ["14:20", "15:20"],
               ["14:10", "19:20"], ["18:20", "21:20"]])))


def plus_10_minute(time):
  hour, minute = map(int, time.split(':'))
  if (minute + 10) >= 60:
    hour += 1
    minute = (minute + 10) % 60
  else:
    minute += 10

  return ':'.join([str(hour).zfill(2), str(minute).zfill(2)])


def solution(book_time):
  answer = 0
  check_change_list = list()
  for start, end in book_time:
    check_change_list.append((start, 1))
    check_change_list.append((plus_10_minute(end), 0))

  check_change_list.sort()
  tmp = 0
  for t, chk in check_change_list:
    if chk == 1:
      tmp += 1
    elif chk == 0:
      tmp -= 1
    answer = max(answer, tmp)
  return answer


print(
    solution(([["15:00", "17:00"], ["16:40", "18:20"], ["14:20", "15:20"],
               ["14:10", "19:20"], ["18:20", "21:20"]])))

print(solution([["09:10", "10:10"], ["10:20", "12:20"]]))


# https://sanghui48.tistory.com/58
def convert_minute(time):
  return int(time[:2]) * 60 + int(time[-2:])


def solution(book_time):
  dic = {}
  for book in book_time:
    st = convert_minute(book[0])
    en = convert_minute(book[1])
    for t in range(st, en + 10):
      if dic.get(t) == None:
        dic[t] = 1
      else:
        dic[t] += 1
  return max(dic.values())


print(
    solution(([["15:00", "17:00"], ["16:40", "18:20"], ["14:20", "15:20"],
               ["14:10", "19:20"], ["18:20", "21:20"]])))

print(solution([["09:10", "10:10"], ["10:20", "12:20"]]))
