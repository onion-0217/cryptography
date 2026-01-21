import ECC_Key as ek
import random

if __name__ == "__main__":
    print("🤖공개키를 입력받겠습니다!")
    ECC_field = int(input(f"🤖체(Field) 값을 알려주세요.\nF: "))
    ECC_a = int(input(f"\n🤖y^2 = x^3 + ax + b에서 a값과 b값을 알려주세요.\na: "))
    ECC_b = int(input(f"b: "))
    print(f"\n🤖P의 좌표를 알려주세요.")
    ECC_P_x = int(input(f"x좌표: "))
    ECC_P_y = int(input(f"y좌표: "))

    ECC_alpha = int(input(f"\n🤖비밀키를 입력받겠습니다!"
                          f"\n🔒정수값을 하나 알려주세요.\n비밀키: "))

    print(f"\n🤖수신자에게 보낼 평문의 좌표를 알려주세요.")
    ECC_M_x = int(input(f"x좌표: "))
    ECC_M_y = int(input(f"y좌표: "))

    ECC_Q = ek.find_np(ECC_field, ECC_alpha, ECC_a, ECC_P_x, ECC_P_y)
    ECC_random_k = random.randint(1, 10)
    ECC_kQ_x, ECC_kQ_y = ek.find_np(ECC_field, ECC_random_k, ECC_a,ECC_Q[0], ECC_Q[1])

    C1 = ek.find_np(ECC_field, ECC_random_k, ECC_a, ECC_P_x, ECC_P_y)
    C2 = ek.find_np_sum_p(ECC_field, ECC_a, ECC_kQ_x, ECC_kQ_y, ECC_M_x, ECC_M_y)

    print(f"🤖암호문 생성중...")

    print(f"\n암호문이 생성되었습니다!\n🤖수신자에게 암호문 ({C1}, {C2})를 보내세요.")