import json

# Читаем данные из файла с текущей кодировкой
with open('data.json', 'r', encoding='utf-16') as file:
    data = file.read()

# Парсим JSON
json_data = json.loads(data)

# Перезаписываем файл с указанной кодировкой (например, UTF-8)
with open('data_utf8.json', 'w', encoding='utf-8') as file:
    json.dump(json_data, file, ensure_ascii=False, indent=2)
