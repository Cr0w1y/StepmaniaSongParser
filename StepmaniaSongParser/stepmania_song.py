class stepmania_song(object):
    def __init__(self, root_path):
        self.root_path = root_path
        self.all_filenames_list = []
        self.filenames_delete_list = []
        self.weird_ext = []
        self.difficulty_dict = {}
        self.lowest_diff = 1000000
        self.delete = False
        self.no_song_files = True
        self.is_sub_folder = False
        self.issues_hit = []

    def add_filename(self, fileName):
        self.all_filenames_list.append(fileName)

    def add_filename_for_deletion(self, fileName):
        self.filenames_delete_list.append(fileName)

    def add_unexpected_ext(self, newExt):
        self.weird_ext.append(newExt)

    def add_difficulty(self, difficulty, rating):
        self.difficulty_dict[difficulty] = rating

    def set_lowest_difficulty(self, lowestDiff):
        self.lowest_diff = lowestDiff

    def mark_delete(self):
        self.delete = True

    def mark_has_song_file(self):
        self.no_song_files = False

    def mark_song_as_subfolder(self):
        self.is_sub_folder = True

    def issue_hit(self, issueText):
        self.issues_hit.append(issueText)

    def get_issues(self):
        return self.issues_hit

    def get_root_path(self):
        return self.root_path

    def get_difficulty(self):
        return self.difficulty_dict

    def get_lowest_diff(self):
        return self.lowest_diff

    def should_delete(self):
        return self.delete

    def has_no_song_files(self):
        return self.no_song_files

    def is_song_sub_subfolder(self):
        return self.is_sub_folder

    def get_files(self):
        return self.all_filenames_list

    def get_files_for_deletion(self):
        return self.filenames_delete_list

    def get_unexpected_ext(self):
        return self.weird_ext