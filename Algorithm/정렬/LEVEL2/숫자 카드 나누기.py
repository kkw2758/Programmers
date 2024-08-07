def solution(arrayA, arrayB):
    arrayA = list(set(arrayA))
    arrayB = list(set(arrayB))
    answer = []

    def get_divisors(number):
        result = []
        for i in range(1, int(number**0.5) + 1):
            if number % i == 0:
                result.append(i)
                if i**2 != number:
                    result.append(number // i)
        return result

    def get_common_divisors(divisors, members):
        result = []
        for divisor in divisors:
            for member in members:
                if member % divisor:
                    break
            else:
                result.append(divisor)
        return result

    def is_member_divied_by_divisor(divisor, members):
        for member in members:
            if member % divisor == 0:
                return True
        return False

    divisors = get_divisors(min(arrayA))
    common_divisors = get_common_divisors(divisors, arrayA)
    common_divisors.sort(reverse=True)
    for common_divisor in common_divisors:
        if not is_member_divied_by_divisor(common_divisor, arrayB):
            answer.append(common_divisor)
            break

    divisors = get_divisors(min(arrayB))
    common_divisors = get_common_divisors(divisors, arrayB)
    common_divisors.sort(reverse=True)
    for common_divisor in common_divisors:
        if not is_member_divied_by_divisor(common_divisor, arrayA):
            answer.append(common_divisor)
            break

    
    if answer:
        return max(answer)
    else:
        return 0


print(solution([14, 35, 119], [18, 30, 102]))
print(solution([3], [7]))
