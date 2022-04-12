import folder_parser
import debug_data
import folder_actions

# Debug / Release
debug = True
release = False

# Folder path
songs_folder = "C:\\Users\\craig\\Downloads\\NewSongs"
debug_folder = "C:\\Users\\craig\\Downloads\\Output\\"

# ----------------------- Populate data -----------------------
all_songs_list = folder_parser.parse_all(songs_folder)
# -------------------------------------------------------------

# -------------------- Generate Debug info --------------------
debug_data.debug_steps(all_songs_list, debug_folder, debug)
# -------------------------------------------------------------

# --------------- Actually Modify Song Folders ----------------
folder_actions.release_steps(all_songs_list, release)
# -------------------------------------------------------------
