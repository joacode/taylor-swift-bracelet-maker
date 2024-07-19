from string import ascii_lowercase, digits
import re
from clean_lyrics import clean_lyrics
from get_words_by_songs import get_words_by_songs

separator_pattern = r"^------------ Title:.*?$"
feat_pattern = r"^\[.*?$"

characters = ascii_lowercase + digits
alphabet_list = []

for char in characters:
    alphabet_list.append(char)

char_dictionary = {}
total_char_in_song = 0
most_used_character = ""
most_used_character_count = 0

lyrics = ""

with open("songs_lyrics.txt", mode="r") as file:
    lyrics = file.read()

get_words_by_songs(lyrics)

lyrics = re.sub(separator_pattern, "", lyrics, flags=re.MULTILINE)
lyrics = re.sub(feat_pattern, "", lyrics, flags=re.MULTILINE)

for char in alphabet_list:
    char_count = lyrics.count(char)

    if char_count > 0:
        char_dictionary[char] = char_count
        total_char_in_song += char_count

        if char_count > most_used_character_count:
            most_used_character = char
            most_used_character_count = char_count


most_used_word = ""
most_used_word_count = 0

words_array = clean_lyrics(lyrics).split(sep=None)

words_array.sort()
words_dictionary = {}

for word in words_array:
    word_count = words_array.count(word)

    if word_count > 0:
        words_dictionary[word] = word_count

        if word_count > most_used_word_count:
            print("new most used word: " + word)
            most_used_word = word
            most_used_word_count = word_count


print(char_dictionary, total_char_in_song)
print(most_used_character, most_used_character_count)
print(words_dictionary, len(words_array))
print(most_used_word, most_used_word_count)
