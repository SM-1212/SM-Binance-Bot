from flask import Flask, render_template, request
import os, json

app = Flask(__name__)

CREDENTIALS_PATH = 'creds.json'

def load_credentials():
    if os.path.exists(CREDENTIALS_PATH):
        with open(CREDENTIALS_PATH) as f:
            return json.load(f)
    return {"api_key": "", "api_secret": ""}

@app.route('/')
def home():
    creds = load_credentials()
    return render_template('index.html', creds=creds)

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=10000)
