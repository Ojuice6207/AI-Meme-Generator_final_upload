from PIL import Image
import os

input_folder = "templates"
output_folder = "templates_resized"

os.makedirs(output_folder, exist_ok=True)

for file in os.listdir(input_folder):
    if file.endswith(".jpg") or file.endswith(".png"):
        img = Image.open(os.path.join(input_folder, file))

       
        if img.mode in ("P", "RGBA"):
            img = img.convert("RGB")

        img = img.resize((500, 500)) 
        img.save(os.path.join(output_folder, file), "JPEG")  

        print(f"✅ Resized & saved: {file}")

print("🎯 All templates resized successfully!")

