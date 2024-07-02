def solution(bandage, health, attacks):
  answer = 0
  chain = 0
  max_health = health
  for time in range(1, attacks[-1][0] + 1):
    # 공격 예정
    if attacks and attacks[0][0] == time:
      attack_info = attacks.pop(0)
      health -= attack_info[1]
      # 캐릭터 사망
      if health <= 0:
        return -1
      chain = 0
    else:
      chain += 1
      health += bandage[1]
      # 추가 회복
      if chain == bandage[0]:
        health += bandage[2]
        chain = 0

      if health > max_health:
        health = max_health
    # print("time : {}".format(time))
    # print("health : {}".format(health))

  return health


solution([5, 1, 5], 30, [[2, 10], [9, 15], [10, 5], [11, 5]])
