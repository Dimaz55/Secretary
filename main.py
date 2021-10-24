documents = [
    {
        "type": "passport",
        "number": "2207 876234",
        "name": "Василий Гупкин"
    },
    {
        "type": "invoice",
        "number": "11-2",
        "name": "Геннадий Покемонов"
    },
    {
        "type": "insurance",
        "number": "10006",
        "name": "Аристарх Павлов"
    },
    {
        "type": "СНИЛС",
        "number": "156-158-485 32",
        "name": "Иван Петров"
    }
]

directories = {
    '1': ['2207 876234', '11-2'],
    '2': ['10006', '156-158-485 32'],
    '3': []
}


def menu():
    '''
    Вывод доступных команд
    '''
    print('Доступные команды:')
    print(' p - вывод владельца по номеру документа')
    print(' s - вывод номера полки по номеру документа')
    print(' l - вывод всех документов')
    print(' a - добавить новый документ')
    print(' d - удаление документа')
    print(' m - перемещение документа между полками')
    print('as - добавление полки')
    print('ss - показать содержимое полок')
    print(' q - выход\n')


def list_all_docs(docs):
    '''
    l
    Вывод всех документов из списка
    '''
    print('Список всех документов:')
    print(''.ljust(55, '-'))
    print('Тип'.ljust(15), '| Номер'.ljust(17), '| Владелец')
    print(''.ljust(55, '-'))
    for doc in docs:
        doc_type, doc_num, doc_owner = doc.values()
        print(doc_type.ljust(15), '| ' + doc_num.ljust(15), '| ' + doc_owner)
    print()


def print_owner_by_doc(docs):
    '''
    p
    Вывод владельца документа по номеру
    '''
    doc_num = input_doc(docs, False)
    if doc_num:
        for doc in docs:
            if doc_num == doc['number']:
                print(f"\nВладелец документа №{doc['number']}: {doc['name']}\n")


def print_shelf_num_by_doc(docs, dirs):
    '''
    s
    Вывод номера полки с нужным документом
    '''
    doc_num = input_doc(docs,False)
    if doc_num:
        for shelf, docs in dirs.items():
            if doc_num in docs:
                print(f"Документ {doc_num} хранится на полке №{shelf}\n")


def add_new_doc(docs, dirs):
    '''
    a
    Добавление нового документа в базу docs и на перечень полок dirs
    '''
    print('Добавление нового документа')
    doc_num = None
    while doc_num is None:
        doc_num = input_doc(docs, True)
    doc_type = input('Введите тип: ')
    doc_owner = input('Введите имя владельца: ')
    max_shelf = max(dirs)
    while True:
        print(f"Введите номер полки для хранения (1 - {max_shelf}): ", end='')
        shelf = input()
        if shelf not in dirs.keys():
            print('Такой полки не существует!')
        else:
            break

    docs.append({'type': doc_type, 'number': doc_num, 'name': doc_owner})
    dirs[shelf].append(doc_num)
    print(f'\nДокумент №{doc_num} создан и добавлен на полку №{shelf}\n')


def change_shelf(docs, dirs):
    '''
    m
    Перемещение документа на другую полку
    '''
    max_shelf = max(dirs)

    print('\nПеремещение документа на новую полку')
    doc_num = input_doc(docs, False)
    if doc_num:
        for s_num, docs in dirs.items():
            if doc_num in docs:
                docs.remove(doc_num)

        while True:
            print(f"Введите номер новой полки (1 - {max_shelf}): ", end='')
            shelf = input()
            if shelf not in dirs.keys():
                print('Полка не существует!')
            else:
                break

        dirs[shelf].append(doc_num)
        print(f"\nТеперь документ {doc_num} хранится на полке № {shelf}\n")


def delete_doc(docs, dirs):
    '''
    d
    Удаляет документ из каталога docs и стеллажа dirs
    '''
    print('Удаление документа:')
    doc_num = input_doc(docs, False)
    if doc_num:
        for doc in docs:
            if doc_num == doc['number']:
                docs.remove(doc)
                for s_num, shelf in dirs.items():
                    if doc_num in shelf:
                        shelf.remove(doc_num)
                        print(f'Документ {doc_num} c полки №{s_num} удалён.\n')


def add_shelf(dirs):
    '''
    as
    Добавление полок на стеллаж dirs
    '''
    new_shelf = input("Введите номер новой полки: ")
    if new_shelf in dirs.keys():
        print("Такая полка уже существует!\n")
    else:
        dirs[new_shelf] = []


def show_shelves(dirs):
    '''
    ss
    Показывает содержимое полок
    '''
    for num, docs in dirs.items():
        print(f'{num}: {", ".join(docs)}')


def input_doc(docs, exist):
    '''
    Ввод номера документа и проверка его существования с номером в каталоге docs.
    exist = True проверяет отсутствие в базе для создания нового возвращает None
            False проверяет существование в базе и возвращает номер
    '''
    doc_num = input('Введите номер документа: ')
    print()
    if exist == True:
        for doc in docs:
            if doc_num == doc['number']:
                print('Документ с таким номером уже существует!\n')
                return None
        return doc_num
    else:
        for doc in docs:
            if doc_num == doc['number']:
                return doc_num
        print('Документ с таким номером не существует!\n')
        return None


def start():
    print('\n   Здравствуйте!')
    print('-------------------')
    menu()
    while True:
        cmd = input('Введите команду (h - помощь): ').lower()
        print()

        if cmd == 'h' or cmd == 'р':
            menu()

        elif cmd == 'q' or cmd == 'й':
            print('До свидания!')
            break

        elif cmd == 'l' or cmd == 'д':
            list_all_docs(documents)

        elif cmd == 'p' or cmd == 'з':
            print_owner_by_doc(documents)

        elif cmd == 's' or cmd == 'ы':
            print_shelf_num_by_doc(documents, directories)

        elif cmd == 'a' or cmd == 'ф':
            add_new_doc(documents, directories)

        elif cmd == 'm' or cmd == 'ь':
            change_shelf(documents, directories)

        elif cmd == 'd' or cmd == 'в':
            delete_doc(documents, directories)

        elif cmd == 'as' or cmd == 'фы':
            add_shelf(directories)

        elif cmd == 'ss' or cmd == 'ыы':
            show_shelves(directories)

        else:
            print('Неизвестная команда!\n')


if __name__ == '__main__':
    start()
