from flask import Flask, jsonify, request
import json
import os

app = Flask(__name__)

FILE = 'input.json'

def getMarkdown():
    if os.path.exists(FILE):
        with open(FILE, 'r') as f:
            data = json.load(f)

        return data.get("gptOutput", "")
    return ""

def updateMarkdown(newMarkdown):
    with open(FILE, 'w') as f:
        json.dump({"gptOutput": newMarkdown}, f)

@app.route('/get', methods=['GET'])
def get_markdown():
    markdown = getMarkdown()
    return jsonify({"markdown": markdown})

@app.route('/post', methods=['POST'])
def post_markdown():
    try:
        data = request.json
        text = data.get("text", "").strip()
        if not text:
            return jsonify({"Error": "No text provided"}), 400
        
        markdown = getMarkdown()
        new_markdown = f"{markdown}\n{text}"
        updateMarkdown(new_markdown)
        return jsonify({"Success": "Markdown successfully updated"})
    except Exception as e:
        return jsonify({"Error": str(e)}), 400

if __name__ == "__main__":
    app.run(debug=True)