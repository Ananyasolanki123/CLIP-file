from flask import Flask, request, jsonify, render_template
from transformers import CLIPProcessor, CLIPModel
from PIL import Image
import torch
import io

app = Flask(__name__)

# Load CLIP model
model = CLIPModel.from_pretrained("openai/clip-vit-base-patch32")
processor = CLIPProcessor.from_pretrained("openai/clip-vit-base-patch32")

# Route to render the HTML form
@app.route('/', methods=['GET'])
def form():
    return render_template('form.html')

# API route to process form input
@app.route('/score-theme', methods=['POST'])
def score_theme():
    try:
        theme = request.form.get('theme')
        file = request.files.get('file')

        if not theme or not file:
            return jsonify({"error": "Missing theme or file"}), 400

        image = Image.open(io.BytesIO(file.read())).convert("RGB")
        inputs = processor(text=[theme], images=image, return_tensors="pt", padding=True)
        outputs = model(**inputs)

        image_emb = outputs.image_embeds
        text_emb = outputs.text_embeds
        similarity = torch.cosine_similarity(image_emb, text_emb).item()
        score = round(similarity * 100, 2)

        return jsonify({
            "theme": theme,
            "score": score,
            "message": f"Image matches '{theme}' with score {score}/100"
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
