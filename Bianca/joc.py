from Bianca.jucator import Jucator


class Joc:
    def __init__(self, jucator1char, jucator2char):
        self.jucator1 = Jucator(jucator1char)
        self.jucator2 = Jucator(jucator2char)
        self.matrix = [['-', '-', '-'],
                       ['-', '-', '-'],
                       ['-', '-', '-']]
        self.rand = 1
        self.joaca()

    def joaca(self):
        while not (self.verificareGameOver()):
            self.afisare()
            print("Jucator ", self.rand, "\n")
            pozitie_incorecta = 1
            while pozitie_incorecta:
                print("Linia:")
                linie = input()
                while not (int(linie) >= 0 and int(linie) < 3):
                    print("Linie incorecta, introdu iar")
                    linie = input()
                print("\nColoana:")
                coloana = input()
                while not (int(coloana) >= 0 and int(coloana) < 3):
                    print("Coloana incorecta, introdu iar")
                    coloana = input()
                if self.matrix[int(linie)][int(coloana)] != '-':
                    pozitie_incorecta = 1
                    print("Pozitie ocupata");
                    self.afisare()
                else:
                    pozitie_incorecta = 0
                    if self.rand == 1:
                        self.matrix[int(linie)][int(coloana)] = self.jucator1.getx0();
                        self.rand = 2;
                    else:
                        self.matrix[int(linie)][int(coloana)] = self.jucator2.getx0();
                        self.rand = 1;

    def afisare(self):
        for i in self.matrix:
            for j in i:
                print(j, end=" ")
            print()

    def verificareGameOver(self):
        """verificare pe linii si coloane"""

        for i in range(2):
            if self.matrix[i][0] == self.matrix[i][1] == self.matrix[i][2] and self.matrix[i][0] != '-':
                self.afisare()
                if self.jucator1.getx0() == self.matrix[i][0]:
                    print("X a castigat")
                else:
                    print("0 a castigat")
                exit(1);

            if self.matrix[0][i] == self.matrix[1][i] == self.matrix[2][i] and self.matrix[0][i] != '-':
                self.afisare()
                if self.jucator1.getx0() == self.matrix[0][i]:
                    print("X a castigat")
                else:
                    print("0 a castigat")
                exit(1);

        """Verificare pe diagonale"""

        if self.matrix[0][0] == self.matrix[1][1] == self.matrix[2][2] and self.matrix[0][0] != '-':
            self.afisare()
            if self.jucator1.getx0() == self.matrix[0][0]:
                print("X a castigat")
            else:
                print("0 a castigat")
            exit(1);
        if self.matrix[0][2] == self.matrix[1][1] == self.matrix[2][0] and self.matrix[0][2] != '-':
            self.afisare()
            if self.jucator1.getx0() == self.matrix[0][2]:
                print("X a castigat")
            else:
                print("0 a castigat")
            exit(1)

        """Verificare remiza"""
        ok = "true"
        for i in self.matrix:
            for j in i:
                if j == '-':
                    ok = "false"
        if ok == "true":
            print("Remiza");
            exit(1)


Joc('X', '0')
