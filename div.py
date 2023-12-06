import os
import shutil

# 파일 경로 및 폴더 경로를 적절히 변경하세요.
file_path = "output_txt_file.txt"
output_folder = "your_output_folder"

max_chars_per_section = 9000
current_chars = 0
current_section = []
section_count = 1

# 폴더가 없으면 생성
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

with open(file_path, "r", encoding="utf-8") as file:
    for line in file:
        # 새로운 구획이 시작되면 현재까지의 글자 수를 확인하여 새로운 섹션으로 결정합니다.
        if line.startswith("#") and not current_section:
            continue

        current_section.append(line)

        # msgid 라인에서 글자 수를 계산합니다.
        if line.startswith("msgid"):
            current_chars += len(line.split('"')[1])

        # 현재까지의 글자 수가 최대 길이를 초과하면 새로운 섹션으로 나눕니다.
        if current_chars > max_chars_per_section:
            # 현재 섹션에서 다음 섹션에 필요한 글자 수를 미리 계산
            remaining_chars = max_chars_per_section - (current_chars - len(current_section[-1].split('"')[1]))

            # 현재 섹션에서 다음 섹션에 필요한 만큼 추가로 가져옴
            try:
                while remaining_chars > 0:
                    line = next(file)
                    current_section.append(line)
                    remaining_chars -= len(line)
            except StopIteration:
                pass

            output_file_path = f"{output_folder}/output_section_{section_count}.txt"
            with open(output_file_path, "w", encoding="utf-8") as output_file:
                output_file.writelines(current_section[:-1])  # 마지막 줄은 다음 섹션의 첫 줄일 수 있으므로 제외

            # 파일 이동
            shutil.move(output_file_path, output_file_path)

            # 초기화
            current_chars = 0
            current_section = []
            section_count += 1

# 마지막 섹션이 남아 있을 경우 처리합니다.
if current_section:
    output_file_path = f"{output_folder}/output_section_{section_count}.txt"
    with open(output_file_path, "w", encoding="utf-8") as output_file:
        output_file.writelines(current_section)

    # 파일 이동
    shutil.move(output_file_path, output_file_path)
