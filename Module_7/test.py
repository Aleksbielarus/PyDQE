from package import text_transform_module
from package import console_menu

def abc():
    path_to_file = console_menu.input_file_path('input_file')
    file_text = list(open(path_to_file, 'r'))
    return file_text, path_to_file

print(abc()[0])
print(abc()[1])

