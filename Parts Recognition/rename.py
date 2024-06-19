import os
import shutil

FOLDER_PATHS = {
    "Object 1": {
        "0_whiteBg": 37,
        "1_greenBg": 14,
        "2_blackBg": 12
    },
    "Object 2": {
        "0_whiteBg": 31,
        "1_greenBg": 16,
        "2_blackBg": 12
    },
    "Object 3": {
        "0_whiteBg": 38,
        "1_greenBg": 17,
        "2_blackBg": 13
    },
    "Object 4": {
        "0_whiteBg": 72,
        "1_greenBg": 17,
        "2_blackBg": 10
    }
}

def rename_images(folder_path, counts):
    counters = {img_type: 1 for img_type in counts.keys()}
    
    files = sorted([f for f in os.listdir(folder_path) if f.lower().endswith('.jpg')])
    
    for img_type, count in counts.items():
        for old_name in files[:count]:
            _, ext = os.path.splitext(old_name)
            new_name = f"{img_type}_{counters[img_type]:02d}{ext.lower()}"
            old_path = os.path.join(folder_path, old_name)
            new_path = os.path.join(folder_path, new_name)
            
            shutil.move(old_path, new_path)
            print(f"Renamed {old_path} to {new_path}")
            
            counters[img_type] += 1
        
        files = files[count:]

for obj, counts in FOLDER_PATHS.items():
    folder_path = os.path.join(os.getcwd(), obj)
    rename_images(folder_path, counts)

print("Image renaming completed.")
