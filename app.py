import os
from flask import request
from flask import jsonify
from flask import Flask
app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def hello():
    if request.method == 'POST':
        name = request.json.get('name')
        return jsonify(message=f"Hello, {name}!")
    else:
        return jsonify(message="Hello from Python!")

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
