import os
import shutil


def delete_characters_in_files(directory_path, num_chars_to_delete):
    if not os.path.isdir(directory_path):
        print(f"Error: The directory '{directory_path}' does not exist.")
        return

    for filename in os.listdir(directory_path):
        file_path = os.path.join(directory_path, filename)
      
        if os.path.isfile(file_path):
            try:
                with open(file_path, 'r', encoding='utf-8') as file:
                    content = file.read()

                modified_content = content[num_chars_to_delete:]

                with open(file_path, 'w', encoding='utf-8') as file:
                    file.write(modified_content)

                print(f"Successfully modified: {filename}")

            except Exception as e:
                print(f"Error processing file '{filename}': {str(e)}")

    print("File modification complete.")




def delete_folders(directory, folders_to_delete):
    """
    Deletes a list of folders in the specified directory.

    :param directory: The path to the directory containing the folders.
    :param folders_to_delete: A list of folder names to delete.
    """
    for folder in folders_to_delete:
        folder_path = os.path.join(directory, folder)
        if os.path.exists(folder_path) and os.path.isdir(folder_path):
            shutil.rmtree(folder_path)
            print(f"Deleted folder: {folder_path}")
        else:
            print(f"Folder not found: {folder_path}")
