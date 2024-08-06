def solution(number, limit, power):
  answer = 0

  def get_knight_power(number):
    result = 0
    for i in range(1, int(number**0.5) + 1):
      if number % i == 0:
        result += 1
        if i ** 2 != number:
          result += 1

    return result

  
  for i in range(1, number + 1):
    knight_power = get_knight_power(i)
    if knight_power > limit:
      answer += power
    else:
      answer += knight_power
  return answer


print(solution(5, 3, 2))
print(solution(10, 3, 2))
