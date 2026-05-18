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
