import os
import shutil

# Define a dict with folder paths and respective image counts
FOLDER_PATHS = {"Object 1": {"1_whiteBg": 37,
                             "1_greenBg": 14,
                             "1_blackBg": 12},
                "Object 2": {"2_whiteBg": 31,
                             "2_greenBg": 16,
                             "2_blackBg": 12},
                "Object 3": {"3_whiteBg": 38,
                             "3_greenBg": 17,
                             "3_blackBg": 13},
                "Object 4": {"4_whiteBg": 72,
                             "4_greenBg": 17,
                             "4_blackBg": 10}}

# Function to rename image files in a folder according to specified counts
def rename_images(folder_path, counts):
    count = {img_type: 1 for img_type in counts.keys()}
    
    # Retrieve all JPEG files in the folder
    files = sorted([f for f in os.listdir(folder_path) if f.lower().endswith('.jpg')])
    
    for img, count in counts.items():
        # Rename each image according to the specified count
        for old_name in files[:count]:
            _, ext = os.path.splitext(old_name)
            new_name = f"{img}_{count[img]:02d}{ext.lower()}"
            old_path = os.path.join(folder_path, old_name)
            new_path = os.path.join(folder_path, new_name)
            
            print(f"Renaming {old_path} to {new_path}")
            shutil.move(old_path, new_path)
            
            count[img] += 1
        
        # Remove processed files from the list
        files = files[count:]


# Iterate over each object folder and then rename all image files

for obj, counts in FOLDER_PATHS.items():
    folder_path = os.path.join(os.getcwd(), obj)
    rename_images(folder_path, counts)

print("Image renaming process completed :D")