todo_list = list()
tekst = "1.Dodaj \n2.Usuń \n3.Wyłącz"


def choose():
    print(todo_list)
    print(tekst)
    option = input("Co chcesz zrobić?: ")
    if option == "1":
        task = input("Nazwa zadania: ").upper()
        todo_list.append(task)
        choose()
    elif option == "2":
        i = 1
        for x in todo_list:
            print(f'{i}: {x}')
            i = i + 1
        print(len(todo_list))
        number = int(input("Które zadanie chcesz usunąć?"))
        if number > len(todo_list) and isinstance(number, int):
            print("Nie ma takiego zadania")
        else:
            todo_list.pop(number - 1)

        choose()
    elif option == "3":
        print('Wyłączam program')
    else:
        print("Złe polecenie, spróbuj ponownie!")
        choose()


choose()
