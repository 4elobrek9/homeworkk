def get_grades():
    print("Введите 10 оценок студента (от 1 до 12):")
    grades = []
    for _ in range(10):
        grade = int(input(f"Оценка {len(grades) + 1}: "))
        while grade < 1 or grade > 12:
            print("Оценка должна быть от 1 до 12!")
            grade = int(input(f"Оценка {len(grades) + 1}: "))
        grades.append(grade)
    return grades

def display_grades(grades):
    print("Оценки студента:")
    for i, grade in enumerate(grades, start=1):
        print(f"{i}. {grade}")

def retake_exam(grades):
    print("Пересдача экзамена:")
    index = int(input("Введите номер оценки для пересдачи: "))
    while index < 1 or index > len(grades):
        print("Неверный номер оценки. Попробуйте еще раз.")
        index = int(input("Введите номер оценки для пересдачи: "))
    new_grade = int(input("Введите новую оценку: "))
    while new_grade < 1 or new_grade > 12:
        print("Оценка должна быть от 1 до 12!")
        new_grade = int(input("Введите новую оценку: "))
    grades[index - 1] = new_grade
    print("Оценка успешно изменена.")

def get_scholarship(grades):
    avg_grade = sum(grades) / len(grades)
    if avg_grade >= 10.7:
        print("Стипендия выходит!")
    else:
        print("Стипендия не выходит.")

def sort_grades(grades):
    print("Выберите порядок сортировки:")
    print("1. По возрастанию")
    print("2. По убыванию")
    choice = int(input("Введите номер варианта: "))
    if choice == 1:
        sorted_grades = sorted(grades)
    elif choice == 2:
        sorted_grades = sorted(grades, reverse=True)
    else:
        print("Неверный выбор. Возвращаемся в меню.")
        return grades
    print("Отсортированный список оценок:")
    for i, grade in enumerate(sorted_grades, start=1):
        print(f"{i}. {grade}")
    return sorted_grades

def medium(grades):
    avg = sum(grades) / len(grades)
    print(" ")
    print("Средняя оценка:", avg)
    return avg

def display_menu():
    print("\nМеню:")
    print("1. Вывод оценок")
    print("2. Пересдача экзамена")
    print("3. Выходит ли стипендия")
    print("4. Вывод отсортированного списка оценок")
    print("5. Вывод средней оценки")
    print("0. Выход")

def main():
    grades = get_grades()
    while True:
        display_menu()
        choice = int(input("Выберите действие (0-5): "))
        if choice == 0:
            print("Программа завершена.")
            break
        elif choice == 1:
            display_grades(grades)
        elif choice == 2:
            retake_exam(grades)
        elif choice == 3:
            get_scholarship(grades)
        elif choice == 4:
            grades = sort_grades(grades)
        elif choice == 5:
            medium(grades)
        else:
            print("Неверный выбор. Попробуйте еще раз.")

if __name__ == "__main__":
    main()
