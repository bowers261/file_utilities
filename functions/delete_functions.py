import os
import shutil

def delete_folders(directory, folders_to_delete):
    for folder in folders_to_delete:
        folder_path = os.path.join(directory, folder)
        if os.path.exists(folder_path) and os.path.isdir(folder_path):
            shutil.rmtree(folder_path)
            print(f"Deleted folder: {folder_path}")
        else:
            print(f"Folder not found: {folder_path}")
