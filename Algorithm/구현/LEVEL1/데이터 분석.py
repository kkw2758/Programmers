def solution(data, ext, val_ext, sort_by):
  flag_dict = {}
  for idx, flag in enumerate(["code", "date", "maximum", "remain"]):
    flag_dict[flag] = idx
  data = [d for d in data if val_ext > d[flag_dict[ext]]]
  data.sort(key=lambda x: x[flag_dict[sort_by]])
  return data
