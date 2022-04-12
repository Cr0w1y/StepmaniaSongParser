def remove_unwanted_files(all_songs_list):
    # Remove every unwanted file
    for next_song in all_songs_list:
        for next_file in next_song.get_files_for_deletion():
            os.remove(next_file)

def remove_unwanted_subfolders(all_songs_list):
    # Remove any subfolder that does not have songs
    for next_song in all_songs_list:
        if next_song.is_song_sub_subfolder() and next_song.has_no_song_files():
            for next_file in next_song.get_files():
                os.remove(next_file)
            os.rmdir(next_song.get_root_path())

def remove_unwanted_songs(all_songs_list):
    # Remove every unwanted song
    for next_song in all_songs_list:
        if next_song.should_delete() and (next_song.get_lowest_diff() != 1000000):
            for next_file in next_song.get_files():
                os.remove(next_file)
            os.rmdir(next_song.get_root_path())

def release_steps(all_songs_list, release):
    if release:
        remove_unwanted_files(all_songs_list)
        remove_unwanted_subfolders(all_songs_list)
        remove_unwanted_songs(all_songs_list)