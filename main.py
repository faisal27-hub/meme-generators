import os
from PIL import Image

# --- Ensure 'output' folder exists ---
output_folder = "output"
os.makedirs(output_folder, exist_ok=True)

# --- Image filenames tere folder ke hisaab se ---
image_files = ["1.jpg.jpg", "2.jpg.jpg", "3.jpg.jpg", "4.jpg.jpg","5.jpg.jpg","6.jpg.jpg","7.jpg.jpg"]

for file in image_files:
    img = Image.open(file)

    # --- New filename with prefix inside 'output' folder ---
    new_name = os.path.join(output_folder, "meme_" + file)

    # --- Save image as it is ---
    img.save(new_name)
    print(f"Saved: {new_name}")