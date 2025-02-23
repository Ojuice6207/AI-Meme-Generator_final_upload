import os
import json

# Define folder where templates are stored
template_path = "templates_resized"

# Define default text positions (modifiable later)
default_positions = {
    "top_text_position": [30, 50],  # Adjust for better placement
    "bottom_text_position": [30, 450]
}

# Generate metadata
meme_list = []
for file in os.listdir(template_path):
    if file.endswith(".jpg") or file.endswith(".png"):
        meme_list.append({
            "name": file.replace("_", " ").split(".")[0],  # Convert underscores to spaces
            "file": file,
            "top_text_position": default_positions["top_text_position"],
            "bottom_text_position": default_positions["bottom_text_position"]
        })

# Save to memes.json
with open("memes.json", "w") as f:
    json.dump(meme_list, f, indent=4)

print("✅ memes.json updated successfully!")
