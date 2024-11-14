import os
import shutil
import argparse
from json import loads

# FileOrganizer class to organize files based on their extensions.


class FileOrganizer:

    def __init__(self):
        # Load the file type mappings from a JSON configuration file.
        with open("file_types.json") as f:
            self.FILE_TYPES = loads(f.read())

    def move_file(self,
                  root_src_dir: str,
                  file_name: str,
                  root_dst_dir: str,
                  _cache={}):
        # Get the file extension.
        ext = f".{file_name.split('.')[-1]}"

        # Skip if the file extension is not defined in FILE_TYPES.
        if not self.FILE_TYPES.get(ext):
            return 1

        # Construct source file path.
        f_src = root_src_dir + file_name

        # Check if the destination directory for this extension is cached.
        if ext in _cache:
            shutil.move(f_src, _cache[ext])
            return 0

        # Define the destination folder for this extension.
        f_dst = root_dst_dir + self.FILE_TYPES[ext]

        # Create the folder if it doesn't exist.
        if not os.path.exists(f_dst):
            os.mkdir(f_dst)

        # Cache the destination folder path for reuse.
        _cache[ext] = f_dst
        # Move the file to the designated folder.
        shutil.move(f_src, f_dst)
        return 0

    def organize(self):
        # Setup argparse for command-line arguments.
        parser = argparse.ArgumentParser(
            description="Organize files based on file type extensions.")

        parser.add_argument("-rs",
                            "--rootsrc",
                            help="specify the source directory to organize")
        parser.add_argument("-rd",
                            "--rootdst",
                            help="specify the destination directory")

        # Parse arguments.
        args = parser.parse_args()

        # Assign root directories based on arguments.
        root_src_dir = args.rootsrc
        root_dst_dir = args.rootdst

        # Validate the source directory.
        if not root_src_dir:
            parser.print_help()
            return
        elif not os.path.isdir(root_src_dir):
            print("Source directory doesn't exist")
            return

        # Set destination directory to source directory if none specified.
        if not root_dst_dir:
            root_dst_dir = root_src_dir
        elif root_dst_dir and not os.path.isdir(root_dst_dir):
            print("Destination directory doesn't exist")
            return

        # Ensure directory paths end with '/' for consistency.
        root_src_dir += "" if root_src_dir.endswith("/") else "/"
        root_dst_dir += "" if root_dst_dir.endswith("/") else "/"

        # Get a list of files in the source directory.
        src_dir_content = os.fwalk(root_src_dir)
        src_dir_files = list(src_dir_content)[0][2]

        # Move each file based on its extension.
        for file_name in src_dir_files:
            self.move_file(root_src_dir, file_name, root_dst_dir)


# Run the organizer.
if __name__ == "__main__":
    organizer = FileOrganizer()
    organizer.organize()
