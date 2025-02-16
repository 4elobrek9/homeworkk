def highlight_reserved_words(text, reserved_words):
    # Разделяем текст на слова
    words = text.split()
    # Изменяем регистр зарезервированных слов на верхний
    highlighted_text = ' '.join([word.upper() if word in reserved_words else word for word in words])
    return highlighted_text

# Запрос ввода от пользователя
text_input = input("Введите текст: ")
reserved_input = input("Введите зарезервированные слова, разделенные запятой: ")

# Преобразуем строку зарезервированных слов в список
reserved_words = [word.strip() for word in reserved_input.split(',')]

# Получаем измененный текст
modified_text = highlight_reserved_words(text_input, reserved_words)

# Выводим измененный текст
print("\nИзмененный текст:")
print(modified_text)
