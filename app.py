from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

def shifty_cipher(text, shift):
    result = []
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            shifted = (ord(char) - base + shift) % 26 + base
            result.append(chr(shifted))
        else:
            result.append(char)
    return ''.join(result)

@app.route('/encrypt', methods=['POST'])
def encrypt():
    try:
        data = request.get_json()
        text = data.get('text', '')
        shift = int(data.get('shift', 0))
        cipher = shifty_cipher(text, shift)
        return jsonify({'cipher': cipher})
    except Exception as e:
        return jsonify({'error': str(e)}), 500
