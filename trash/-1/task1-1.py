def sort_list(lst):
    n = len(lst)
    two_thirds = n * 2 // 3
    one_third = n // 3

    avg = sum(lst) / n
    if avg > 0:
        lst[:two_thirds] = sorted(lst[:two_thirds])
    else:
        lst[:one_third] = sorted(lst[:one_third])

    lst[two_thirds:] = lst[two_thirds:][::-1]
    return lst

def get_input():
    print("Введите элементы списка (через пробел):")
    user_input = input().split()
    return [int(x) for x in user_input]

def main():
    my_list = get_input()
    sorted_list = sort_list(my_list)
    print("Отсортированный список:", sorted_list)

if __name__ == "__main__":
    main()
