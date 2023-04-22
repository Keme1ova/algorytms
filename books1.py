with open('books.txt', 'r', encoding='utf-8') as file:
    for i in range(3):
        line = file.readline().strip()
        print(line)