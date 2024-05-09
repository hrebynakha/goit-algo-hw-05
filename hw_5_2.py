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
    mid = len(arr) // 2
    #print(arr, mid, arr[mid])
    if arr[mid] == x:
        return depth, arr[mid]
    if len(arr) == 2:
        # return right or left element for x
        if x > arr[mid-1]:
            return depth, arr[mid]
        return depth, arr[mid-1]
    new_array = arr[:mid+1] if arr[mid] > x else arr[mid:]
    return binary_search(new_array, x, depth=depth+1)

arr  = [1.1, 1.3, 2.5, 3.8, 4.6, 5.9]

if __name__ == '__main__':
    for test_element in [3.8, 4.6, 6.0, 1.2, 3, 0, 10 ]:
        print("Searching element...", test_element)
        print(binary_search(arr, test_element))
