import os
import cv2
import random
import shutil
import numpy as np
import matplotlib.pyplot as plt
from ultralytics import YOLO
from zipfile import ZipFile, is_zipfile
import requests

# Dynamic zip file detection
zip_path = None
for fname in os.listdir('/content/'): # Corrected: list contents of /content/ directory
    if 'handwritten_dataset' in fname and fname.endswith('.zip'):
        zip_path = os.path.join('/content/', fname) # Corrected: construct path correctly
        break

# If no zip is found, provide a fallback or clear instructions
if not zip_path:
    print("No zip file found. Downloading a sample dataset for demonstration...")
    # Example placeholder: replace with actual URL if available or instructions
    # !wget -O /content/handwritten_dataset.zip https://example.com/handwritten_dataset.zip
    # zip_path = "/content/handwritten_dataset.zip"
    print("CRITICAL: Please upload 'handwritten_dataset.zip' to the /content/ folder and run this cell again.")
else:
    print(f"Detected zip file: {zip_path}")

extract_path = "/content/dataset_extracted" # Corrected: set a proper extraction directory

if zip_path and os.path.exists(zip_path):
    if is_zipfile(zip_path):
        if os.path.exists(extract_path):
            print(f"Removing existing extraction directory: {extract_path}")
            shutil.rmtree(extract_path)
        os.makedirs(extract_path, exist_ok=True) # Ensure the directory exists before unzipping

        # Use shell command 'unzip' for potentially more robust extraction
        # The -o flag overwrites existing files without prompting
        # The -d flag specifies the destination directory
        print(f"Extracting {zip_path} to {extract_path} using unzip command...")
        !unzip -o "{zip_path}" -d "{extract_path}" # Fixed: Added quotes to paths

        print(f"Successfully extracted to {extract_path}")
    else:
        print(f"Error: {zip_path} is corrupted or not a valid zip file. Try re-uploading the file.")
elif not zip_path:
    print("Zip file not found, skipping extraction.")

import os
import random
import shutil

# Updated paths based on the new extraction folder
base_path = "/content/dataset_extracted"
output_path = "/content/yolo_dataset"

all_image_paths_with_classes = []
all_unique_letter_classes = set()

# 1. Collect all image paths
if os.path.exists(base_path):
    for root, _, files in os.walk(base_path):
        for file in files:
            if file.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp', '.tiff')):
                image_full_path = os.path.join(root, file)
                # The class name is the immediate parent directory
                letter_class_name = os.path.basename(root)
                all_image_paths_with_classes.append((image_full_path, letter_class_name))
                all_unique_letter_classes.add(letter_class_name)

classes = sorted(list(all_unique_letter_classes))
class_name_to_id = {name: i for i, name in enumerate(classes)}

# Clean start for output
if os.path.exists(output_path):
    shutil.rmtree(output_path)

for split in ['train', 'val']:
    for folder in ['images', 'labels']:
        os.makedirs(os.path.join(output_path, folder, split), exist_ok=True)

split_ratio = 0.8
images_grouped_by_class = {class_name: [] for class_name in classes}
for path, label in all_image_paths_with_classes:
    images_grouped_by_class[label].append(path)

# 3. Process splits
for letter_class_name in classes:
    image_paths = images_grouped_by_class[letter_class_name]
    random.shuffle(image_paths)
    split_idx = int(len(image_paths) * split_ratio)

    train_images = image_paths[:split_idx]
    val_images = image_paths[split_idx:]
    class_id = class_name_to_id[letter_class_name]

    for dataset_type, imgs in [("train", train_images), ("val", val_images)]:
        for src in imgs:
            img_name = f"{letter_class_name}_{os.path.basename(src)}"
            dst_img = os.path.join(output_path, "images", dataset_type, img_name)
            shutil.copy(src, dst_img)

            label_name = os.path.splitext(img_name)[0] + ".txt"
            label_path = os.path.join(output_path, "labels", dataset_type, label_name)
            with open(label_path, "w") as f:
                # YOLO format: class_id x_center y_center width height (normalized)
                f.write(f"{class_id} 0.5 0.5 1.0 1.0\n")

print(f"YOLO Dataset Created at {output_path} with {len(classes)} classes.")

yaml_content = f"""
path: /content/yolo_dataset
train: images/train
val: images/val
names:
"""
for i, c in enumerate(classes):
    yaml_content += f"  {i}: {c}\n"
with open("/content/handwriting.yaml", "w") as f:
    f.write(yaml_content)
print(yaml_content)

model = YOLO("yolov8n.pt")
model.train(
    data="/content/handwriting.yaml",
    epochs=10,
    imgsz=64,
    batch=32
)

metrics = model.val()
print(metrics)

import random

# Uncomment the following lines if you want to upload a new image for prediction
# from google.colab import files
# uploaded = files.upload()
# uploaded_image = list(uploaded.keys())[0]

# For demonstration, pick a random image from the extracted dataset
# Ensure all_image_paths_with_classes is available from previous cells
if 'all_image_paths_with_classes' in locals() and all_image_paths_with_classes:
    random_image_info = random.choice(all_image_paths_with_classes)
    uploaded_image = random_image_info[0] # Get the path of the random image
    print(f"Using random image for prediction: {uploaded_image}")
else:
    # Fallback if all_image_paths_with_classes is not found or empty
    print("Error: No image paths found from previous steps. Please ensure the dataset is extracted correctly.")
    print("You may need to manually specify an image path or re-run previous cells.")
    # As a last resort, try a known image path if one exists after extraction
    uploaded_image = "/content/dataset_extracted/handwritten-english-characters-and-digits/combined_folder/train/A_caps/A_caps.001.png" # Example fallback
    if not os.path.exists(uploaded_image):
        raise FileNotFoundError(f"Fallback image {uploaded_image} not found. Please upload an image or check dataset extraction.")

results = model.predict(
    source=uploaded_image,
    conf=0.25,
    save=True
)
print("Prediction Complete")

import cv2
import matplotlib.pyplot as plt
# Get the image with detections plotted on it directly from the results object
plotted_img_bgr = results[0].plot()
# Convert BGR to RGB for matplotlib display
img_rgb = cv2.cvtColor(plotted_img_bgr, cv2.COLOR_BGR2RGB)
plt.figure(figsize=(8,8))
plt.imshow(img_rgb)
plt.axis("off")
plt.show()

boxes = results[0].boxes
# Ensure there is at least one detected box before trying to access its properties
if len(boxes) > 0:
    # Take the first detected box for displaying predicted letter and confidence
    box = boxes[0]
    cls_id = int(box.cls[0])
    conf = float(box.conf[0])

    # Make sure 'classes' variable is defined from previous steps
    if 'classes' in locals() and cls_id < len(classes):
        print(f"Predicted Letter: {classes[cls_id]}")
        print(f"Confidence: {conf:.2f}")
    else:
        print(f"Could not map class ID {cls_id} to a class name. Check 'classes' variable.")
else:
    print("No objects detected in the image.")
