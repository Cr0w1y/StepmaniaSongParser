import os
import shutil

def generate_file_of_song_difficulties(all_songs_list, debug_folder):
    # Populate file with all difficulty info
    with open(debug_folder + "Difficulty_Data.txt", "w") as difficulty_file:
        for next_song in all_songs_list:
            all_difficulty_data = next_song.get_difficulty()
            if all_difficulty_data != {}:
                difficulty_file.write(next_song.get_root_path() + "\n")
                for next_difficulty in all_difficulty_data.keys():
                    difficulty_file.write("\t" + next_difficulty + " " + all_difficulty_data[next_difficulty] + "\n")

def generate_file_of_issues(all_songs_list, debug_folder):
    # Populate file with all issues hit when parsing song files
    with open(debug_folder + "IssuesData.txt", "w") as issues_file:
        for next_song in all_songs_list:
            for next_issue in next_song.get_issues():
                issues_file.write(next_issue + "\n")

def generate_file_of_songs_to_delete(all_songs_list, debug_folder):
    # Populate file with all songs that meet deletion specifications
    with open(debug_folder + "SongsToRemove.txt", "w") as remove_songs:
        for next_song in all_songs_list:
            if next_song.should_delete():
                remove_songs.write(next_song.get_root_path() + "\n")
                remove_songs.write("\tLowest value is: " + str(next_song.get_lowest_diff()) + "\n")

def generate_file_of_all_files(all_songs_list, debug_folder):
    # Populate file with all songs that meet deletion specifications
    with open(debug_folder + "AllFiles.txt", "w") as all_file:
        for next_song in all_songs_list:
            all_file.write(next_song.get_root_path() + "\n")
            for next_file in next_song.get_files():
                all_file.write("\t" + next_file + "\n")

def generate_file_of_songs_with_no_song_files(all_songs_list, debug_folder):
    # Populate file with song classes that do not have songs in them
    with open(debug_folder + "SongsWithNoSongFiles.txt", "w") as no_songs_file:
        for next_song in all_songs_list:
            if next_song.has_no_song_files():
                no_songs_file.write(next_song.get_root_path() + "\n")

def generate_file_of_sub_subfolder_songs(all_songs_list, debug_folder):
    # Populate file with song classes that do not have songs in them
    with open(debug_folder + "SubSubFolderSongs.txt", "w") as is_sub_subfolder:
        for next_song in all_songs_list:
            if next_song.is_song_sub_subfolder():
                is_sub_subfolder.write(next_song.get_root_path() + "\n")

def generate_file_of_sub_subfolder_and_no_song_overlap(all_songs_list, debug_folder):
    # Populate file with song classes that do not have songs in them
    with open(debug_folder + "Overlap.txt", "w") as is_sub_subfolder:
        for next_song in all_songs_list:
            if next_song.is_song_sub_subfolder() and next_song.has_no_song_files():
                is_sub_subfolder.write(next_song.get_root_path() + "\n")

def debug_steps(all_songs_list, debug_folder, debug):
    if debug:
        generate_file_of_all_files(all_songs_list, debug_folder)
        generate_file_of_issues(all_songs_list, debug_folder)
        generate_file_of_song_difficulties(all_songs_list, debug_folder)
        generate_file_of_songs_to_delete(all_songs_list, debug_folder)
        generate_file_of_songs_with_no_song_files(all_songs_list, debug_folder)
        generate_file_of_sub_subfolder_songs(all_songs_list, debug_folder)
        generate_file_of_sub_subfolder_and_no_song_overlap(all_songs_list, debug_folder)