punctuation = """!"#$%&()*+,-./:;<=>?@[]^_`{|}~"""


def clean_lyrics(lyrics):
    for char in punctuation:
        lyrics = lyrics.replace(char, "")

    lyrics = lyrics.replace("-", "")
    lyrics = lyrics.lower()

    return lyrics
