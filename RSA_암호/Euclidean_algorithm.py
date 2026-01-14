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

#ed = 1 (mod Euler_n)에서의 d값 찾기_구조, 역원 찾기
#주로 Euler_n, e의 순서로 인수를 받을 예정임
def euclidean_algorithm_2(left, right):
    #서로소 계산을 위한 몫 저장
    calculate_data = []

    while True:
        result_left = left // right
        calculate_data.append(result_left)
        left = left % right
        if left == 0:
            return inverse_element_algorithm(calculate_data)

        result_right = right // left
        calculate_data.append(result_right)
        right = right % left
        if right == 0:
            return inverse_element_algorithm(calculate_data)

#몫들을 이용하여 ed의 d값 찾기 알고리즘
def inverse_element_algorithm(data):
    default_data = [0,1]
    for i in range(0, int(len(data)) - 1):
        result = default_data[i] - (int(data[i]) * default_data[i + 1])
        default_data.append(result)

    return default_data[len(default_data) - 1]


if __name__ == '__main__':
    print("******수의 역원을 찾는 문제입니다.******")
    dividend = int(input('나눠지는 값을 입력해주세요\n1️⃣: '))
    divisor = int(input('나누는 값을 입력해주세요\n2️⃣: '))

    #편의상 나누는 수를 더 작게 만들었습니다.
    if dividend < divisor:
        swap = dividend
        dividend = divisor
        divisor = swap

    if dividend != divisor:
        print(f"😎나눠지는 값의 역원은 {euclidean_algorithm_2(dividend, divisor)}입니다.")
