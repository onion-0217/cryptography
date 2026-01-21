import ECC_Key as ek

if __name__ == "__main__":
    print(f"\n🤖수신받은 C1, C2의 좌표를 알려주세요")
    print(f"\n🤖C1의 좌표")
    ECC_C1_x = int(input(f"x좌표: "))
    ECC_C1_y = int(input(f"y좌표: "))
    print(f"\n🤖C2의 좌표")
    ECC_C2_x = int(input(f"x좌표: "))
    ECC_C2_y = int(input(f"y좌표: "))

    ECC_field = int(input(f"\n🤖해독을 위해 체(Field) 값을 알려주세요.\nF: "))
    ECC_a = int(input(f"🤖y^2 = x^3 + ax + b에서 a값을 알려주세요.\na: "))
    ECC_alpha = int(input(f"\n🗝️비밀 키를 알려주세요\n비밀 키: "))

    print(f"\n🤖복호화 진행 중...")

    Shared_Secret = ek.find_np(ECC_field, ECC_alpha, ECC_a, ECC_C1_x, ECC_C1_y)
    print(f"🔑복구된 공유 비밀(S): {Shared_Secret}")

    Minus_S_x = Shared_Secret[0]
    Minus_S_y = (-Shared_Secret[1]) % ECC_field

    Decrypted_M = ek.find_np_sum_p(ECC_field, ECC_a, ECC_C2_x, ECC_C2_y, Minus_S_x, Minus_S_y)

    print(f"\n😎복호화 완료!")
    print(f"🤖원래 평문의 좌표는 {Decrypted_M} 입니다.")