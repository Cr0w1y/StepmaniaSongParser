import os
import re
import StepmaniaSong

def parseAll(folder):
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
    allStepmaniaFiles = []

    # Populate list with all songs
    for root, dirs, files in os.walk(folder):
        for name in files:
            full_path = os.path.join(root, name)
            split_ext = os.path.splitext(name)
            ext = split_ext[1].lower()

            nextStepmaniaSong = findIfSongExists(root, allStepmaniaFiles)
            findIfSongIsSubSubFolder(folder, nextStepmaniaSong)

            if ext in [ext_sm, ext_ssc, ext_dwi]:
                nextStepmaniaSong.addFileName(full_path)
                nextStepmaniaSong.markHasSongFile()
                all_lines = readAllLines(nextStepmaniaSong, full_path)

                if ext_sm == ext:
                    parseSm(nextStepmaniaSong, name, all_lines)

                elif ext_ssc == ext:
                    parseSsc(nextStepmaniaSong, name, all_lines)

                elif ext_dwi == ext:
                    parseDwi(nextStepmaniaSong, name, all_lines)

            elif ext in ext_delete:
                nextStepmaniaSong.addFileNameForDeletion(full_path)

            elif ext in ext_ignore:
                nextStepmaniaSong.addFileName(full_path)

            else:
                nextStepmaniaSong.addUnexpectedExt(full_path)

    markSongsForDeletion(allStepmaniaFiles)

    return allStepmaniaFiles

def findIfSongExists(root, allStepmaniaFiles):
    # See if song already exists in song files
    songFound = False

    for nextStepmaniaSong in allStepmaniaFiles:
        if nextStepmaniaSong.getRootPath() == root:
            songFound = True
            break

    # Create new song class if one does not exist for the song
    if not songFound:
        nextStepmaniaSong = StepmaniaSong.StepmaniaSong(root)
        allStepmaniaFiles.append(nextStepmaniaSong)

    return nextStepmaniaSong

def findIfSongIsSubSubFolder(folder, nextStepmaniaSong):
    # If the depth of a song folder is more that 2 folders, mark the song as so
    depthOfFolder = len(folder.split('\\'))
    depthOfSong = len(nextStepmaniaSong.getRootPath().split('\\'))

    if depthOfSong > (depthOfFolder + 2):
        # Folder of structure of song is too deep
        nextStepmaniaSong.markSongAsSubSubFolder()

def readAllLines(nextStepmaniaSong, full_path):
    all_lines = None

    try:
        with open(full_path, 'r', encoding='utf8') as next_file:
            all_lines = next_file.readlines()
    except:
        try:
            with open(full_path, 'r', encoding='cp852') as next_file:
                all_lines = next_file.readlines()
        except:
            nextStepmaniaSong.issueHit("readlines (utf and cp852) issue with file: " + full_path)

    return all_lines

def parseSm(nextStepmaniaSong, name, all_lines):
    # Parse sm file extension
    try:
        for next_line in range(len(all_lines)):
            next_pattern =  re.findall("(#NOTES)", all_lines[next_line])
            if len(next_pattern) != 0:
                next_difficulty = re.findall("\W*(.*?):", all_lines[next_line + 3])
                next_rating = re.findall("\W*(.*?):", all_lines[next_line + 4])
                nextStepmaniaSong.addDifficulty(next_difficulty[0], next_rating[0])
    except:
        nextStepmaniaSong.issueHit("sm issue with file: " + name)

def parseSsc(nextStepmaniaSong, name, all_lines):
    # Parse ssc file extension
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
                nextStepmaniaSong.addDifficulty(next_difficulty, next_rating)
                next_difficulty = False
                next_rating = False
    except:
        nextStepmaniaSong.issueHit("ssc issue with file: " + name)

def parseDwi(nextStepmaniaSong, name, all_lines):
    # Parse ssc file extension
    try:
        for next_line in all_lines:
            next_pattern =  re.findall("#SINGLE:(.*?):(.*?):", next_line)
            if len(next_pattern) !=0:
                nextStepmaniaSong.addDifficulty(next_pattern[0][0], next_pattern[0][1])
    except:
        nextStepmaniaSong.issueHit("dwi issue with file: " + name)

def markSongsForDeletion(allStepmaniaFiles):
    # Mark song for deletion if songs lowest difficulty is above 6
    for nextStepmaniaSong in allStepmaniaFiles:
        allDifficultyData = nextStepmaniaSong.getDifficulty()
        if allDifficultyData != {}:
            for nextDifficulty in allDifficultyData.keys():
                if int(allDifficultyData[nextDifficulty]) < nextStepmaniaSong.getLowestDifficulty():
                    nextStepmaniaSong.setLowestDifficulty(int(allDifficultyData[nextDifficulty]))

        if nextStepmaniaSong.getLowestDifficulty() > 6:
            nextStepmaniaSong.markDelete()