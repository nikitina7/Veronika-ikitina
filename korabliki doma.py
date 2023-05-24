import random
print('💙- ūdens'
      '🤍- nekas nav'
      '🧡- ir kuģis'
      '🤎-kuģa vairs nav')
more = [

]
my_list = [

]
razmer = int(input("Izvēlies jūras izmēru: "))

for listi in range(razmer):
    kletka = [0] * razmer
    more.append(kletka)
    my_list.append(listi)

counter = 0
razmer_korabl = random.randint(0, razmer // 2)
while counter < razmer // 2:
    kugis_list = random.randrange(0, razmer)
    kugis_element = random.randrange(0, razmer)
    if more[kugis_list][kugis_element] == 0:
        more[kugis_list][kugis_element] = 1

        counter += 1
    else:
        more[kugis_list][kugis_element] = 1

vistrel = razmer * razmer // 2
while True:
    for index, row in enumerate(more):
        print(index, end='')
        for element in row:
            if element == 0 or element == 1:
                print('💙', end='')
            elif element == 2:
                print('🤍', end='')
            elif element == 3:
                print('🧡', end='')
        print('')
    print('Šeit ir ' + str(counter) + ' kuģi.')
    print('Tev atlika ' + str(vistrel) + ' šāvieni.')
    if counter == 0:
        print('Visi kuģi tika likvidēti. Tu uzvarēji')
        break
    if vistrel == 0:
        print('Šeit vel ir kuģi, bet tev vairs nav šāvienu. You lose.')
        for index, row in enumerate(more):
            print(index, end='')
            for element in row:
                if element == 0:
                    print('💙', end='')
                elif element == 1:
                    print('🤎', end='')
                elif element == 2:
                    print('🤍', end='')
                elif element == 3:
                    print('🧡', end='')
            print('')
        break
    vistrel_vert = int(input('Izvēlies vertikāli(0-' + str(razmer - 1) + '): '))
    vistrel_hor = int(input('Izvēlies horizontāli(0-' + str(razmer - 1) + '): '))
    if more[vistrel_hor][vistrel_vert] == 0:
        more[vistrel_hor][vistrel_vert] = 2
        vistrel -= 1
    elif more[vistrel_hor][vistrel_vert] == 1:
        more[vistrel_hor][vistrel_vert] = 3
        counter -= 1
        vistrel -= 1