#n =
#e = 65537
#d =
#p = 900000000041
#q = 900000000047

###DEFAULT VALUE
#decrypt_d = 0
#decrypt_n = 0
#UNIT_len = 6

crypt_sentence = input("👾복호화할 수를 입력해주세요\n")
recommend_number_UNIT = []
for i in range(2, len(crypt_sentence)):
    if len(crypt_sentence[i])%i == 0:
        recommend_number_UNIT.append(i)
UNIT_len = int(input(f"👾몇 글자마다 끊어서 복호화 할지 입력해주세요."
                     f"\n추천: {recommend_number_UNIT[0]}, {recommend_number_UNIT[1]}, {recommend_number_UNIT[2]}, ..."
                     f"\n"))
decrypt_n = int(input("👾n값을 입력해주세요"))
decrypt_d = int(input("👾d값을 입력해주세요"))
decrypt_sentence = ""

decrypt_num = [crypt_sentence[i : i + UNIT_len] for i in range(0, len(crypt_sentence), UNIT_len)]

for i in range(0, len(decrypt_num)):
    calcul_var = decrypt_num[i]
    decrypt_sentence += str(pow(int(calcul_var), decrypt_d, decrypt_n))

result = decrypt_sentence.rstrip()

print(f"👾복호화 결과는...\n{result}\n입니다!")