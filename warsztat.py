workers = list()
menu = "1.Dodaj klienta \n2.Przypisz usterke \n3.Przypisz pracownika \n4.Podsumowanie \n5.Pokaż wszystkich klientów \n6.Pokaż wszystkie naprawy"
clients = {}
repairs = {}


class Customer:
    def __init__(self, imie, nazwisko, telefon):
        self.imie = imie
        self.nazwisko = nazwisko
        self.telefon = telefon

    def przedstaw(self):
        print(self.imie)
        print(f'Twój Customer: {self.imie} {self.nazwisko}, numer: {self.telefon}')


def main():
    print(menu)
    option = input("Co chcesz zrobić?: ")
    if option == "1":
        imie = input("Podaj imię: ")
        nazwisko = input("Podaj nazwisko: ")
        numer = input("Podaj numer telefonu: ")
        newCustomer = Customer(imie, nazwisko, numer)
        clients[newCustomer.telefon] = [newCustomer.imie, newCustomer.nazwisko, newCustomer.telefon]
        print(newCustomer.przedstaw())
        main()

    if option == "2":
        id = input("Podaj identyfikator usterki: ")
        usterka = input("Podaj nazwę usterki: ")
        cena = input("Podaj cenę naprawy: ")
        klient = input("Podaj numer telefonu klienta: ")
        repairs[id] = [usterka, cena, clients[klient]]
        main()

    if option == "3":
        imie = input("Podaj imię pracownika: ")
        nazwisko = input("Podaj nazwisko pracownika: ")
        id = input("Podaj identyfikator usterki: ")
        repairs[id] = [repairs[id], {'pracownik', imie, nazwisko}]
        main()

    if option == "4":
        id = input("Podaj identyfikator usterki: ")
        print(repairs[id])
        main()

    if option == "5":
        print(clients)
        main()

    if option == "6":
        print(repairs)
        main()


if __name__ == '__main__':
    main()
