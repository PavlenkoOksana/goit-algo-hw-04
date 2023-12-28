import random
import timeit

def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    return merge(merge_sort(left_half), merge_sort(right_half))

def merge(left, right):
    merged = []
    left_index = 0
    right_index = 0

    while left_index < len(left) and right_index < len(right):
        if left[left_index] <= right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1

    while left_index < len(left):
        merged.append(left[left_index])
        left_index += 1

    while right_index < len(right):
        merged.append(right[right_index])
        right_index += 1

    return merged


def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]  
        j = i-1
        while j >=0 and key < arr[j] :
                arr[j+1] = arr[j]
                j -= 1
        arr[j+1] = key 
    return arr    


def sort_data(arr):
    return sorted(arr.copy())

def test_sorting_algorithm(algorithm, data):
    def sort_data():
        return algorithm(data.copy())

    return timeit.timeit(sort_data, number=1)


def main():
    # Генерація різних наборів тестових даних
    data_sizes = [1000, 5000, 10000, 50000]
    for size in data_sizes:
        data = [random.randint(0, size) for _ in range(size)]

        # Вимірювання часу виконання для кожного алгоритму
        merge_sort_time = test_sorting_algorithm(merge_sort, data)
        insertion_sort_time = test_sorting_algorithm(insertion_sort, data)
        timsort_time = test_sorting_algorithm(sort_data, data)

        print(f"Порівняльний аналіз 3-х алгоритмів за часом виконання шляхом їх тестування на масиві розміром {size} елементів:\n")
        print(f"Сортування злиттям: {merge_sort_time} сек.")
        print(f"Сортування вставками: {insertion_sort_time} сек.")
        print(f"Сортування Timsort: {timsort_time} сек.")
        print("----------------------------------------\n")


if __name__ == "__main__":
    main()