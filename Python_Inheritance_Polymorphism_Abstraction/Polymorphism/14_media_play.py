class Media:
    def play(self):
        print("Playing media.")


class Audio(Media):
    def play(self):
        print("Playing audio file.")


class Video(Media):
    def play(self):
        print("Playing video file.")


class Podcast(Media):
    def play(self):
        print("Playing podcast episode.")


for media in [Audio(), Video(), Podcast()]:
    media.play()
