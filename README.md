# pyou-dl
Youtube audio downloader for Linux utilizing youtube-dl application

IMPORTANT!!!
------------
This is a program is for Linux. This will not work cross platform.
It uses pickle, so if it's not already installed, use "pip3 install pickle"
It also uses youtube-dl, so make sure that is installed with "pip3 install youtube-dl".
Do not use apt to install, youtube-dl will throw an exception saying it can't download videos for some reason.

USING THE PROGRAM
-----------------
Use python3 to run the pyou-dl.py.

Option 1 will take every song name in the input file (songs_to_add.txt by default) and download it to the "../" directory by default.

The songs in the input file should be formatted so that there is no punctuation except for "-" as well as capitalizing every word.

Capitalizing and using no punctuation will help reduce redundancies.

The songs should be written in a way that makes it easy for the search to return the desired video as the first result of a search.
 - (EX. Thunderstruck -- ACDC)
 - (EX. Sweet Child O Mine -- Guns N Roses)
  
The song names taken are stored in the used_songs.pkl file along with their video ID's.

You can view the contents of the used_songs.pkl by selecting option 2.

The purpose of the file it to minimize redundant songs while downloading as well as making it easy to backup these songs.

This means you can delete all song files and still keep relevant data for downloading using the unpacker (not yet included).

CONSTANTS
---------
Feel free to change the constants to what you wish if you have something else in mind.

As said before, it defaults to downloading songs to the parent directory of the current directory.

The default values for the input and pickle file are also in the constants section of the py file.

All of these can be changed, but if you happen to delete the provided pickle file, you will need to set up another properly.

This can be done by running python3 and typing "import pickle" then "pickle.dump({}, open(your_file_name_here, "wb"))"
