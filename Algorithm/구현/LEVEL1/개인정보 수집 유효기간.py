# 나의 풀이 1
def solution(today, terms, privacies):
  answer = []

  def add_month(today, month):
    t_year, t_month, t_day = map(int, today.split("."))

    if (t_month + month) % 12 == 0 and (t_month + month) // 12 != 0:
      after_year = str(t_year + (t_month + month) // 12 - 1)
    else:
      after_year = str(t_year + (t_month + month) // 12)

    after_month = (t_month + month) % 12
    if after_month == 0:
      after_month = 12
    after_month = str(after_month).zfill(2)
    after_day = str(t_day).zfill(2)
    return ".".join([after_year, after_month, after_day])

  term_type = {}
  for term in terms:
    type, month = term.split()
    term_type[type] = int(month)

  for idx, privacy in enumerate(privacies):
    day, type = privacy.split()
    if add_month(day, term_type[type]) <= today:
      answer.append(idx + 1)
  return answer


# 나의 풀이 2
def solution(today, terms, privacies):
  answer = []

  def convert_day(today):
    t_year, t_month, t_day = map(int, today.split("."))
    day = t_year * 12 * 28 + t_month * 28 + t_day
    return day

  today = convert_day(today)

  term_type = {}
  for term in terms:
    type, month = term.split()
    term_type[type] = int(month) * 28

  for index, privacy in enumerate(privacies):
    day, type = privacy.split()
    if convert_day(day) + term_type[type] <= today:
      answer.append(index + 1)

  return answer
