# 나의 풀이
# 문제에서 주어진 내용을 그대로 구현하였는데 index 만큼 뒤의 알파벳으로 바꾼 결과가 skip 문자열을 포함하고 있는 경우를 고려하지 못하여서 오답 처리된다.
def solution(s, skip, index):
    answer = ''
    for c in s:
        skip_count = 0
        for i in range(1, index + 1):
            if chr((ord(c) + i - 97) % 26 + 97) in skip:
                skip_count += 1
        answer += chr((ord(c) + index + skip_count - 97) % 26 + 97)
    return answer


# 참고 풀이 1
# skip 문자열에 포함된 문자들은 결과 문자열에 포함될 수 없으므로 소문자에서 skip 문자열에 포함된 문자를 제외한 뒤 shift를 진행한다.
def solution(s, skip, index):
    answer = ""
    alpha = "abcdefghijklmnopqrstuvwxyz"
    for i in skip:
        alpha = alpha.replace(i, "")
    for a in s:
        answer += alpha[(alpha.find(a) + index) % len(alpha)]
    return answer


# 참고 풀이 2
# from string import ascii_lowercase를 이용해서 소문자 문자열 따로 만들 필요가 없다.
# 집합 자료형의 차집합을 이용하여 replace 함수를 이용하지 않았다.
# sorted() 함수의 결과값은 정렬된 리스트이다.
from string import ascii_lowercase


def solution(s, skip, index):
    result = ''

    a_to_z = set(ascii_lowercase)
    a_to_z -= set(skip)
    a_to_z = sorted(a_to_z)
    l = len(a_to_z)

    dic_alpha = {alpha: idx for idx, alpha in enumerate(a_to_z)}

    for i in s:
        result += a_to_z[(dic_alpha[i] + index) % l]
    return result
