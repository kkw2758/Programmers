# 시간 초과
def solution(players, callings):
  for calling in callings:
    target_idx = find_idx(players, calling)
    players[target_idx], players[target_idx -
                                 1] = players[target_idx -
                                              1], players[target_idx]
  return players

def find_idx(players, calling):
  for idx in range(len(players)):
    if players[idx] == calling:
      return idx
  return -1

## 다른 풀이


def solution(players, callings):
  rank_info = {}
  player_info = {}
  for rank, player in enumerate(players):
    player_info[player] = rank
    rank_info[rank] = player

  for calling in callings:
    rank = player_info[calling]
    front_rank = rank - 1
    front_player = rank_info[front_rank]
    player_info[calling], player_info[front_player] = player_info[
        front_player], player_info[calling]
    rank_info[rank], rank_info[front_rank] = rank_info[front_rank], rank_info[rank]

  result = []
  for name, rank in sorted(list(player_info.items()), key=lambda x: x[1]):
    result.append(name)
  return result


print(
    solution(["mumu", "soe", "poe", "kai", "mine"],
             ["kai", "kai", "mine", "mine"]))
