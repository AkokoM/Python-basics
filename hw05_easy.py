__author__ = 'Kokorev Alexey Mihaylovich'

# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.

'''
import os


def make_dir(i):
    dir_path = os.path.join(os.getcwd(), i)
    try:
        os.mkdir(dir_path)
    except:
        print(dir_path + ' - такая директория уже есть')


def remove_dir(i):
    os.rmdir('{}'.format(i))


for j in range(9): # Создание директорий dir_1 - dir_9 в папке из которой запущен данный скрипт
    make_dir('dir_{}'.format(j+1))


# for j in range(9):
#     remove_dir('dir_{}'.format(j+1))
'''

# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.
# ТОЛЬКО ПАПКИ, А НЕ ФАЙЛЫ!

'''
import os

for root, dirs, files in os.walk("."):
    print(root)
'''

# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.
# ИСПОЛЬЗОВАТЬ ТОЛЬКО МОДУЛЬ OS

'''
import os

def copy_current_script():
    global file_path
    import shutil

    base_name = os.path.basename(__file__)
    file_path = os.path.join(os.getcwd(), 'copy_{}'.format(base_name))
    shutil.copyfile(__file__, file_path)
    print('Создана копия файла: {}'.format(file_path))

copy_current_script()
'''
