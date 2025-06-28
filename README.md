# 🎨 Theme-Based Fashion Scoring API — Style Studio: Game Zone

This project is a lightweight Flask API that uses **OpenAI’s CLIP model** to evaluate how well an uploaded fashion design image matches a given **thematic prompt** (e.g., "futuristic streetwear", "cottagecore floral").  

Used as part of **Style Studio’s Game Zone**, this model powers theme-based design challenges and automatically scores user submissions.

---
Style Studio APP Repo-https://github.com/Ananyasolanki123/StyleStudio

## 🚀 Features

- ✅ Accepts any uploaded fashion image
- ✅ Accepts a theme prompt (text)
- ✅ Uses `openai/clip-vit-base-patch32` to score semantic alignment
- ✅ Returns a score out of 100 indicating how well the image fits the theme
- ✅ Can be used to power leaderboards, contests, or real-time feedback

---

## 🧠 How It Works

1. The user is presented with a theme.
2. They upload a fashion design to match the theme.
3. The system computes cosine similarity between the image and the theme prompt using CLIP.
4. A score (0–100) is returned based on similarity.

---

## 🛠️ API Endpoints

### `GET /`

Returns a basic upload form (if `form.html` exists in the `templates/` directory).

### `POST /score-theme`

**Form Fields:**
- `theme`: a text prompt (e.g., "vintage streetwear with denim")
- `file`: an uploaded `.jpg` or `.png` image

**Response:**

json
{
  "theme": "futuristic streetwear",
  "score": 82.47,
  "message": "Image matches 'futuristic streetwear' with score 82.47/100"
}

📦 Project Structure
CLIP THEME MATCH-STYLE STUDIO/
├── main.py                 # Flask app
├── templates/form.html      # (optional) upload UI

Install dependencies

pip install flask torch transformers Pillow
Run the app
python model.py
Open http://localhost:5000 in your browser.

🏆 Game Zone Integration
This model is part of the  Design Analysis feature of Style Studio Game Zone, where:

Users are shown a generated theme

They upload their fashion design matching that theme

The model scores their submission

Scores are shown on a leaderboard or used for winner selection

📬 Contact
Built by Ananya solanki for Style Studio.
