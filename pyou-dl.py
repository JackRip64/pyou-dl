#!/usr/bin/python3 
import youtube_dl
import pickle

# Global Vars
NEW_SONGS_FILE = "songs_to_add.txt"
USED_SONGS_FILE = "used_songs.pkl"
DOWNLOAD_PATH = ".."


# adds new songs from NEW_SONGS_FILE
def add_songs():
	with open(USED_SONGS_FILE, "rb") as file:
		used_songs = pickle.load(file)

	with open(NEW_SONGS_FILE, "r") as file:
		for song_name in [line.replace("\n", "") for line in file.readlines()]:

			# defining options for ytdl instance
			DL_OPTIONS = {
				'format': 'bestaudio',
				'outtmpl': f'{DOWNLOAD_PATH}/{song_name}.%(ext)s',
				'default_search': 'ytsearch',
				'noplaylist': True,
				'postprocessors': [{
					'key': 'FFmpegExtractAudio',
					'preferredcodec': 'mp3',
					'preferredquality': '192'
					}]
			}

			# pulling video info
			with youtube_dl.YoutubeDL(DL_OPTIONS) as ytdl:
				info = ytdl.extract_info(f"{song_name} -- Audio", download=False)["entries"][0]

				# pulling relevant info
				video_title, video_id = info["title"], info["id"]

				# checking if video is already used
				not_used = True
				for video in used_songs.values():
					if video == video_id:
						print(f"\n[[[Excluding {song_name}, ID already in use]]]\n")
						not_used = False
						break

				# accepting video into dict and downloading
				if not_used:
					used_songs[song_name] = video_id
					ytdl.download([f"youtube.com/watch?v={video_id}"])
					print(f"\n[[['{song_name}' successfully downloaded]]]\n")

	# dumping updated dict into USED_SONGS_FILE
	with open(USED_SONGS_FILE, "wb") as file:
		pickle.dump(used_songs, file)

# shows songs and id's from USED_SONGS_FILE
def show_used_songs():
	with open(USED_SONGS_FILE, "rb") as file:
		for song_name, video_id in pickle.load(file).items():
			print(f"{song_name:>50} | {video_id}")

# main function with decision making
def main():
	print("1. Add Songs\n2. View Used Songs")
	response = None
	while response not in ["1", "2"]:
		response = input("> ")
		if response not in ["1", "2"]:
			print("Invalid Input")
	if response == "1":
		add_songs()
	elif response == "2":
		show_used_songs()

if __name__ == '__main__':
	main()
