with open('test_file.txt', 'r', encoding='utf-8') as input_file:
    lines = input_file.readlines()

extracted_strings = []

for line in lines:
    # 찾는 문자열이 있는지 확인
    if line.startswith('msgid "'):
        # msgid " 뒤에 이어지는 문자열 추출
        string_value = line.split('"')[1]
        extracted_strings.append(string_value)

# 추출된 문자열을 새로운 파일에 저장
with open('extract_result.txt', 'w', encoding='utf-8') as output_file:
    for string_value in extracted_strings:
        output_file.write(string_value + '\n')
