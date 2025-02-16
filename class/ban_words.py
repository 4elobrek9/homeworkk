def load_reserved_words(filename):
    """Загружает зарезервированные слова из файла."""
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            return [line.strip() for line in file if line.strip()]
    except FileNotFoundError:
        print(f"Файл '{filename}' не найден.")
        return []

def replace_reserved_words(text, reserved_words, prefixes):
    """Заменяет зарезервированные слова и слова с приставками на символы '#'."""
    words = text.split()
    replaced_words = []
    for word in words:
        if word in reserved_words or any(word.startswith(prefix) for prefix in prefixes):
            replaced_words.append('#' * len(word))
        else:
            replaced_words.append(word)
    return ' '.join(replaced_words)

def main():
    # Запрос ввода от пользователя
    text_input = input("Введите текст: ")

    # Загрузка зарезервированных слов из файла
    reserved_words = load_reserved_words('C:/Users/Student2-4/homeworkk/class/matword.txt')

    # Заданные приставки
    prefixes = ['ХУЕ-', 'ХУЁ-', 'ХУЙ-', 'ХУЮ-', 'ХУЯ-', 'ПИЗДА-', 'ПИЗДО-']

    # Получаем измененный текст
    modified_text = replace_reserved_words(text_input, reserved_words, prefixes)

    # Выводим измененный текст
    print("\nИзмененный текст:")
    print(modified_text)

if __name__ == "__main__":
    main()
