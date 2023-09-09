class genre:
    def __init__(self, genre):
        self.genre = genre
        self.song = []

    def addSong(self, song):
        self.song = list(song)
    def __str__(self):
        return f"Genre: {self.song}"

class Song:
    def __init__(self,title,artist):
        self.title = title
        self.artist = artist
    def __str__(self):
        return f"Genre: {self.title}"

class user:
    def __init__(self, username, bill):
        self.username = username
        
Rock = genre("Rock")
Jazz = genre("Jazz")
Pop = genre("Pop")

song1 = Song("Song 1" , "Rock")
song2 = Song("Song 2" , "Rock")
song3 = Song("Song 3" , "Rock")
song4 = Song("Song 4" , "Rock")
song5 = Song("Song 5 ", "Jazz")
song6 = Song("Song 6" , "Jazz")
song7 = Song("Song 7" , "Jazz")
song8 = Song("Song 8" , "Jazz")
song9 = Song("Song 9" , "Pop")
song10 = Song("Song 10" , "Pop")
song11 = Song("Song 11" , "Pop")
song12 = Song("Song 12" , "Pop")

print (song1)

listSong = [song1, song2, song3, song4]

Rock.addSong(listSong)

print (Rock.song)
print (isinstance(Song, genre))