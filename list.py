empty_list = list()
empty_list2 = []
# to samo

names = ['Ola', 'Asia', 'Zosia', 'Bartek']

print(names[2]);

mixed = ['Python', 3.8, 4, True]

nested = [[1, 2, 4], ['a', 'b', 'c']]

names[1] = "Patryk"

print(names)  # zmieni sie Asia na Patryk
print(names[1])

full_list = names + mixed + nested
print(full_list)
print(full_list[-1])

full_list.append('moja zmienna')
print(full_list)

full_list.extend(range(10))
print(full_list)

full_list.insert(2, 'moje dane')
print(full_list)
# INSERT NIE JEST WYDAJNY W PYTHONIE, przy duzych listach ma to znaczenie

full_list.remove(4)
full_list.pop(-2)
print(full_list)

full_list.reverse()
print(full_list)

full_list.clear()
print(full_list)
