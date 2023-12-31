# goit-algo-hw-04
# Порівняння трьох алгоритмів сортування: злиттям, вставками та Timsort

## Опис завдання

Це завдання полягає у порівнянні ефективності трьох алгоритмів сортування: сортування злиттям, сортування вставками та алгоритм Timsort, що використовується у вбудованих функціях сортування: sorted і sort у Python. Ефективність буде оцінена за часом виконання алгоритмів на різних наборах даних. Для вимірювання часу виконання алгоритмів використовувався модуль `timeit`.

## Емпіричні дані

Для порівняння алгоритмів сортування були використані набори даних різного розміру. Результати тестування наведні в таблиці:

| алгоритм / розмір | 1 000 | 5 000 | 10 000| 50 000|
| --------------    |:-----:| -----:|-----:|-----:|
| Merge Sort        |0.00204|0.01613|0.03648|0.18057|
| Insertion Sort    |0.02173|0.59428|2.24328|62.75997|
| Timsort           |0.00011|0.00069|0.00146|0.00916|

- Сортування злиттям (Merge Sort) виконується за часовою складністю O(n∙logn) 
- Сортування вставками (Insertion Sort) має часову складність O($n^2$) 
- Timsort, який використовує комбінацію сортування злиттям і вставками, демонструє кращу часову ефективність у порівнянні з іншими алгоритмами сортування 

Вочевидь, алгоритм Timsort є більш ефективним. Більш наглядно це показують дані у таблиці, де зазначено ***у скільки разів Timsort швидший*** за Merge Sort та Insertion Sort:

| алгоритм  | 1 000 | 5 000 | 10 000| 50 000|
| --------------    |:-----:| -----:|-----:|-----:|
| Merge Sort        |18,55|23.38|24.99|19.71|
| Insertion Sort    |197.55|861.28|1536.49|6851.53|

## Висновки

Результати емпіричного аналізу показують, що алгоритм Timsort, використовуваний вбудованою функцією sorted() в Python, працює більш ефективно, ніж обидва окремі алгоритми сортування. Це відбувається завдяки комбінації сортування злиттям та сортування вставками, які адаптуються до характеристик даних. Це пояснює, чому багато програмістів використовують вбудовані алгоритми сортування в Python, такі як sorted(), оскільки вони оптимізовані для широкого спектру вхідних даних та показують хорошу ефективність.