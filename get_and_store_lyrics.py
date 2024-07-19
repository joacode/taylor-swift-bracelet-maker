import requests
from songs_in_albums import all_songs_in_albums

title_str = "------------ Title: "
count = 1

for song_detail in all_songs_in_albums:
    print(count)

    song = requests.get(f"https://taylor-swift-api.sarbo.workers.dev/lyrics/{song_detail["song_id"]}")
    data = song.json()

    with open("songs_lyrics.txt", mode="a") as file:
        file.write(
            title_str
            + data["song_title"]
            + " | song_id: "
            + str(data["song_id"])
            + "\n"
        )
        
        file.write(data["lyrics"] + "\n" + "\n")
    
    count += 1
