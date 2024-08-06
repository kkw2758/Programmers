import sys
sys.setrecursionlimit(10 ** 6)

def solution(s):

    def recursive(s):
        print(s)
        if not s:
            return 0
        x = s[0]
        same_cnt = 1
        diff_cnt = 0
        for i in range(1, len(s)):
            if x == s[i]:
                same_cnt += 1
            else:
                diff_cnt += 1
            if same_cnt == diff_cnt:
                return 1 + recursive(s[i + 1:])
        return 1

    return recursive(s)



print(solution("a"))
print(solution(""))
