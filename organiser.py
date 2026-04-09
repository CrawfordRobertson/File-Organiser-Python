import os
import shutil

# Change this to your folder
SOURCE_FOLDER = "C:/Users/YourName/Downloads"

FILE_TYPES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif"],
    "Videos": [".mp4", ".mkv", ".avi"],
    "Documents": [".pdf", ".docx", ".txt"]
}

def organise_files():
    for filename in os.listdir(SOURCE_FOLDER):
        file_path = os.path.join(SOURCE_FOLDER, filename)

        if os.path.isfile(file_path):
            for folder, extensions in FILE_TYPES.items():
                if filename.lower().endswith(tuple(extensions)):
                    target_folder = os.path.join(SOURCE_FOLDER, folder)

                    if not os.path.exists(target_folder):
                        os.makedirs(target_folder)

                    shutil.move(file_path, os.path.join(target_folder, filename))
                    print(f"Moved {filename} → {folder}")
                    break

if __name__ == "__main__":
    organise_files()
