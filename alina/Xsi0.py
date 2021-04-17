tabel = [' '] * 10


def printPoz():
    print('Pozitii')
    print('1|2|3')
    print('-+-+-')
    print('4|5|6')
    print('-+-+-')
    print('7|8|9')


def printTabel(tabel):
    print('\n')
    print(tabel[1] + '|' + tabel[2] + '|' + tabel[3])
    print('-+-+-')
    print(tabel[4] + '|' + tabel[5] + '|' + tabel[6])
    print('-+-+-')
    print(tabel[7] + '|' + tabel[8] + '|' + tabel[9])
    print('\n')


def mutare(tabel, simbol):
    print(simbol + ' muta')
    print('Alegeti pozitia (de la 1 la 9)')
    poz = input()
    poz_corecta = False
    while not (poz_corecta):
        if not (poz.isnumeric()):
            print("Introduceti un numar")
            print('Alegeti pozitia (de la 1 la 9)')
            poz = input()
        elif (int(poz) < 1 or int(poz) > 9):
            print('Alegeti pozitia (de la 1 la 9)')
            poz = input()
        elif tabel[int(poz)] != ' ':
            print('Pozitie deja ocupata')
            print('Alegeti pozitia (de la 1 la 9)')
            poz = input()
        else:
            poz = int(poz)
            poz_corecta = True

    tabel[poz] = simbol


def castigator(tabel, simbol, cnt):
    if cnt >= 5:
        if ((tabel[7] == simbol and tabel[8] == simbol and tabel[9] == simbol) or (
                tabel[4] == simbol and tabel[5] == simbol and tabel[6] == simbol)
                or (tabel[1] == simbol and tabel[2] == simbol and tabel[3] == simbol) or (
                        tabel[7] == simbol and tabel[4] == simbol and tabel[1] == simbol)
                or (tabel[2] == simbol and tabel[5] == simbol and tabel[8] == simbol) or (
                        tabel[3] == simbol and tabel[6] == simbol and tabel[9] == simbol)
                or (tabel[1] == simbol and tabel[5] == simbol and tabel[9] == simbol) or (
                        tabel[7] == simbol and tabel[5] == simbol and tabel[3] == simbol)):
            printTabel(tabel)
            print('Joc Incheiat')
            print(simbol + ' a catigat!')
            return True
    return False


def joc(tabel):
    printPoz()
    simbol = 'X'  # X incepe
    cnt = 0  # contor
    for i in range(10):
        printTabel(tabel)
        mutare(tabel, simbol)
        cnt += 1
        if castigator(tabel, simbol, cnt): break
        if cnt >= 9:
            print('Joc Incheiat')
            print('Egalitate!')
            break
        if simbol == 'X':
            simbol = '0'
        else:
            simbol = 'X'
    restart = input('Jucati din nou?(DA/NU)')
    if restart.upper() == 'DA':
        tabel = [' '] * 10
        joc(tabel)


joc(tabel)
