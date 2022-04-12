import os
import re
import stepmania_song

def parse_all(folder):
    '''
    Parse every file in a given directory
    '''

    # Main variables
    ext_sm = ".sm"
    ext_ssc = ".ssc"
    ext_dwi = ".dwi"
    ext_ignore = [".jpg", ".mp3", ".png", ".gif", ".lrc", ".sprite", ".xml", ".ogg", ".ini",
                  ".model", ".db", ".bmp", ".jpeg", ".avi", ".txt", ".crs", ".xstep"]
    ext_delete = [".!jpg", ".!sm", ".zip", ".smzip", ".old", ".mpg", ".sgp", ".html", ".bms",
                  ".dsx", ".ds", ".bme"]
    all_songs_list = []

    # Populate list with all songs
    for root, dirs, files in os.walk(folder):
        for name in files:
            full_path = os.path.join(root, name)
            split_ext = os.path.splitext(name)
            ext = split_ext[1].lower()

            next_song = find_if_song_exists(root, all_songs_list)
            find_if_song_is_a_subfolder(folder, next_song)

            if ext in [ext_sm, ext_ssc, ext_dwi]:
                next_song.add_filename(full_path)
                next_song.mark_has_song_file()
                all_lines = read_all_lines(next_song, full_path)

                if ext_sm == ext:
                    parse_sm_file(next_song, name, all_lines)

                elif ext_ssc == ext:
                    parse_ssc_file(next_song, name, all_lines)

                elif ext_dwi == ext:
                    parse_dwi_file(next_song, name, all_lines)

            elif ext in ext_delete:
                next_song.add_filename_for_deletion(full_path)

            elif ext in ext_ignore:
                next_song.add_filename(full_path)

            else:
                next_song.add_unexpected_file(full_path)

    mark_songs_for_deletion(all_songs_list)

    return all_songs_list

def find_if_song_exists(root, all_songs_list):
    '''
    See if song already exists in song files.  Create new song class if one does
    not exist for the song
    '''
    song_found = False

    for next_song in all_songs_list:
        if next_song.get_root_path() == root:
            song_found = True
            break

    if not song_found:
        next_song = stepmania_song.stepmania_song(root)
        all_songs_list.append(next_song)

    return next_song

def find_if_song_is_a_subfolder(folder, next_song):
    '''
    Regular depth of a song folder is 2, if it is at least that deep from the root
    folder, mark the song as a subfolder
    '''
    depth_of_folder = len(folder.split('\\'))
    depth_of_song = len(next_song.get_root_path().split('\\'))

    if depth_of_song > (depth_of_folder + 2):
        # Folder of structure of song is too deep
        next_song.mark_song_as_subfolder()

def read_all_lines(next_song, full_path):
    '''
    Read lines of file using utf8 or cp852 encoding
    '''
    all_lines = None

    try:
        with open(full_path, 'r', encoding='utf8') as next_file:
            all_lines = next_file.readlines()
    except:
        try:
            with open(full_path, 'r', encoding='cp852') as next_file:
                all_lines = next_file.readlines()
        except:
            next_song.issue_hit("readlines (utf and cp852) issue with file: " + full_path)

    return all_lines

def parse_sm_file(next_song, name, all_lines):
    '''
    Parse sm file to gather difficulty data
    '''
    try:
        for next_line in range(len(all_lines)):
            next_pattern =  re.findall("(#NOTES)", all_lines[next_line])
            if len(next_pattern) != 0:
                next_difficulty = re.findall("\W*(.*?):", all_lines[next_line + 3])
                next_rating = re.findall("\W*(.*?):", all_lines[next_line + 4])
                next_song.add_difficulty(next_difficulty[0], next_rating[0])
    except:
        next_song.issue_hit("sm issue with file: " + name)

def parse_ssc_file(next_song, name, all_lines):
    '''
    Parse ssc file to gather difficulty data
    '''
    next_difficulty = False
    next_rating = False
    try:
        for next_line in all_lines:
            find_difficulty =  re.findall("#DIFFICULTY:(.*?);", next_line)
            if (len(find_difficulty) != 0):
                next_difficulty = find_difficulty[0]

            find_rating = re.findall("#METER:(.*?);", next_line)
            if (len(find_rating) != 0):
                next_rating = find_rating[0]

            if (next_difficulty is not False) and (next_rating is not False):
                next_song.add_difficulty(next_difficulty, next_rating)
                next_difficulty = False
                next_rating = False
    except:
        next_song.issue_hit("ssc issue with file: " + name)

def parse_dwi_file(next_song, name, all_lines):
    '''
    Parse dwi file to gather difficulty data
    '''
    try:
        for next_line in all_lines:
            next_pattern =  re.findall("#SINGLE:(.*?):(.*?):", next_line)
            if len(next_pattern) !=0:
                next_song.add_difficulty(next_pattern[0][0], next_pattern[0][1])
    except:
        next_song.issue_hit("dwi issue with file: " + name)

def mark_songs_for_deletion(all_songs_list):
    '''
    Mark song for deletion if songs lowest difficulty is above 6
    '''
    for next_song in all_songs_list:
        all_difficulty_data = next_song.get_difficulty()
        if all_difficulty_data != {}:
            for nextDifficulty in all_difficulty_data.keys():
                if int(all_difficulty_data[nextDifficulty]) < next_song.get_lowest_diff():
                    next_song.set_lowest_difficulty(int(all_difficulty_data[nextDifficulty]))

        if next_song.get_lowest_diff() > 6:
            next_song.mark_delete()