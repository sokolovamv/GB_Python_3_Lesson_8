# Вспоминаем задачу 3 из прошлого семинара. 
# Мы сформировали текстовый файл с псевдо именами и произведением чисел.
# Напишите функцию, которая создаёт из созданного ранее файла новый с данными в формате JSON. 
# Имена пишите с большой буквы. 
# Каждую пару сохраняйте с новой строки.

import json

def func_json(file1, file2):
    with open(file1, 'r', encoding='utf-8') as f:
        my_dict = {}
        for line in f:
            new_json = line.replace('\n', '').split('=') 
            my_dict[new_json[0]]=new_json[1] 
    with open(file2, 'w', encoding='utf=8') as f:
        new_json = json.dump(my_dict, f, indent=2, ensure_ascii=False )



if __name__ == '__main__':
    func_json('res.txt', 'new_file.json')