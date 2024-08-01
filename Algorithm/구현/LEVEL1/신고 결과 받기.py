def solution(id_list, report, k):
  answer = []
  user_idx = {}
  # 신고 받은 카운트 수
  singo_count = [0] * len(id_list)
  # 유저별 신고한 목록
  singo_info = [set() for _ in range(len(id_list))]
  # 정지당한 유저 목록
  vanced_user = []

  for idx, id in enumerate(id_list):
    user_idx[id] = idx

  for from_user_id, to_user_id in map(lambda x: x.split(), report):
    if to_user_id not in singo_info[user_idx[from_user_id]]:
      singo_count[user_idx[to_user_id]] += 1
      singo_info[user_idx[from_user_id]].add(to_user_id)

  for idx, cnt in enumerate(singo_count):
    if cnt >= k:
      vanced_user.append(id_list[idx])

  for idx, singo_users in enumerate(singo_info):
    mail_cnt = 0
    for singo_user in singo_users:
      if singo_user in vanced_user:
        mail_cnt += 1
    answer.append(mail_cnt)

  return answer


print(
    solution(
        ["muzi", "frodo", "apeach", "neo"],
        ["muzi frodo", "apeach frodo", "frodo neo", "muzi neo", "apeach muzi"],
        2))

print(
    solution(["con", "ryan"], ["ryan con", "ryan con", "ryan con", "ryan con"],
             3))
