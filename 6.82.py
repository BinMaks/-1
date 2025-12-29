
def find_word_in_file(filename, word):
    try:
        with open(filename, 'r') as file:
            content = file.read()
            return word in content
    except FileNotFoundError:
        print("Файл не найден")
        return False

filename = input("Введите имя файла: ")
word = input("Введите слово для поиска: ")
if find_word_in_file(filename, word):
    print("Слово найдено")
else:
    print("Слово не найдено")