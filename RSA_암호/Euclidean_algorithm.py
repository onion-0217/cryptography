def euclidean_algorithm(left, right):
    result_left = left
    result_right = right
    while True:
        result_left = result_left % result_right
        if result_left == 0:
            return result_right
        result_right = result_right % result_left
        if result_right == 0:
            return result_left
if __name__ == '__main__':
    print("******두 수의 최대공약수를 찾는 프로그램입니다******")
    dividend = int(input('첫 번째 수를 입력해주세요\n1️⃣: '))
    divisor = int(input('두 번째 수를 입력해주세요\n2️⃣: '))

    #편의상 나누는 수를 더 작게 만들었습니다.
    if dividend < divisor:
        swap = dividend
        dividend = divisor
        divisor = swap

    if dividend != divisor:
        print(f"😎두 수의 최대공약수는 {euclidean_algorithm(dividend, divisor)}입니다.")

    else:
        print(f"😎두 수의 최대공약수는 {dividend}입니다.")