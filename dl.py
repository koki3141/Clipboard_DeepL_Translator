import pyperclip
import re
import requests
import deepl

API_KEY = '' # 自身の API キーを指定


input_string = pyperclip.paste()
output_string  = re.sub(r"\r\n|\r|\n", " ", input_string).replace("  ", " ")

#pyperclip.copy(output_string)

text=output_string
source_lang = 'EN'
target_lang = 'JA'

translator = deepl.Translator(API_KEY)

# 翻訳を実行
try:
    result = translator.translate_text(text, source_lang=source_lang, target_lang=target_lang)
    print(result)
except:
    print('利用制限がかかりました。')
    pyperclip.copy(output_string)
    print(output_string)

