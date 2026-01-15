import Euclidean_algorithm as ea
import sys
#첫 번째 소수와 두 번째 소수, 그리고 RSA_key(d)값은 개인이 보관한다.
#Euler_n값, 그리고 그와 서로소인 e값은 공개한다.
#🔒로 공개하면 안되는 수를 표시해두었다.
prime_n1 = int(input("🔒첫 번째 소수 입력\n1️⃣: "))
for i in range(2, prime_n1):
    if ea.euclidean_algorithm(prime_n1, i) != 1:
        print("💣소수가 아니에요!")
        sys.exit()

prime_n2 = int(input("🔒두 번째 소수 입력\n2️⃣: "))
for i in range(2, prime_n2):
    if ea.euclidean_algorithm(prime_n2, i) != 1:
        print(".💣소수가 아니에요!")
        sys.exit()

#오일러함수 값 생성기
Euler_n = (prime_n1 - 1) * (prime_n2 - 1)

#서로소 추천값 생성
recommend_number = []
for i in range(2, Euler_n):
    if ea.euclidean_algorithm(Euler_n, i) == 1:
        recommend_number.append(i)

    #메모리 절약
    if len(recommend_number) > 10:
        break

#서로소 입력 받기(e)
Euler_e = int(input(f"{Euler_n} 값과 서로소인 수 입력"
                    f"\n😊추천: {recommend_number[1]}, {recommend_number[3]}, {recommend_number[5]}..."
                    f"\n🗝️: "))

if ea.euclidean_algorithm(Euler_n, Euler_e) != 1:
    print("💣서로소가 아니에요!")
    sys.exit()
#RSA값 생성 완료
RSA_key = ea.euclidean_algorithm_2(Euler_n, Euler_e) % Euler_n
print(f"당신의 RSA_KEY는...\n🔒 {RSA_key}입니다. 타인에게 알리지 마세요.")
###################################################################################################################