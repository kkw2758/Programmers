# 나의 풀이 1 - 시간초과
def solution(numbers):
  answer = []

  def find_bigger_number(target, li):
    if not li:
      return -1

    for i in li:
      if i > target:
        return i
    return -1

  for idx, number in enumerate(numbers):
    answer.append(find_bigger_number(number, numbers[idx + 1:]))
  return answer


print(solution([2, 3, 3, 5]))
print(solution([9, 1, 5, 3, 6, 2]))

# 딕셔너리 자료형을 사용할까? -> numbers의 멤버를 key로 잡았을때 numbers 배열에 중복된 숫자가 올 수 있으므로 value 값을 설정하기가 애매함...

# 정렬? -> 정렬을 하면 numbers 배열의 순서가 보장되지 않으므로 불가능

# upper_bound? -> 현재 순회중인 number 를 제외한 배열의 값이 정렬되어 있다는 보장이 없음.


# 참고 풀이
def solution(numbers):
  stack = []
  answer = [-1] * len(numbers)

  for i in range(len(numbers)):
    while stack and numbers[stack[-1]] < numbers[i]:
      answer[stack.pop()] = numbers[i]
    stack.append(i)

  return answer


print(solution([2, 3, 3, 5]))
print(solution([9, 1, 5, 3, 6, 2]))
