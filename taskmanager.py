import os
import shutil
source_folder = "images"
destination_folder = "jpg_files"
if not os.path.exists(destination_folder):
    os.mkdir(destination_folder)
for file in os.listdir(source_folder):
    if file.lower().endswith(".jpg"):
        source = os.path.join(source_folder, file)
        destination = os.path.join(destination_folder, file)
        shutil.move(source, destination)
        print(file, "moved successfully")
print("Task completed!")