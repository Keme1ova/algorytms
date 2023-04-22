def is_magic_square(square):
    # Проверяем, что список имеет 3 строки и 3 столбца
    if len(square) != 3 or len(square[0]) != 3 or len(square[1]) != 3 or len(square[2]) != 3:
        return False

    # Проверяем, что все числа в списке уникальны и находятся в диапазоне от 1 до 9
    numbers = set()
    for row in square:
        for number in row:
            if number < 1 or number > 9 or number in numbers:
                return False
            numbers.add(number)

    # Проверяем, что сумма каждой строки, каждого столбца и каждой диагонали равна одному и тому же числу
    target_sum = sum(square[0])
    for i in range(1, 3):
        if sum(square[i]) != target_sum:
            return False
        if square[0][i] + square[1][i] + square[2][i] != target_sum:
            return False
    if square[0][0] + square[1][1] + square[2][2] != target_sum:
        return False
    if square[0][2] + square[1][1] + square[2][0] != target_sum:
        return False

    # Если все проверки пройдены, то список является магическим квадратом Ло Шу
    return True

square = [[4, 9, 2], [3, 5, 7], [8, 1, 6]]
if is_magic_square(square):
    print("Это магический квадрат Ло Шу!")
else:
    print("Это не магический квадрат Ло Шу.")
