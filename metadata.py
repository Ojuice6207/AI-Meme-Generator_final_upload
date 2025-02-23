import os
import json


template_path = "templates"


default_positions = {
    "top_text_position": [30, 20],
    "bottom_text_position": [30, 400]  # Adjust based on meme format
}


meme_list = []
for file in os.listdir(template_path):
    if file.endswith(".jpg") or file.endswith(".png"):
        meme_list.append({
            "name": file.replace("_", " ").split(".")[0],  # Remove underscore & extension
            "file": file,
            "top_text_position": default_positions["top_text_position"],
            "bottom_text_position": default_positions["bottom_text_position"]
        })


with open("memes.json", "w") as f:
    json.dump(meme_list, f, indent=4)

print("✅ memes.json created successfully!")
