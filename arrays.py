import random

num_list = list(random.randint(0, 100) for i in range(20))
print("Список: " ,num_list)

print("Макс: " , max(num_list), "  Мин: ", min(num_list))
print("Cумма: ",sum(num_list))
print("Длина списка: ",len(num_list))

num_list.sort()
print("По возрастанию: ",num_list)
num_list.sort(reverse=True)
print("По убыванию: ",num_list)
num_list2 = num_list.copy()
print("Cкопированные список: ", num_list2)
num_list.clear()
print("Очищенный список: ",num_list)



sym_list = ['apple' , 'orange' , 'watermelon' , 'peach' , 'strawberry' , 'pineapple']
print("Самое длинное: ",max(sym_list, key=len))
print("Самое короткое: ",min(sym_list, key=len))
del sym_list[4]
sym_list.append('coconut')
print("Обновленный список: ",sym_list)

word_list = ['h', 'e', 'l', 'l', 'o']
sym_list.extend(word_list)
print("Смешаннай список: ",sym_list)

word_list.reverse()
print("Переверуто: " ,word_list)

list1 = list(random.randint(0, 10) for i in range(5))
print("Первый список: ", list1)
list2 = list(random.randint(0, 10) for i in range(5))
print("Второй список: ", list2)
sum = [i + j for i, j in zip(list1, list2)]
print("Сумма списков: " , sum)





# -------------------- PRACTICE -------------------------

# # -------1
# my_str = '6emds83mmsad99342n42ld9xm37vn4820'
# myh = [i for i in my_str if i.isnumeric()]
# print(myh)
# my_lst2 = [int(i) for i in my_str if i.isdigit()]
# print("Мин: " ,min(my_lst2), "Макс: " , max(my_lst2))

# # -------2
# st = [int(i) for i in input('Введите числа: ').split()]
# lst = [i for i in st if st.count(i) > 1]
# print(*lst)


# # -------3
# zad3 = list(random.randint(0, 100) for i in range(20))
# print("Список: " ,zad3)
# lst_odd = [i for i in zad3 if i % 2 != 0]
# lst_even = [i for i in zad3 if i % 2 == 0]
# print("Нечетные числа: ",*lst_odd)
# print("Четные числа: ",*lst_even)


# # -------4
# # str = list(input())
# # err = [str.index(i) for i in str if st.count(i) > 2]
# # letter = str[err[0]]
# # st.remove(letter)
# # print(f'Буква "{letter}" ошибочно повторяется {len(err) - 2} раз(а)')
# # print(f'Исправленное слово: {"".join(st)}' if len(err) == 3 else 'Не могу исправить')



# # -------5
# # Без труд#а не выловишь и рыбку из пруда
# st = list(input("5)Введите текст: "))
# err = st.index('#')
# del st[err]
# sp = ''.join(st)
# word = max(sp.split(), key=len)
# print(sp, word, sep='\n')

# # -------6
# # фрукты образцовый груз@вик цветы невз56годы дер#ево задачка виноградник грозовой зима яб7локо
# sp = input("6)Введите: ").split()
# sp = [i for i in sp if i.isalpha()]
# sp.sort(key=len)
# print(*sp, sep='\n')



# # -------7
# # кот ёж море ель береза апельсин бирюза имитация
# vowels = 'аиеёоуыэюя'
# st = input("7)Введите cлова: ").split()
# lst1 = [i for i in st if i[0] in vowels]
# lst2 = [i for i in st if i not in lst1]
# print("Гласные: ",*lst1)
# print("Соласные: ",*lst2)


# # -------8
# keys = ['модель', 'цена', 'количество', 'размер', 'цвет', 'скидка']
# values = ['XXLDude', 5678.55, 57, 'XXL', 'черный', '12%']
# res = [key + ': ' + str(value) for key, value in zip(keys, values)]
# print("(8)",*res, sep='\n')


# # -------9
# # Вася Пупкин, 4 5 3 4 5 3 4 5
# lst = input("9)Введите: ").split(', ')
# grades = [int(i) for i in lst[1].split()]
# sum = sum(grades)
# avg = sum / len(grades)
# print(f'{lst[0]}, средний балл: {avg:.2f}')




