import ECC_Key as ek

print("🤖공개키를 입력받겠습니다!")
ECC_field = int(input(f"🤖체의 종류를 알려주세요.\nex)11 입력 시 11진수가 기준인 정수 체입니다.\nF: "))
ECC_a = int(input(f"\n🤖y^2 = x^3 + ax + b에서 a값과 b값을 알려주세요.\na: "))
ECC_b = int(input(f"b: "))
print(f"\n🤖P의 좌표를 알려주세요.")
ECC_P_x = int(input(f"x좌표: "))
ECC_P_y = int(input(f"y좌표: "))

ECC_alpha = int(input(f"\n🤖비밀키를 입력받겠습니다!"
                      f"\n🔒정수값을 하나 알려주세요."))

ECC_Q = ek.find_np(ECC_field, ECC_alpha, ECC_a,ECC_P_x, ECC_P_y)

print(f"🤖수신자에게 {ECC_Q}값을 비밀키와 함께 전달해주세요. {ECC_Q}값은 외부유출되어도 괜찮습니다.")

