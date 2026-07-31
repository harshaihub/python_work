import os, shutil

def organize_files(folder):
    for filename in os.listdir(folder):
        if filename.endswith(('.png', '.jpg')):
            shutil.move(os.path.join(folder, filename), os.path.join(folder, 'Images', filename))
        elif filename.endswith(('.pdf', '.docx')):
            shutil.move(os.path.join(folder, filename), os.path.join(folder, 'Documents', filename))
        elif filename.endswith(('.mp4', '.mkv')):
            shutil.move(os.path.join(folder, filename), os.path.join(folder, 'Videos', filename))

organize_files("C:/Users/Harshvardhan/Downloads")
