# AI-Meme-Generator
# AI Meme Generator 🤖🎭

## 📌 Overview
AI Meme Generator is a FastAPI-based meme creation tool that uses Google Gemini AI to generate memes and GIFs based on user prompts.

## 🚀 Features
- AI-generated memes using predefined templates.
- Supports text overlays and customization.
- Generates memes and GIFs dynamically.
- API-based interaction using FastAPI.

## 🛠️ Tech Stack
- **Backend**: FastAPI
- **AI Model**: Google Gemini API
- **Image Processing**: Pillow (PIL)
- **Deployment**: GitHub, FastAPI server

## 📎 Project Structure
```
📎 AI-Meme-Generator
 ┣ 🗂 templates/        # Meme template images
 ┣ 🗂 static/           # Generated memes
 ┣ 📝 main.py           # FastAPI backend
 ┣ 📝 requirements.txt  # Dependencies
 ┣ 📝 README.md         # Project documentation
 └ 📝 config.py         # API key configuration
```

## 🔧 Installation & Setup
1️⃣ Clone the repository:  
   ```sh
   git clone https://github.com/YOUR-USERNAME/AI-Meme-Generator.git
   ```
2️⃣ Navigate to the project folder:  
   ```sh
   cd AI-Meme-Generator
   ```
3️⃣ Install dependencies:  
   ```sh
   pip install -r requirements.txt
   ```
4️⃣ Set up API keys in `config.py`.  
5️⃣ Run the FastAPI server:  
   ```sh
   uvicorn main:app --reload
   ```
6️⃣ Open **http://127.0.0.1:8000/docs** in your browser to test the API.

## 📌 Usage
- On opening **http://127.0.0.1:8000/docs**, click on post
- Click on try it now
- Enter the prompt in the given place and click on execute
  OR
- Send a `POST` request to `/generate-meme` with a text prompt.
- The API will return a generated meme.
- Download and share your AI-created meme!

## 🎥 Demo Video
📌 **[Watch the Demo Here](https://drive.google.com/file/d/1sA4SdqxqYj2ODpf_bDz0AVxJNeFa0uds/view?usp=sharing)**

## PPT
📌 **[PPT link](https://docs.google.com/presentation/d/1LACM4VhoFrcCkla9R5S376oLIyV2c8KzTkMN1MNgCRE/edit?usp=sharing)**

## 🤝 Contributing
Feel free to submit pull requests! Open an issue if you find bugs.

## 💜 License
MIT License.

---

### **🔹 Next Steps**
- Add more customization options.
- Improve AI meme generation quality.
- Deploy it to a public API service.

