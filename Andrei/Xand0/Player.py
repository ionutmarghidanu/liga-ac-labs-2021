class Player:

    def __init__(self, name, char):
        """
        :param name:
        :param char: X or 0
        """
        self.name = name
        self.char = char

    def __str__(self):
        return "Name: " + self.name + "\nChar: " + self.char
