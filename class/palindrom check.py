def is_palindrome(s):

    cleaned = ''.join(s.split()).lower()

    return cleaned == cleaned[::-1]


user_input = input("Введите строку: ")


if is_palindrome(user_input):
    print("Введенная строка является палиндромом.")
else:
    print("Введенная строка не является палиндромом.")
