income, outcome = 0, 0
with open('income.txt', 'r', encoding='utf-8') as file1, \
open('outcome.txt', 'r', encoding='utf-8') as file2:
    for line in file1:
        num = line.strip()[3:]
        income += int(num)

    for line in file2:
        num = line.strip()[4:]
        outcome += int(num)
print(f'Прибыль за прошлый месяц: {income - outcome} RUB')