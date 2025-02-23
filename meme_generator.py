from fastapi import FastAPI
from pydantic import BaseModel
from PIL import Image, ImageDraw, ImageFont
import os
import json
import subprocess
from gemini_integration import generate_meme_captions

app = FastAPI()

try:
    with open("memes.json", "r") as f:
        meme_templates = json.load(f)
    if not meme_templates:
        raise ValueError("Meme templates file is empty.")
except Exception as e:
    raise ValueError(f"Error loading meme templates: {e}")

class MemeRequest(BaseModel):
    prompt: str

def find_best_template(template_name):
    if not template_name:
        return None
    template_name = template_name.lower().strip()
    for meme in meme_templates:
        if meme["name"].lower() == template_name:
            return meme
    return None

def wrap_text(draw, text, font, max_width):
    if not text:
        return []
    words = text.split()
    lines = []
    current_line = ""
    for word in words:
        test_line = f"{current_line} {word}".strip()
        width = font.getbbox(test_line)[2]
        if width <= max_width:
            current_line = test_line
        else:
            lines.append(current_line)
            current_line = word
    if current_line:
        lines.append(current_line)
    return lines

def create_meme(template_name, top_text, bottom_text, output_path="generated_meme.jpg"):
    meme_data = find_best_template(template_name)
    if not meme_data:
        return {"error": f"Template '{template_name}' not found in the meme database."}
    
    template_path = os.path.join("templates", meme_data["file"])
    if not os.path.exists(template_path):
        return {"error": f"Template file '{template_path}' not found!"}

    img = Image.open(template_path)
    draw = ImageDraw.Draw(img)
    font_path = "arial.ttf"
    try:
        font = ImageFont.truetype(font_path, 40)
    except IOError:
        print("⚠️ Arial.ttf not found. Using default font.")
        font = ImageFont.load_default()
    
    top_position = tuple(meme_data["top_text_position"])
    bottom_position = tuple(meme_data["bottom_text_position"])
    max_width = img.width - 40  

    top_lines = wrap_text(draw, top_text, font, max_width)
    bottom_lines = wrap_text(draw, bottom_text, font, max_width)
    
    y_offset = top_position[1]
    for line in top_lines:
        draw.text((top_position[0], y_offset), line, font=font, fill="white")
        y_offset += font.getbbox(line)[3]
    
    y_offset = bottom_position[1]
    for line in bottom_lines:
        draw.text((bottom_position[0], y_offset), line, font=font, fill="white")
        y_offset += font.getbbox(line)[3]
    
    img.save(output_path)
    return output_path

@app.post("/generate-meme/")
async def generate_meme(request: MemeRequest):
    try:
        # Generate captions using Gemini AI
        top_text, bottom_text, template_name = generate_meme_captions(request.prompt)

        # Debugging: Print raw response
        print(f"🛠️ Gemini Raw Response: {top_text}, {bottom_text}, {template_name}")

        # Ensure values are valid strings
        top_text = str(top_text).strip() if top_text else "Top Text"
        bottom_text = str(bottom_text).strip() if bottom_text else ""  
        template_name = str(template_name).strip() if template_name else None

        if not template_name:
            return {"error": "Failed to determine meme template. Try again later."}

        output_path = create_meme(template_name, top_text, bottom_text)
        
        if isinstance(output_path, dict) and "error" in output_path:
            return {"error": output_path["error"]}

        return {
            "message": "Meme created successfully!",
            "template_used": template_name,
            "output_file": output_path
        }
    except Exception as e:
        print(f"🚨 API Error: {e}")
        return {"error": "An unexpected error occurred. Please try again later."}

if __name__ == "__main__":
    subprocess.Popen([
        "uvicorn", "meme_generator:app", "--host", "127.0.0.1", "--port", "8000", "--reload"
    ])
