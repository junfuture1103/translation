def extract_empty_msgstr(po_file_path, txt_file_path):
    with open(po_file_path, 'r', encoding='utf-8') as po_file:
        po_content = po_file.read()

    # 각 엔트리를 추출
    entries = po_content.split('\n\n')

    # 새로운 .txt 파일 생성
    with open(txt_file_path, 'w', encoding='utf-8') as txt_file:
        for entry in entries:
            lines = entry.strip().split('\n')
            has_empty_msgstr = False

            for line in lines:
                if line.startswith('msgstr ""'):
                    has_empty_msgstr = True
                    break

            if has_empty_msgstr:
                txt_file.write(entry + '\n\n')

# 사용 예시
po_file_path = 'language.txt'
txt_file_path = 'output_txt_file.txt'
extract_empty_msgstr(po_file_path, txt_file_path)
