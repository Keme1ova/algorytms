with open('fruits4.txt', 'r', encoding='utf-8') as file:
    result = {}
    for line in file:
        words = line.strip().lower().split()
        for w in words:
            result[w] = result.get(w, 0) + 1
print(f'Названия этих фруктов встречаются в тексте:')
for k, v in result.items():
    print(f'"{k}" - {v} раз(а)')