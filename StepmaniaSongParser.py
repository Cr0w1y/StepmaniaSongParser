import FolderParser
import HelperFunctions

# Debug / Release
debug = True
release = False

# Folder path
folderContainingSongs = "C:\\Users\\craig\\Downloads\\NewSongs"
debugFolder = "C:\\Users\\craig\\Downloads\\Output\\"

# ----------------------- Populate data -----------------------
allStepmaniaFiles = FolderParser.parseAll(folderContainingSongs)
# -------------------------------------------------------------

# -------------------- Generate Debug info --------------------
HelperFunctions.DebugSteps(allStepmaniaFiles, debugFolder, debug)
# -------------------------------------------------------------

# --------------- Actually Modify Song Folders ----------------
HelperFunctions.ReleaseSteps(allStepmaniaFiles, release)
# -------------------------------------------------------------
