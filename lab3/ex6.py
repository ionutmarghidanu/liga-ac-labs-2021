class Human:

    def power(self):
        print("I am a human")

    def human_method(self):
        print('Self human method')


class Woman:

    def power(self):
        print("I am a woman")

    def woman_method(self):
        print('Self woman method')


class SuperWoman(Woman, Human):

    def power(self):
        super().power()
        print("Extended functionality")


s = SuperWoman()
s.power()

