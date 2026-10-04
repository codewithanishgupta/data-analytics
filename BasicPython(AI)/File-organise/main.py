import os
import shutil


# Folder path you want to organize
FOLDER_PATH = os.getcwd()  # Current working directory

# File type mapping
FILE_TYPES = {
    'Images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.webp',".ico"],
    'Documents': ['.pdf', '.docx', '.doc', '.txt', '.xlsx', '.pptx', '.md',".exe",".winmd"],
    'Audio': ['.mp3', '.wav', '.aac', '.flac'], 
    'Videos': ['.mp4', '.avi', '.mov', '.mkv'],
    'Archives': ['.zip', '.rar', '.tar', '.gz'],
    'Scripts': ['.js', '.sh', '.bat'],
}

# Create folders if they don't exist
for folder in FILE_TYPES.keys(): # Create folders for each file type
    folder_path = os.path.join(FOLDER_PATH, folder)
    if not os.path.exists(folder_path): 
        os.makedirs(folder_path)

# Organize files
for file in os.listdir(FOLDER_PATH):
    file_path = os.path.join(FOLDER_PATH, file)

     # Skip folders
    if os.path.isdir(file_path):
         continue
     
     # Get file extension
    #  print(os.path.splitext(file))
    file_ext = os.path.splitext(file)[1].lower()

    for folder, extensions in FILE_TYPES.items(): 
         if file_ext in extensions:
            shutil.move(file_path, os.path.join(FOLDER_PATH, folder, file))

print("Files organized successfully✅") 