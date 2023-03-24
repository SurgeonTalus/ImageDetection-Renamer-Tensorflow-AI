import os
import tkinter as tk
from tkinter import filedialog
import tensorflow as tf

# Open GUI to select folder
root = tk.Tk()
root.withdraw()
folder_path = filedialog.askdirectory()

# Get the list of files in the directory
files = os.listdir(folder_path)

# Counter for version number
version_counter = {}

# Use TensorFlow to identify objects in all image files in the directory
for file in files:
    if file.endswith('.jpeg') or file.endswith('.jpg') or file.endswith('.JPG') or file.endswith('.JPEG') or file.endswith('.PNG') or file.endswith('.png'):
        try:
            # Load image file
            image_file = os.path.join(folder_path, file)
            img = tf.keras.preprocessing.image.load_img(image_file, target_size=(224, 224))
            img_array = tf.keras.preprocessing.image.img_to_array(img)
            img_array = tf.keras.applications.mobilenet_v2.preprocess_input(img_array)
        
            # Use model to predict object in image
            model = tf.keras.applications.MobileNetV2()
            predictions = model.predict(tf.expand_dims(img_array, axis=0))
            predicted_class = tf.keras.applications.mobilenet_v2.decode_predictions(predictions)[0][0][1]
        
            # Rename the file with the predicted object name and a version number if necessary
            new_name = predicted_class + os.path.splitext(file)[1]
            version = version_counter.get(new_name, 0)
            if version > 0:
                new_name = predicted_class + f"_{version}{os.path.splitext(file)[1]}"
            while os.path.exists(os.path.join(folder_path, new_name)):
                version += 1
                new_name = predicted_class + f"_{version}{os.path.splitext(file)[1]}"
            version_counter[new_name] = version
            os.rename(image_file, os.path.join(folder_path, new_name))
            print(f"Renamed {image_file} to {new_name}.")
        except Exception as e:
            print(f"Error processing {file}: {e}")
