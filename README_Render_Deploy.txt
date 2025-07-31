SM TRADING BOT - BINANCE FUTURES (RENDER.COM DEPLOYMENT)

1. Go to https://dashboard.render.com/
2. Click "New Web Service" > Connect your GitHub OR "Deploy a Web Service Manually"
3. Upload this folder (or paste into a repo)
4. Set Environment variables from `.env.example`:
   - BINANCE_API_KEY
   - BINANCE_API_SECRET
   - WEBHOOK_SECRET_KEY

5. In "Start Command", put:
   python main.py

6. After deploy, your endpoint will be:
   https://your-app-name.onrender.com/webhook

7. Use this URL in TradingView alerts (Webhook section)

TRADINGVIEW ALERT FORMAT (JSON):
{
  "symbol": "BTCUSDT",
  "side": "BUY",
  "strategy": "Scalping"
}

You’re done! Bot will auto-trade Futures with SL/TSL logic.