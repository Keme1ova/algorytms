alpha = [i for i in range(ord('а'), ord('я') + 1)]
alpha.insert(6, 1105)
with open('alphabet.txt', 'w', encoding='utf-8') as file:
    for i in alpha:
        file.write(chr(i).upper() + chr(i) + '\n')