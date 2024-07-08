def solution(name, yearning, photo):
  answer = []
  yearning_dict = dict()
  for i in range(len(name)):
    yearning_dict[name[i]] = yearning[i]

  for members in photo:
    result = 0
    for name in members:
      if name in yearning_dict:
        result += yearning_dict[name]
    answer.append(result)
  return answer


print(
    solution(["may", "kein", "kain", "radi"], [5, 10, 1, 3],
             [["may", "kein", "kain", "radi"], ["may", "kein", "brin", "deny"],
              ["kon", "kain", "may", "coni"]]))
