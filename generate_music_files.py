import os

#Remove old files
try:
    os.remove("test.txt")
except OSError:
    pass

#All files
all_files = os.listdir()

#Find only .ogg files
ogg_files = []
for file in all_files:
    if (file.lower().endswith('.ogg')):
        ogg_files.append(file)

print(ogg_files)

# 1/2
# songs.txt file
new_songs_file = open("songs.txt", "w+")

# 2/2
# music.asset file
new_music_assets_file = open("music.asset", "w+")

indent = "  "

for file in ogg_files:
    # songs.txt
    filename, extension = os.path.splitext(file)
    print("Filename: " + filename)
    print("Extension: " + extension)
    new_songs_file.write("song = {"+"\n")
    new_songs_file.write(indent + "name = "+ '"'+ filename + '"' + "\n")
    new_songs_file.write(indent + "chance = {"+"\n")
    new_songs_file.write(indent + indent + "modifer = {"+"\n")
    new_songs_file.write(indent + indent + indent + "factor = 1"+"\n")
    new_songs_file.write(indent + indent + "}"+"\n")
    new_songs_file.write(indent + "}"+"\n")
    new_songs_file.write("}"+"\n")

    # music.asset file
    new_music_assets_file.write("music = {" + "\n")
    new_music_assets_file.write(indent + "name = " + '"' + filename + '"' + "\n")
    new_music_assets_file.write(indent + "file = " + '"' + filename + extension + '"' + "\n")
    new_music_assets_file.write("}" + "\n")


