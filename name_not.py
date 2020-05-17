

documents = [
    {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
    {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
    {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"},
    {"type": "insurance", "number": "5455 028765"}
]

directories = {
    '1': ['2207 876234', '11-2', '5455 028765'],
    '2': ['10006'],
    '3': []
}

def add(doc):
  number_shelf = input('Введите номер полки: ')
  if number_shelf in directories.keys():
    number_doc = input('Введите номер документа: ')
    type_doc = input('Введите тип документа: ')
    name = input('Ведите номер владельца: ')
    doc.append({"type": type_doc , "number": number_doc , "name": name})
    directories[number_shelf] += [number_doc]
    print(doc)
    print(directories)

  else:
    print('Такой полки не существует')

# add(documents)

def people_name(doc):
    for doc_name in doc:
        try:
            doc_name['name']
        except:
            print(f'У данного документа {doc_name["number"]} отсутствует имя name.')


# people_name(documents)


def main():
    while True:
        user_input = input(
            'Введите номер команды: a - команда, которая добавит новый документ, p - команда, которая выведет ошибку, q - выход из программы ')
        if user_input == 'a':
            add(documents)
        if user_input == 'p':
            people_name(documents)

        elif user_input == 'q':
            break


main()
