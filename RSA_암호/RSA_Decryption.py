import mapping_list
#n = 10000000002200000000057
#e = 65537
#d = 2106748859844271175069
#p = 100000000003
#q = 100000000019
#Security is a Process, not a Product


###DEFAULT VALUE
#decrypt_d = 0
#decrypt_n = 0
#UNIT_len = n의 크기
CHAR_LEN = 2 #A B C D 등이 30 31 32 33 2자리 수로 구성되었으므로 2라 적음
UNIT_len = 5 * CHAR_LEN # 10

crypt_sentence = input("👾복호화할 수를 입력해주세요\n")
recommend_number_UNIT = []
for i in range(2, len(crypt_sentence)):
    if len(crypt_sentence)%i == 0:
        recommend_number_UNIT.append(i)
decrypt_n = int(input("👾n값을 입력해주세요\n"))
decrypt_d = int(input("👾d값을 입력해주세요\n"))

n_len = len(str(decrypt_n))

decrypt_sentence = ""
RESULT = ''

decrypt_num = [crypt_sentence[i : i + n_len] for i in range(0, len(crypt_sentence), n_len)]

for i in range(0, len(decrypt_num)):
    calcul_var = decrypt_num[i]

    decrypt_val = pow(int(calcul_var), decrypt_d, decrypt_n)
    decrypt_sentence += str(decrypt_val).zfill(UNIT_len)

for i in range(0, len(decrypt_sentence), CHAR_LEN):
    calcul_var = decrypt_sentence[i : i + CHAR_LEN]
    RESULT += mapping_list.num_to_char[calcul_var]


result = RESULT.rstrip()

print(f"👾복호화 결과는...\n{result}\n입니다!")