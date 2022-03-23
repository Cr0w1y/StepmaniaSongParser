import os
import shutil

def generateFileOfSongDifficulties(allStepmaniaFiles, debugFolder):
    # Populate file with all difficulty info
    with open(debugFolder + "Difficulty_Data.txt", "w") as difficultyFile:
        for nextStepmaniaSong in allStepmaniaFiles:
            allDifficultyData = nextStepmaniaSong.getDifficulty()
            if allDifficultyData != {}:
                difficultyFile.write(nextStepmaniaSong.getRootPath() + "\n")
                for nextDifficulty in allDifficultyData.keys():
                    difficultyFile.write("\t" + nextDifficulty + " " + allDifficultyData[nextDifficulty] + "\n")

def generateFileOfIssues(allStepmaniaFiles, debugFolder):
    # Populate file with all issues hit when parsing song files
    with open(debugFolder + "IssuesData.txt", "w") as issuesFile:
        for nextStepmaniaSong in allStepmaniaFiles:
            for nextIssue in nextStepmaniaSong.getIssues():
                issuesFile.write(nextIssue + "\n")

def generateFileOfSongsToDelete(allStepmaniaFiles, debugFolder):
    # Populate file with all songs that meet deletion specifications
    with open(debugFolder + "SongsToRemove.txt", "w") as removeSongs:
        for nextStepmaniaSong in allStepmaniaFiles:
            if nextStepmaniaSong.shouldDelete():
                removeSongs.write(nextStepmaniaSong.getRootPath() + "\n")
                removeSongs.write("\tLowest value is: " + str(nextStepmaniaSong.getLowestDifficulty()) + "\n")

def generateFileOfAllFiles(allStepmaniaFiles, debugFolder):
    # Populate file with all songs that meet deletion specifications
    with open(debugFolder + "AllFiles.txt", "w") as allFile:
        for nextStepmaniaSong in allStepmaniaFiles:
            allFile.write(nextStepmaniaSong.getRootPath() + "\n")
            for nextFile in nextStepmaniaSong.getFiles():
                allFile.write("\t" + nextFile + "\n")

def generateFileOfSongsWithNoSongFiles(allStepmaniaFiles, debugFolder):
    # Populate file with song classes that do not have songs in them
    with open(debugFolder + "SongsWithNoSongFiles.txt", "w") as noSongsFile:
        for nextStepmaniaSong in allStepmaniaFiles:
            if nextStepmaniaSong.hasNoSongFiles():
                noSongsFile.write(nextStepmaniaSong.getRootPath() + "\n")

def generateFileOfSubSubFolderSongs(allStepmaniaFiles, debugFolder):
    # Populate file with song classes that do not have songs in them
    with open(debugFolder + "SubSubFolderSongs.txt", "w") as isSubSubFolder:
        for nextStepmaniaSong in allStepmaniaFiles:
            if nextStepmaniaSong.isSongSubSubFolder():
                isSubSubFolder.write(nextStepmaniaSong.getRootPath() + "\n")

def generateFileOdSubSubFolderAndNoSongOverlap(allStepmaniaFiles, debugFolder):
    # Populate file with song classes that do not have songs in them
    with open(debugFolder + "Overlap.txt", "w") as isSubSubFolder:
        for nextStepmaniaSong in allStepmaniaFiles:
            if nextStepmaniaSong.isSongSubSubFolder() and nextStepmaniaSong.hasNoSongFiles():
                isSubSubFolder.write(nextStepmaniaSong.getRootPath() + "\n")

def RemoveUnwantedFiles(allStepmaniaFiles):
    # Remove every unwanted file
    for nextStepmaniaSong in allStepmaniaFiles:
        for nextFile in nextStepmaniaSong.getFilesForDeletion():
            os.remove(nextFile)

def RemoveUnwantedSubFolders(allStepmaniaFiles):
    # Remove any subfolder that does not have songs
    for nextStepmaniaSong in allStepmaniaFiles:
        if nextStepmaniaSong.isSongSubSubFolder() and nextStepmaniaSong.hasNoSongFiles():
            for nextFile in nextStepmaniaSong.getFiles():
                os.remove(nextFile)
            os.rmdir(nextStepmaniaSong.getRootPath())

def RemoveUnwantedSongs(allStepmaniaFiles):
    # Remove every unwanted song
    for nextStepmaniaSong in allStepmaniaFiles:
        if nextStepmaniaSong.shouldDelete() and (nextStepmaniaSong.getLowestDifficulty() != 1000000):
            for nextFile in nextStepmaniaSong.getFiles():
                os.remove(nextFile)
            os.rmdir(nextStepmaniaSong.getRootPath())

def DebugSteps(allStepmaniaFiles, debugFolder, debug):
    if debug:
        generateFileOfAllFiles(allStepmaniaFiles, debugFolder)
        generateFileOfIssues(allStepmaniaFiles, debugFolder)
        generateFileOfSongDifficulties(allStepmaniaFiles, debugFolder)
        generateFileOfSongsToDelete(allStepmaniaFiles, debugFolder)
        generateFileOfSongsWithNoSongFiles(allStepmaniaFiles, debugFolder)
        generateFileOfSubSubFolderSongs(allStepmaniaFiles, debugFolder)
        generateFileOdSubSubFolderAndNoSongOverlap(allStepmaniaFiles, debugFolder)

def ReleaseSteps(allStepmaniaFiles, release):
    if release:
        RemoveUnwantedFiles(allStepmaniaFiles)
        RemoveUnwantedSubFolders(allStepmaniaFiles)
        RemoveUnwantedSongs(allStepmaniaFiles)