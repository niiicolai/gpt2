from flask import Flask, request, jsonify
from flask_cors import CORS
from transformers import GPT2LMHeadModel, GPT2Tokenizer

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "http://127.0.0.1:5500"}})

model = GPT2LMHeadModel.from_pretrained("fine_tuned_gpt2")
tokenizer = GPT2Tokenizer.from_pretrained("fine_tuned_gpt2")

@app.route("/generate", methods=["POST"])
def generate_text():
    input_text = request.json["input_text"]
    input_ids = tokenizer.encode(input_text, return_tensors="pt")

    output = model.generate(
        input_ids, 
        max_length=500, 
        num_return_sequences=1, 
        no_repeat_ngram_size=2,
        temperature=0.7
    )
    generated_text = tokenizer.decode(output[0], skip_special_tokens=True)

    return jsonify({"generated_text": generated_text})

if __name__ == "__main__":
    app.run()
