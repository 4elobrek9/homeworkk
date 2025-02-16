def count_sentences(text):
    # Разделяем текст на предложения по знакам препинания
    sentences = [sentence for sentence in text.split('.') if sentence]
    # Убираем пустые строки и считаем количество предложений
    return len([s for s in sentences if s.strip()])

# Запрос ввода от пользователя
text_input = input("Введите текст: ")

# Подсчет количества предложений
sentence_count = count_sentences(text_input)

# Вывод результата
print(f"\nКоличество предложений в тексте: {sentence_count}")
