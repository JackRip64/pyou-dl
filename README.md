# pyou-dl
Youtube audio downloader for Linux utilizing youtube-dl application

IMPORTANT!!!
------------
This is a program is for Linux. This will not work cross platform.
It also uses youtube-dl, so make sure that is installed with "pip3 install youtube-dl".
Do not use apt to install, youtube-dl will throw an exception saying it can't download videos for some reason.

USING THE PROGRAM
-----------------
Use python3 to run the pyou-dl.py.

Option 1 will take every song name in the input file (songs_to_add.txt by default) and download it to the "../" directory by default.

The songs in the input file should be formatted so that there is no punctuation except for "-".

The songs should be written in a way that makes it easy for the search to return the desired video as the first result of a search.
 - (EX. Thunderstruck -- ACDC)
 - (EX. Sweet Child O Mine -- Guns N Roses)
  
The song names taken are stored in the used_songs.pkl file along with their video ID's.

You can view the contents of the used_songs.pkl by selecting option 2.

The purpose of the file it to minimize redundant songs while downloading as well as making it easy to backup these songs.

This means you can delete all song files and still keep relevant data for downloading using the unpacker (not yet included).
