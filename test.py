with open('path_file.txt', 'r') as file:
    lines = file.readlines()

modified_lines = []

for line in lines:
    if line.startswith('msgstr ""'):
        modified_lines.append('msgstr "hello world!"\n')
    else:
        modified_lines.append(line)

with open('result.txt', 'w') as result_file:
    result_file.writelines(modified_lines)
