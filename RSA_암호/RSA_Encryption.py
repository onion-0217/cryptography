from RSA_암호.mapping_list import char_to_num
#n = 10000000002200000000057
#e = 65537
#d = 2106748859844271175069
#p = 100000000003
#q = 100000000019
#Security is a Process, not a Product

UNIT = 1
char_to_num_last = char_to_num['Z']
#단위를 맞추기 위한 의미없는 값
padding_char = char_to_num[' ']

sentence_origin = input("🤖 문장을 입력해주세요, 문장부호는 사용을 금합니다.\n")
n = int(input("🤖 암호화하기 위한 n값과 e값을 입력해주세요\nn: "))
e = int(input("e: "))

sentence_char_to_num = []
#문자 -> 숫자
for i in range(0, len(sentence_origin)):
    sentence_char_to_num.append(char_to_num[sentence_origin[i]])

#n의 크기에 따른 보안성 변화
if n < int(f'{char_to_num_last * 2}'):
    cryp_unit_size = UNIT
elif n < int(f'{char_to_num_last * 3}'):
    cryp_unit_size = 2 * UNIT
elif n < int(f'{char_to_num_last * 4}'):
    cryp_unit_size = 3 * UNIT
elif n < int(f'{char_to_num_last * 5}'):
    cryp_unit_size = 4 * UNIT
else:
    cryp_unit_size = 5 * UNIT

#숫자를 단위묶음으로 묶기
cryp_block = []
for i in range(0, len(sentence_char_to_num), cryp_unit_size):
    #파이썬은 인덱싱 에러발생에 대해 관대함을 확인
    chunk = sentence_char_to_num[i : i + cryp_unit_size]

    if len(chunk) < cryp_unit_size:
        for i in range(0, cryp_unit_size - len(chunk)):
            chunk.append(padding_char)

    chunk = "".join(chunk)
    cryp_block.append(chunk)

#단위묶음을 암호화하는 작업
for i in range(0, len(cryp_block)):
    calcul_var = cryp_block[i]
    cryp_int = pow(int(calcul_var), e, n)
    cryp_block[i] = str(cryp_int).zfill(len(str(n)))

cryp_block = "".join(cryp_block)
print(f'🤖문장 암호의 결과입니다.\nRESULT: {cryp_block}')
