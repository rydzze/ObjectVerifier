import os
import cv2
import h5py
import numpy as np

FOLDER_PATH = ["Object 1", "Object 2", "Object 3", "Object 4"]
NEW_WIDTH = 750
NEW_HEIGHT = 500

with h5py.File('dataset.h5', 'w') as hdf:
    color_images = []
    labels = []
    
    for obj, path in enumerate(FOLDER_PATH, start=1):
        images = [file for file in os.listdir(path) if file.endswith(('.JPG', '.jpg'))]
        
        for i, img in enumerate(sorted(images)):
            img_path = os.path.join(path, img)
            
            image = cv2.imread(img_path)
            color_img = cv2.resize(image, (NEW_WIDTH, NEW_HEIGHT))
            
            color_images.append(color_img)
            labels.append(obj)
        
        print(f"Object {obj} done ...")
        
    hdf.create_dataset('Objects', data=np.array(color_images), compression="gzip", compression_opts=9)
    hdf.create_dataset('Labels', data=np.array(labels), compression="gzip", compression_opts=9)

print("All images have been stored in the HDF5 dataset.")
