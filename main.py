from flask import Flask, render_template, request, jsonify
import os

app = Flask(__name__)

# 🔐 Load API Keys (from environment or .env)
BINANCE_API_KEY = os.getenv("BINANCE_API_KEY")
BINANCE_SECRET_KEY = os.getenv("BINANCE_SECRET_KEY")

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/get_sl_tsl', methods=['POST'])
def get_sl_tsl():
    data = request.json
    symbol = data.get("symbol", "")
    sl, tsl = get_sl_tsl_points(symbol)
    return jsonify({"sl": sl, "tsl": tsl})

# 📊 Professional SL/TSL on 15-min Timeframe
def get_sl_tsl_points(symbol):
    symbol = symbol.upper()
    if symbol == "BTCUSDT":
        return 400, 300
    elif symbol == "ETHUSDT":
        return 50, 35
    elif symbol == "BNBUSDT":
        return 10, 7
    elif symbol == "SOLUSDT":
        return 4, 3
    return 0, 0

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=10000)
