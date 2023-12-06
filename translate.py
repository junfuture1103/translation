from google.cloud import translate_v2 as translate

def translate_text(client, text, target_language='ko'):
    result = client.translate(text, target_language=target_language)
    return result['translatedText']

def process_txt_file(input_txt_path, output_txt_path):
    with open(input_txt_path, 'r', encoding='utf-8') as txt_file:
        lines = txt_file.readlines()

    translated_lines = []

    # Initialize Google Translate client
    client = translate.Client()

    for line in lines:
        if line.startswith('msgid'):
            msgid = line.strip().split('msgid ')[1].strip('"')
            translated_text = translate_text(client, msgid)
            translated_line = f'msgid "{msgid}"\nmsgstr "{translated_text}"\n\n'
            translated_lines.append(translated_line)
        else:
            translated_lines.append(line)

    with open(output_txt_path, 'w', encoding='utf-8') as output_file:
        output_file.writelines(translated_lines)
# Usage
po_file_path = 'output_txt_file.txt'
output_po_file_path = 'translated_txt_file.txt'
process_txt_file(po_file_path, output_po_file_path)
