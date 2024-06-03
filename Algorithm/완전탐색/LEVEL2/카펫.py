# 나의 풀이
import math


def solution(brown, yellow):
    answer = []
    candidates = []
    for i in range(1, int(math.sqrt(yellow) + 1)):
        if yellow % i == 0:
            candidates.append((i, yellow // i))

    for h, w in candidates:
        if (h + w + 2) * 2 == brown:
            answer.append(w + 2)
            answer.append(h + 2)

    answer.sort(reverse=True)
    return answer


print(solution(10, 2))
print(solution(8, 1))
print(solution(24, 24))
