with open("text.txt", 'r') as file:  # Открываем файл, выдав имя file
    stringg = file.read()  # Получаем строку
words = stringg.split()  # Разделяем ее на слова, записав в список
print(f'Количество слов в файле "text.txt" {len(words)}')  # Выдаем сообщение с количеством слов
