with open('first.txt', 'r', encoding='utf-8') as file1, \
open('second.txt', 'r', encoding='utf-8') as file2:
    for line_x, line_y in zip(file1, file2):
        print(f'Сотрудник {line_x.strip()}, должность - {line_y.strip()}')