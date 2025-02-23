import requests
import os

response = requests.get("https://api.imgflip.com/get_memes")
if response.status_code == 200:
    memes = response.json()["data"]["memes"]
else:
    print("Failed to fetch memes.")
    memes = []

os.makedirs("templates", exist_ok=True)

headers = {
    "User-Agent": "Mozilla/5.0"  
}

for meme in memes[:200]:  
    filename = f"templates/{meme['name'].replace(' ', '_')}.jpg"
    
    try:
        img_response = requests.get(meme["url"], headers=headers, stream=True)
        if img_response.status_code == 200:
            with open(filename, "wb") as file:
                for chunk in img_response.iter_content(1024):
                    file.write(chunk)
            print(f"✅ Saved: {filename}")
        else:
            print(f"❌ Failed to download: {meme['name']} (Status Code: {img_response.status_code})")

    except Exception as e:
        print(f"⚠️ Error downloading {meme['name']}: {e}")


