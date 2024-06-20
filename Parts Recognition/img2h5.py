import os
import cv2
import h5py
import numpy as np

# Define the constant variables
FOLDER_PATH = ["Object 1", "Object 2", "Object 3", "Object 4"]
NEW_WIDTH = 750
NEW_HEIGHT = 500

# Create a new HDF5 file for storing data
with h5py.File('dataset.h5', 'w') as hdf:
    images = []
    labels = []
    
    # Loop through each folder
    for obj, path in enumerate(FOLDER_PATH, start=1):
        # Retrieve all JPEG files in the folder
        files = [file for file in os.listdir(path) if file.lower().endswith('.jpg')]
        
        print(f"\nProcessing the images of Object {obj} ...")

        # Process each image in the folder
        for i, img in enumerate(sorted(files)):
            img_path = os.path.join(path, img)
            
            # Read and then resize the image
            image = cv2.imread(img_path)
            image = cv2.resize(image, (NEW_WIDTH, NEW_HEIGHT))
            
            # Append the image and label in list
            images.append(image)
            labels.append(obj)
        
        print(f"Images of Object {obj} has been processed ...")
    
    # Convert lists into numpy arrays and store in HDF5
    hdf.create_dataset('Images', data=np.array(images), compression="gzip", compression_opts=9)
    hdf.create_dataset('Labels', data=np.array(labels), compression="gzip", compression_opts=9)

print("\nAll images and labels have been stored in the HDF5 dataset.")
