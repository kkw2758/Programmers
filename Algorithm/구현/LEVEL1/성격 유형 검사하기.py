def solution(survey, choices):
  answer = ''
  type_score = {}
  for type in ["R", "T", "C", "F", "J", "M", "A", "N"]:
    type_score[type] = 0

  for i in range(len(survey)):
    type1, type2 = survey[i][0], survey[i][1]
    if choices[i] < 4:
      type_score[type1] += 4 - choices[i]
    elif choices[i] > 4:
      type_score[type2] += choices[i] - 4

  for types in ["RT", "CF", "JM", "AN"]:
    type1, type2 = types[0], types[1]
    if type_score[type1] >= type_score[type2]:
      answer += type1
    else:
      answer += type2

  return answer
