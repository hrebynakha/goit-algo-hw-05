"""
Завдання 2

Реалізувати двійковий пошук для відсортованого масиву з дробовими числами.
Написана функція для двійкового пошуку повинна повертати кортеж,
де першим елементом є кількість ітерацій, потрібних для знаходження елемента.
Другим елементом має бути "верхня межа" — це найменший елемент,
який є більшим або рівним заданому значенню.
"""

def binary_search(arr, x, depth=1):
    """Binary recursive search"""
    array_length = len(arr)
    mid = array_length // 2
    if arr[mid] == x:
        return x, depth
    if array_length == 1:
        return None, depth
    new_array = arr[:mid] if arr[mid] > x else arr[mid:]
    return binary_search(new_array, x, depth=depth+1)

example_array = [1, 2, 2.6, 2.8, 3, 9, 10.5, 10.7, 19.887, 19.888, 20, 21.6]

if __name__ == '__main__':
    element = float(input("Input element to search:"))
    print(binary_search(example_array, element))
