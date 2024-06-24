# 제약 사항
# numbers의 길이는 1이상 100,000 이하
# 모든 숫자의 경우의 수를 구하는 것은 불가능하다.. -> 완전탐색 불가
# numbers의 원소는 0 이상 1,000 이하 -> 숫자가 엄청 길어질 수도 있다.


# 나의 풀이 - 오답
def solution(numbers):
  answer = ''
  string_numbers = []
  for number in numbers:
    string_numbers.append(str(number))

  string_numbers.sort(reverse=True)

  for string_number in string_numbers:
    answer += string_number
  return answer


print(solution([6, 10, 2]))
print(solution([3, 30, 34, 5, 9]))  # 9 5 34 3 30


# 참고 풀이
def solution(numbers):
  numbers = list(map(str, numbers))

  numbers.sort(reverse=True, key=lambda x: x * 3)

  return str(int("".join(numbers)))


print(solution([6, 10, 2]))
print(solution([3, 30, 34, 5, 9]))  # 9 5 34 3 30
