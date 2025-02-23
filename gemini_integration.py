import google.generativeai as genai
import os
import json
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")
if not api_key:
    raise ValueError("GOOGLE_API_KEY is missing. Please check your .env file.")

genai.configure(api_key=api_key)
model = genai.GenerativeModel("gemini-pro")

try:
    with open("memes.json", "r") as f:
        meme_templates = json.load(f)
    if not meme_templates:
        raise ValueError("Meme templates file is empty.")
except Exception as e:
    raise ValueError(f"Error loading meme templates: {e}")

def extract_json(response_text):
    """Safely extracts JSON from the Gemini response."""
    if not response_text:
        print("⚠️ Empty response from Gemini. Using fallback values.")
        return None

    try:
        json_start = response_text.find('{')
        json_end = response_text.rfind('}')
        if json_start != -1 and json_end != -1:
            json_str = response_text[json_start:json_end + 1]
            return json.loads(json_str)
    except json.JSONDecodeError as e:
        print(f"⚠️ JSON Parsing Failed: {e}. Using fallback values.")
    return None

def generate_meme_captions(prompt):
    """Generates meme captions & selects a meme template, enforcing structured JSON output."""
    try:
        meme_list = ", ".join([f'"{m["name"]}"' for m in meme_templates])
        
        full_prompt = (
            f"Generate a funny meme caption for: '{prompt}'.\n"
            f"Choose ONLY from this meme list: {meme_list}.\n"
            f"Strictly return JSON in this format (no extra text):\n"
            f'{{"top_text": "Your Top Text", "bottom_text": "Your Bottom Text", "template_name": "Template Name"}}'
        )

        response = model.generate_content(full_prompt)

        print(f"🛠️ Gemini Raw Response: {response.text}")

        parsed_response = extract_json(response.text) or {
            "top_text": "Funny Meme",
            "bottom_text": "Generated Text",
            "template_name": meme_templates[0]["name"]
        }

        top_text = parsed_response.get("top_text")
        bottom_text = parsed_response.get("bottom_text")
        template_name = parsed_response.get("template_name")

        # Ensure values are strings and not None before stripping
        top_text = str(top_text).strip() if top_text else "Top Text"
        bottom_text = str(bottom_text).strip() if bottom_text else ""
        template_name = str(template_name).strip().lower() if template_name else None

        if not template_name or template_name == "template name":
            return None, None, None

        matching_template = next((m["name"] for m in meme_templates if m["name"].lower() == template_name), None)

        if not matching_template:
            print(f"⚠️ Template '{template_name}' not found in memes.json. Using fallback.")
            matching_template = meme_templates[0]["name"]

        return top_text, bottom_text, matching_template

    except Exception as e:
        print(f"❌ Error generating captions: {e}")
        return None, None, None
