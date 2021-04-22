class Song(object):

    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        print("------")
        for line in self.lyrics:
            print(line)


lyrics = ["Happy birthday to you", 
            "I don't want to get sued",
            "So I'll stop right there"]
happy_bday = Song(lyrics)

lyrics = ["They rally around the family",
            "With pockets full of shells"]
bulls_on_parade = Song(lyrics)

happy_bday.sing_me_a_song()
bulls_on_parade.sing_me_a_song()
print("------")
