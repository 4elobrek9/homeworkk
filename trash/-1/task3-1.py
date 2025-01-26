def enhanced_bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False  # Флаг для отслеживания перестановок
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]  # Перестановка
                swapped = True  # Установить флаг перестановки в True
        if not swapped:  # Если не было перестановок, выходим из цикла
            break
    return arr

# Пример использования
if __name__ == "__main__":
    sample_list = [64, 34, 25, 12, 22, 11, 90]
    sorted_list = enhanced_bubble_sort(sample_list)
    print("Отсортированный список:", sorted_list)