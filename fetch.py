import requests

response = requests.get("https://api.imgflip.com/get_memes")
if response.status_code == 200:
    memes = response.json()["data"]["memes"]
    for i, meme in enumerate(memes[:50]): 
        print(f"{i+1}. {meme['name']} - {meme['url']}")
else:
    print("Failed to fetch memes.")
