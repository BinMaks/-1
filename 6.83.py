
def copy_file(source, destination):
    try:
        with open(source, 'r') as src_file:
            content = src_file.read()
            with open(destination, 'w') as dest_file:
                dest_file.write(content)
        print("Файл успешно скопирован")
    except FileNotFoundError:
        print("Исходный файл не найден")
    except Exception as e:
        print("Ошибка при копировании:", str(e))

source_file = input("Введите имя исходного файла: ")
dest_file = input("Введите имя целевого файла: ")
copy_file(source_file, dest_file)