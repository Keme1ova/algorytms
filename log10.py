with open('log.txt', encoding='utf-8') as file_input, \
     open('best_employees.txt', 'w', encoding='utf-8') as file_output:

    for line in file_input:
        start, end = [int(h) * 60 + int(m) for t in line.split(', ')[1:] for h, m in [t.split(':')]]
        if end - start > 240:
            file_output.write(line.split(', ')[0] + '\n')