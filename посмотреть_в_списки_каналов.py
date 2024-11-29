import pickle

def pickle_to_text(pickle_file_path, text_file_path):
    try:
        # Открываем файл формата pickle для чтения
        with open(pickle_file_path, 'rb') as pickle_file:
            # Загружаем данные из pickle файла
            data = pickle.load(pickle_file)

        # Открываем текстовый файл для записи
        with open(text_file_path, 'w', encoding='utf-8') as text_file:
            # Записываем данные в текстовый файл
            # Если данные - это строка, просто записываем
            if isinstance(data, str):
                text_file.write(data)
            # Если данные - это список, кортеж или другой итерируемый объект
            elif isinstance(data, (list, tuple)):
                for item in data:
                    text_file.write(f"{item}\n")
            # Если данные - это словарь, записываем ключи и значения
            elif isinstance(data, dict):
                for key, value in data.items():
                    text_file.write(f"{key}: {value}\n")
            else:
                # В случае других типов данных, преобразуем в строку
                text_file.write(str(data))

        print(f"Данные из {pickle_file_path} успешно записаны в {text_file_path}.")

    except Exception as e:
        print(f"Произошла ошибка: {e}")

# Пример использования
pickle_to_text('channels.pickle', 'Источники.txt')
pickle_to_text('channel_mapping.pickle', 'Соответствия.txt')
pickle_to_text('destination_channels.pickle', 'Получатели.txt')





grades = {
    "Alice": [12,24,54],
    "Bob": 90,
    "Charlie": 92
}
values_list = list(grades.values())
print(values_list[0][0])