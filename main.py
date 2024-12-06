# Открываем файл bobr.txt в режиме чтения
with open('bobr.txt', 'r', encoding='utf-8') as file:
    # Читаем содержимое файла
    bobr = file.read()

# Разделяем текст на слова
words = bobr.split()

# Подсчитываем количество слов
word_count = len(words)

# Выводим количество слов
print("Количество слов в файле:", word_count)
