class MojaKlasa:
    wiek = 12
    wzrost = 5
    imie = "Adam"


mk1 = MojaKlasa()
mk1.imie = "Szymon"
mk1.wzrost = 80
mk1.wiek = 20


class Osoba:
    wspolczynnik_wyplaty = 2.0


    def __init__(self, imie, wiek, **kwargs):
        self.imie = imie
        self.wiek = wiek

    def get_salary(self):
        return 5000 * self.wspolczynnik_wyplaty

class Admin(Osoba):
    wspolczynnik_wyplaty = 3.0

class Maszyna():
    pobor_energii = 50

class Cyborg(Osoba, Maszyna):
    nr_licznika = 100

c1 = Cyborg('Astro', 125, masa = 12, trybiki = 333, costam = 'abc')

j1 = Osoba("Jan", 23)
j2 = Osoba("Szymon", 25)
a1 = Admin("Robert", 33)
print(a1.get_salary())
print(j1.get_salary())

print(j1.imie)
print(j1.wiek)
print(j2.imie)
print(j2.wiek)