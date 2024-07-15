def solution(keymap, targets):
  answer = []
  min_count = {}
  for key_info in keymap:
    for i, key in enumerate(key_info):
      if key in min_count:
        min_count[key] = min(min_count[key], i + 1)
      else:
        min_count[key] = i + 1

  for target in targets:
    count = 0
    for key in target:
      if key not in min_count:
        count = -1
        break
      count += min_count[key]
    answer.append(count)
  return answer


print(solution(["ABACD", "BCEFD"], ["ABCD", "AABB"]))
print(solution(["AA"], ["B"]))
print(solution(["AGZ", "BSSS"], ["ASA", "BGZ"]))
