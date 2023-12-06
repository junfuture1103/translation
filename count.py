def sum_msgid_characters(txt_file_path):
    with open(txt_file_path, 'r', encoding='utf-8') as txt_file:
        lines = txt_file.readlines()

    total_char_count = 0

    for line in lines:
        if line.startswith('msgid'):
            msgid = line.strip().split('msgid ')[1].strip('"')
            char_count = len(msgid)
            total_char_count += char_count

    print(f"Total length of all msgid: {total_char_count}")

# Usage
txt_file_path = 'your_output_folder\output_section_2.txt'
sum_msgid_characters(txt_file_path)