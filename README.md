# goit-algo-hw-05

Install requirements
```
pip install -r requirements.txt
```
run `py hw_5_3.py`


# Task 3


Вивід результатів пошуку, при парметрах
- кількість тестів функції 5000 разів
- пошук слова "пошук", наявне в обох статтях
- пошук слова "Python", відсутнє в обох статтях


```
Testing search algoritm Boyer Moore for article №1, searching 'пошук' ......
Result for algoritm Boyer Moore elapsed time:0.0981760740005484
Testing search algoritm Boyer Moore for article №1, searching 'Python' ......
Result for algoritm Boyer Moore elapsed time:2.9559935259994745
Testing search algoritm Boyer Moore for article №2, searching 'пошук' ......
Result for algoritm Boyer Moore elapsed time:2.130450657000438
Testing search algoritm Boyer Moore for article №2, searching 'Python' ......
Result for algoritm Boyer Moore elapsed time:4.693560406999495
Testing search algoritm Knut-Moris-Pratta for article №1, searching 'пошук' ......
Result for algoritm Knut-Moris-Pratta elapsed time:0.13692586900015158
Testing search algoritm Knut-Moris-Pratta for article №1, searching 'Python' ......
Result for algoritm Knut-Moris-Pratta elapsed time:5.374850422999771
Testing search algoritm Knut-Moris-Pratta for article №2, searching 'пошук' ......
Result for algoritm Knut-Moris-Pratta elapsed time:3.414310774000114
Testing search algoritm Knut-Moris-Pratta for article №2, searching 'Python' ......
Result for algoritm Knut-Moris-Pratta elapsed time:17.29333726799996
Testing search algoritm Rabin-Karp for article №1, searching 'пошук' ......
Result for algoritm Rabin-Karp elapsed time:0.7576826889999211
Testing search algoritm Rabin-Karp for article №1, searching 'Python' ......
Result for algoritm Rabin-Karp elapsed time:29.06174587299938
Testing search algoritm Rabin-Karp for article №2, searching 'пошук' ......
Result for algoritm Rabin-Karp elapsed time:16.35469499299961
Testing search algoritm Rabin-Karp for article №2, searching 'Python' ......
Result for algoritm Rabin-Karp elapsed time:42.246017779000795

```

Згідно отрманих даних, можемо зробити наступні висовки:
- алгоритм Боєра-Мура, досить ефективно поводить себе в обох прикладах і при пошуку як існуючого елементу так і того якого немає.
- алгоритм Кнута-Морріса-Пратта також видався ефективним для пошуку існуючого тексту, проте можемо спостерігати залежжність зібльшення часу виконання при пошуку неіснуючого елементу при збільшенні кількості символів в тексті.
- алгоритм Рабіна-Карпа досить ефективно себе поводить при пошук існуючго елемента та коли цей елемент знаходить не далеко відносно початку, проте даний алгоритм досить погано себе проявив на при тесту пошуку неіснуючого елемента та при збільшенні загальної кількості тектсу та віддаленості від початку тексту шуканого елементу 