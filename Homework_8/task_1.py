# Напишите функцию, которая получает на вход директорию и рекурсивно обходит её и все вложенные директории. 
# Результаты обхода сохраните в файлы json, csv и pickle.
# Для дочерних объектов указывайте родительскую директорию.
# Для каждого объекта укажите файл это или директория.
# Для файлов сохраните его размер в байтах, 
# а для директорий размер файлов в ней с учётом всех вложенных файлов и директорий. 

import os
import json
import csv
import pickle


def write_json_csv_pickle(directory):
    # рекурсивный обход директории и всех вложенных директорий
    result_dict_json = {}
    directory_info = []

    for dir_path, dir_file, file_name in os.walk(directory):
        size = sum([os.path.getsize(os.path.join(dir_path, name)) for name in file_name])

        result_dict_json[f'Directory: {dir_path} = {size} bytes'] = [
            f'FILE: {file} = {os.path.getsize(os.path.join(dir_path, file))} bytes' for file in file_name]

        directory_info.append({
            'Type': 'Directory',
            'Parent Directory': dir_path,
            'Name': file_name,
            'Size': size
        })

        for file in file_name:
            file_path = os.path.join(dir_path, file)
            file_size = os.path.getsize(file_path)

            directory_info.append({
                    'Type': 'File',
                    'Parent Directory': dir_path,
                    'Name': file,
                    'Size': file_size
            })
    
    # запись в JSON
    with open('directory_info.json', 'w', encoding='utf-8') as json_file:
        json.dump(result_dict_json, json_file, indent=4)

    # запись в  CSV
    with open('directory_info.csv', 'w', encoding='utf-8') as csv_file:
        fieldnames = ['Type', 'Parent Directory', 'Name', 'Size']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(directory_info)    

    # запись в PICKLE
    with open('pickle_file.bin', 'wb') as pickle_file:
        pickle.dump(result_dict_json, pickle_file)

write_json_csv_pickle('/Users/vladislav/Desktop/Masha/GB/Python_3/Lesson_8/')



