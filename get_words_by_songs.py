from clean_lyrics import clean_lyrics
import re


def get_words_by_songs(lyrics):
    cleaned_lyrics = re.sub(r"^\[.*?$", "", lyrics, flags=re.MULTILINE)

    songs_list = cleaned_lyrics.split("------------ ")

    cleaned_lyrics = re.sub(r"^Title:.*\n", "", cleaned_lyrics, flags=re.MULTILINE)

    songs_list = re.sub(r"^Title:.*\n", "", songs_list, flags=re.MULTILINE)

    cleaned_lyrics = clean_lyrics(cleaned_lyrics)

    print(songs_list, len(songs_list))
