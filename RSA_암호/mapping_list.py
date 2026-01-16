char_to_num = {}

# 소문자 (00 ~ 25)
for i in range(26):
    char = chr(ord('a') + i)
    char_to_num[char] = f"{i:02d}"

# 대문자 (30 ~ 55)
for i in range(26):
    char = chr(ord('A') + i)
    char_to_num[char] = str(i + 30)

#26~29 사이 중 마음에 드는 수
char_to_num[' '] = '28'
char_to_num[','] = '29'

#숫자 -> 문자 표
num_to_char = {v: k for k, v in char_to_num.items()}
