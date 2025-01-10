import os


def camel_to_snake_case(s):
    snake = ''.join(['_' + c.lower() if c.isupper() else c for c in s])
    return snake.lstrip('_')


# for dirpath, dirnames, filenames in os.walk(r'C:\Users\vpc\PycharmProjects\AdventOfCode2024\AdventOfCode2024'):
for dirpath, dirnames, filenames in os.walk(os.curdir):
    for filename in filenames:
        new_filename = camel_to_snake_case(filename)
        if dirpath == '.' and filename.endswith('.py') and filename != new_filename:  # current directory only
            print(filename, new_filename)
            # os.renamexxx(filename, new_filename)  # xxx added to avoid accidental rename

# print('\nPython files copied to C:\\temp\\PycharmProjects')armProjects')
