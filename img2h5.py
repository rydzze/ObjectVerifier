import os
import cv2
import h5py
import numpy as np

FOLDER_PATH = ["Object 1", "Object 2", "Object 3", "Object 4"]
NEW_WIDTH = 1500
NEW_HEIGHT = 1000

with h5py.File('dataset.h5', 'w') as hdf:
    for obj, path in enumerate(FOLDER_PATH, start=1):
        images = [file for file in os.listdir(path) if file.endswith(('.JPG', '.jpg'))]
        
        for i, img in enumerate(sorted(images)):
            img_path = os.path.join(path, img)
            
            image = cv2.imread(img_path)
            color_img = cv2.resize(image, (NEW_WIDTH, NEW_HEIGHT))
            grey_img = cv2.cvtColor(color_img, cv2.COLOR_BGR2GRAY)
            
            color_img_array = np.array(color_img)
            grey_img_array = np.array(grey_img)
            color_dataset_name = f'Object{obj}_Color_{i+1:02d}'
            grey_dataset_name = f'Object{obj}_Greyscale_{i+1:02d}'
            
            hdf.create_dataset(color_dataset_name, data=color_img_array, compression="gzip", compression_opts=9)
            hdf.create_dataset(grey_dataset_name, data=grey_img_array, compression="gzip", compression_opts=9)

        print(f"Object {obj} done ...")

print("All images have been stored in the HDF5 dataset.")
