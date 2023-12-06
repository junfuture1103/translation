with open('extract_result_kor.txt', 'r', encoding='utf-8') as input_file:
    extracted_strings = input_file.readlines()

# 기존 파일 읽기
with open('test_file.txt', 'r', encoding='utf-8') as original_file:
    original_lines = original_file.readlines()

# msgstr 부분에 추출된 문자열 삽입
output_lines = []
for line in original_lines:
    if line.startswith('msgstr ""'):
        # 추출된 문자열이 남아있다면 삽입
        if extracted_strings:
            extracted_string = extracted_strings.pop(0).strip()
            output_lines.append(f'msgstr "{extracted_string}"\n')
        else:
            output_lines.append(line)
    else:
        output_lines.append(line)

# 결과를 새로운 파일에 저장
with open('output_file_with_msgstr.txt', 'w', encoding='utf-8') as output_file:
    output_file.writelines(output_lines)
