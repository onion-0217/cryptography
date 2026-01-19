import Euclidean_algorithm as ea

#F = Z_??
#y^2 = x^3 + ax + b
#P(x1, y1)
def find_lambda_one_point(field, a, x1, y1):
    return [(3 * pow(x1, 2) + a) % field, (2 * y1) % field]

def find_lambda_two_point(field, x1, y1, x2, y2):
    return [(y2 - y1) % field, (x2 - x1) % field]

#Q = αP, α는 주어진 비밀 키이다. Q를 찾는 방법?
#2P를 구하는 함수식
#field = Z_i에서 i값을 의미함
def find_2p(field, a, x1, y1):
    slope = find_lambda_one_point(field, a, x1, y1)
    dig = slope[0] * ea.euclidean_algorithm_2(slope[1], field)
    x2 = pow(dig, 2) - x1 -x1
    y2 = dig * (x1 - x2) - y1
    x2 %= field
    y2 %= field
    return [x2, y2]

def find_np_sum_p(field, a, x1, y1, x2, y2):
    slope = find_lambda_two_point(field, x1, y1, x2, y2)
    dig = slope[0] * ea.euclidean_algorithm_2(slope[1], field)
    x3 = pow(dig, 2) - x1 -x2
    y3 = dig * (x1 - x3) - y1
    x3 %= field
    y3 %= field
    return [x3, y3]


def find_np(field, alpha, a, x1, y1):
    tx, ty = x1, y1
    result = None

    while alpha > 0:

        if alpha % 2 == 1:
            if result is None:
                result = [tx, ty]
            else:
                result = find_np_sum_p(field, a, result[0], result[1], tx, ty)

        temp_2p = find_2p(field, a, tx, ty)
        tx, ty = temp_2p[0], temp_2p[1]

        alpha //= 2

    return result

if __name__ == '__main__':
    field = int(input("field = "))
    alpha = int(input("alpha = "))
    a = int(input("a = "))
    x1 = int(input("x1 = "))
    y1 = int(input("y1 = "))
    result = find_np(field, alpha, a, x1, y1)
    print(f"결과는 {result}")
