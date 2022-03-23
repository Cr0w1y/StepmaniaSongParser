class StepmaniaSong:
    def __init__(self, rootPath):
        self.rootPath = rootPath
        self.fileNames = []
        self.fileNamesForDeletion = []
        self.unexpectedExt = []
        self.DifficultyDict = {}
        self.lowestDifficulty = 1000000
        self.delete = False
        self.noSongFiles = True
        self.isSubSubFolder = False
        self.issues = []

    def addFileName(self, fileName):
        self.fileNames.append(fileName)

    def addFileNameForDeletion(self, fileName):
        self.fileNamesForDeletion.append(fileName)

    def addUnexpectedExt(self, newExt):
        self.unexpectedExt.append(newExt)

    def addDifficulty(self, difficulty, rating):
        self.DifficultyDict[difficulty] = rating

    def setLowestDifficulty(self, lowestDiff):
        self.lowestDifficulty = lowestDiff

    def markDelete(self):
        self.delete = True

    def markHasSongFile(self):
        self.noSongFiles = False

    def markSongAsSubSubFolder(self):
        self.isSubSubFolder = True

    def issueHit(self, issueText):
        self.issues.append(issueText)

    def getIssues(self):
        return self.issues

    def getRootPath(self):
        return self.rootPath

    def getDifficulty(self):
        return self.DifficultyDict

    def getLowestDifficulty(self):
        return self.lowestDifficulty

    def shouldDelete(self):
        return self.delete

    def hasNoSongFiles(self):
        return self.noSongFiles

    def isSongSubSubFolder(self):
        return self.isSubSubFolder

    def getFiles(self):
        return self.fileNames

    def getFilesForDeletion(self):
        return self.fileNamesForDeletion

    def getUnexpectedExt(self):
        return self.unexpectedExt