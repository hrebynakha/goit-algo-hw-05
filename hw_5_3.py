"""
Завдання 3

Порівняти ефективність алгоритмів пошуку підрядка: 
Боєра-Мура, Кнута-Морріса-Пратта та Рабіна-Карпа на основі двох текстових файлів (стаття 1, стаття 2). 
Використовуючи timeit, треба виміряти час виконання кожного алгоритму для двох видів підрядків: 
одного, що дійсно існує в тексті, та іншого — вигаданого (вибір підрядків за вашим бажанням). 
На основі отриманих даних визначити найшвидший алгоритм для кожного тексту окремо та в цілому.
"""
from timeit import timeit
from algoritms import boyer_moore_search, kmp_search, rabin_karp_search
import requests

def test_bm_search(text, pattern):
    """Boyer Moore search test function"""
    boyer_moore_search(text, pattern)


def test_kmp_search(text, pattern):
    """Knut-Moris-Pratta search test function"""
    kmp_search(text, pattern)


def test_rk_search(text, pattern):
    """Rabin-Karp search test function"""
    rabin_karp_search(text, pattern)

def run_test(func_part_name, text_id, pattern, times=100):
    """Run test function"""
    print(f"Testing search algoritm {alg_names[func_part_name]}" +\
          f" for article №{text_id}, searching '{pattern}' ......")
    for _ in range(4):
        print("" * 100)
    elapsed_time = timeit(
        f"test_{func_part_name}_search(text, pattern)",
        setup=f"from __main__ import test_{func_part_name}_search",
        number=times, globals=globals()
    )
    return f"Result for algoritm {alg_names[func_part_name]}" +\
           f" elapsed time:{elapsed_time}"

urls = ['18_R5vEQ3eDuy2VdV3K5Lu-R-B-adxXZh', '13hSt4JkJc11nckZZz2yoFHYL89a4XkMZ']
alg_names = {
    "bm" : "Boyer Moore",
    "kmp" : "Knut-Moris-Pratta",
    "rk" : "Rabin-Karp"
}
for func_short_name in alg_names.keys():
    for text_id, doc_id in enumerate(urls, start=1):
        url = f"https://drive.usercontent.google.com/u/0/uc?id={doc_id}&export=download"
        response = requests.get(url)
        text = response.text
        for pattern in ["пошук", "Python"]:
            print(run_test(func_short_name, text_id, pattern, 5000))
            print("=" * 100)
