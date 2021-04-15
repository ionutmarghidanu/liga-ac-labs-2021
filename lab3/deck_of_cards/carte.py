class Carte:

    def __init__(self, valoare, culoare):
        """
        :param valoare: int: valoarea cartii de joc
        :param culoare: string: tipul cartii
        """
        self.valoare = valoare
        self.culoare = culoare

    def __eq__(self, other) -> bool:
        return self.valoare == other.valoare and self.culoare == other.culoare

    def __str__(self):
        return self.valoare + ' ' + self.culoare
