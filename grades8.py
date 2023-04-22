result = {}
with open('grades.txt', 'r', encoding='utf-8') as file1:
    for line in file1:
        l = line.strip().split()
        grades = [int(i) for i in l[-4:]]
        aver_grade = sum(grades) / len(grades)
        if aver_grade >= 4.5:
            result[l[0] + ' ' + l[1]] = aver_grade
for student, aver_grade in result.items():
    print(f'{student}, средний балл: {aver_grade:.2f}')     