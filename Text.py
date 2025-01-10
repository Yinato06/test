def custom_write(file_name, strings):
    line_position = {}
    current_line = 1
    with open(file_name, 'a+', encoding='utf-8') as file:
        for string in strings:
            byte_position = file.tell()
            file.write(string + '\n')
            line_position[(current_line, byte_position)] = string
            current_line += 1
        return line_position


info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
]

result = custom_write('test.txt', info)

for elem in result.items():
    print(elem)
