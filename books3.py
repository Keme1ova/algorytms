with open('books.txt', 'r', encoding='utf-8') as file:
    words = file.read().replace('"', '').split()
    result = [w for w in words if len(w) == len(max(words, key=len))]
 
print(*result) 