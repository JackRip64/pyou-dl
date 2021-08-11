
### IMPORTANT ###
# Do NOT use '/' in NEW_SONGS_FILE, it WILL break everything.
# Im looking into a way to fix this as it is not a python problem
# 	but a problem with how youtube-dl handles download names.
# 
# When typing songs, always leave out punctuation and capitalize
# 	all words to minimize inconsistencies in the song dictionary.
# You should also format the name so that it can be found at the
# 	top of a single youtube search result. (Basically make it easy
# 	to understand :P)
# EXAMPLE: Thunderstruck -- ACDC

import os
import pickle
import json

#constants
NEW_SONGS_FILE = "songs_to_add.txt"
USED_SONGS_FILE = "used_songs.pkl"
DOWNLOAD_PATH = "../"
CWD = os.getcwd()

#variables
used_songs = {}

# Functions #
#===================================================#

#downloads new songs
def add_new_songs():
	
	#loading in contents of USED_SONGS_FILE
	with open(USED_SONGS_FILE, "rb") as file:
		used_songs = pickle.load(file)

	#looping over every song in NEW_SONGS_FILE
	with open(NEW_SONGS_FILE, "r") as file:
		for song_name in [line.replace("\n", "") for line in file.readlines()]:
			
			#CONSOLE COMMANDS
			#VVVVVVVVVVVVVVV#
			INFO_COMMAND = f"youtube-dl ytsearch:'{song_name}' --no-playlist --write-info-json --skip-download -o '{song_name}'"
			DOWNLOAD_COMMAND = f"youtube-dl -f bestaudio -x --audio-format 'mp3' -o '{DOWNLOAD_PATH}{song_name}.%(ext)s'"

			#executing INFO_COMMAND to generate info.json
			info_got = False
			try:
				os.system(INFO_COMMAND)
				info_got = True
			except Exception:
				print(f"Could not download data for {song_name}")

			if info_got:
				#finding info.json file
				info_file = [file for file in os.listdir(CWD) if file.endswith("info.json")][0]

				#loading video_id from info.json file
				video_id = json.load(open(info_file, "r"))["id"]

				#deleting info.json file
				os.system(f"rm '{info_file}'")

				#check song_name and video_id against used_songs dict reject if in
				not_used = True
				for name, video in used_songs.items():
					if name == song_name:
						print(f"\n[[[Song name '{song_name}' has already been used, not including...]]]\n")
						not_used = False
						break
					elif video == video_id:
						print(f"\n[[[Video ID '{video_id}' has already been used, not including...]]]\n")
						not_used = False
						break
					else:
						pass

				#accepting entry into table for download
				if not_used:
					used_songs[song_name] = video_id
					os.system(f"{DOWNLOAD_COMMAND} youtube.com/watch?v={video_id}")
					print(f"\n[[['{song_name}' has been successfully downloaded to '{DOWNLOAD_PATH}'!]]]\n")
				else:
					pass
						
	#clearing NEW_SONGS_FILE
	with open(NEW_SONGS_FILE, "w") as file:
		file.write("")

	#dumping new used_songs into USED_SONGS_FILE
	with open(USED_SONGS_FILE, "wb") as file:
		pickle.dump(used_songs, file)

#shows used songs (who wouldve guessed?)
def show_used_songs():
	with open(USED_SONGS_FILE, "rb") as file:
		used_songs = pickle.load(file)
		for song_name, video_id in used_songs.items():
			print(f"{song_name:>50} | {video_id}")

#===================================================#
# End Functions #

#input for mode select
answer = False
while answer != "1" and answer != "2":
	print("1. Add New Songs From File\n2. Display Used Songs")
	answer = input("> ")

#decision made
if answer == "1":
	add_new_songs()
elif answer == "2":
	show_used_songs()
else:
	pass