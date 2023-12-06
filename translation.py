import re
import requests
import json
import time
import copy

MY_CLIENT_ID = 'HI816N1RXAs_KzBrITkP'
MY_CLIENT_SECRET = 'oiGynjvFwR'

CLIENT_ID, CLIENT_SECRET = MY_CLIENT_ID, MY_CLIENT_SECRET

def extract_empty_msgstr(po_file_path):
    with open(po_file_path, 'r', encoding='utf-8') as po_file:
        po_content = po_file.read()

    # 각 엔트리를 추출
    entries = po_content.split('\n\n')
        
    modified_lines = []

    for entry in entries:
        lines = entry.strip().split('\n')
        parsed_en_line = None
        
        for line in lines:
            result_line = line

            match_msgid = re.search(r'msgid "(.*?)"', line)
            match_msgstr = re.search(r'msgstr "(.*?)"', line)
            
            if match_msgid:
                parsed_en_line = match_msgid.group(1)
                    
                result = ""

                if parsed_en_line:
                    result_kor_line = papago_translate(parsed_en_line)
                    
                    # msgstr이 이미 존재하면 기존 값을 유지하고, 없다면 새로 번역 값을 추가
                    if match_msgstr:
                        result += f'msgstr "{match_msgstr.group(1)}"\n'
                        #print(f'msgstr "{match_msgstr.group(1)}"\n')  # 추가된 msgstr 출력
                    else:
                        result += f'msgstr "{result_kor_line}"\n'
                        #print(f'msgstr "{result_kor_line}"\n')  # 추가된 msgstr 
                    
                    result_line=line
            
            modified_lines.append(result_line)
    
    with open('result.txt', 'w') as result_file:
        result_file.writelines(modified_lines)
                    
                        

def papago_translate(text):
    url = 'https://openapi.naver.com/v1/papago/n2mt'
    headers = {
        'Content-Type': 'application/json',
        'X-Naver-Client-Id': CLIENT_ID,
        'X-Naver-Client-Secret': CLIENT_SECRET
    }
    data = {'source': 'en', 'target': 'ko', 'text': text}
    
    if(text == None):
        return "error"

    # post 방식으로 서버 쪽으로 요청
    response = requests.post(url, json.dumps(data), headers=headers) 
    # print(response)   # status code : response 200번대가 나오면 성공, 400번대는 실패

    try:
        result_text = response.json()['message']['result']['translatedText']
        
    except Exception as e:
        result_text = "error"
        # print(f"An error occurred: {e}")
    
    return result_text


def main():
    po_file_path = 'output_txt_file.txt'
    extract_empty_msgstr(po_file_path)

if __name__ == "__main__":
    main()