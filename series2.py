filename = input()
lines, words, symbols = 0, 0, 0
with open("series.txt", 'r', encoding='utf-8') as file:
    for i in file:
        lines += 1
        words += len([w for w in i.split() if w.isalpha()])
        symbols += len([s for s in i if s.isalnum()])
print(f'Количество строк в файле {filename}: {lines}\n'
      f'Количество слов: {words}\n'
      f'Число символов: {symbols}\n'
     )