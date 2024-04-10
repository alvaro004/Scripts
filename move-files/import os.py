import os
import shutil

def copy_matching_files(names_to_find, source_dir, destination_dir):
    """Copies files with matching names from a source directory to a destination directory.

    Args:
        names_to_find (list): A list of filenames to search for.
        source_dir (str): The path to the source directory.
        destination_dir (str): The path to the destination directory.
    """

    if not os.path.exists(destination_dir):
        os.makedirs(destination_dir)  # Create the destination folder if it doesn't exist

    for filename in os.listdir(source_dir):
        if filename in names_to_find:
            source_path = os.path.join(source_dir, filename)
            destination_path = os.path.join(destination_dir, filename)
            shutil.copyfile(source_path, destination_path)
            print(f"Copied '{filename}' to '{destination_dir}'")

# Example Usage
names = input("Enter the filenames to search for, separated by commas: ").split(",")
source_folder = input("Enter the path to the source folder: ")
destination_folder = input("Enter the path to the destination folder: ")

copy_matching_files(names, source_folder, destination_folder)
