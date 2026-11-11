from datetime import datetime, timezone
from pathlib import Path
from typing import Optional

from fastapi import FastAPI, Query
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles

ROOT = Path(__file__).resolve().parent.parent
FRONTEND = ROOT / "frontend"

app = FastAPI(title="EVIL EYE TERMINAL", version="0.2.0", description="Educational market intelligence demo.")
app.mount("/assets", StaticFiles(directory=FRONTEND), name="assets")

# All prices and market statistics below are illustrative demo values, not live quotes.
ASSETS = [
    {"symbol": "NIFTY", "name": "NIFTY 50", "price": 24196.35, "change": 0.72, "type": "Index", "exchange": "NSE"},
    {"symbol": "SENSEX", "name": "S&P BSE SENSEX", "price": 79624.10, "change": 0.64, "type": "Index", "exchange": "BSE"},
    {"symbol": "BANKNIFTY", "name": "NIFTY BANK", "price": 51842.70, "change": -0.31, "type": "Index", "exchange": "NSE"},
    {"symbol": "RELIANCE", "name": "Reliance Industries", "price": 1428.50, "change": 1.18, "type": "Equity", "exchange": "NSE"},
    {"symbol": "TCS", "name": "Tata Consultancy Services", "price": 3892.20, "change": -0.46, "type": "Equity", "exchange": "NSE"},
    {"symbol": "HDFCBANK", "name": "HDFC Bank", "price": 1682.75, "change": 0.28, "type": "Equity", "exchange": "NSE"},
    {"symbol": "INFY", "name": "Infosys", "price": 1544.60, "change": 1.92, "type": "Equity", "exchange": "NSE"},
    {"symbol": "ICICIBANK", "name": "ICICI Bank", "price": 1261.30, "change": 0.51, "type": "Equity", "exchange": "NSE"},
    {"symbol": "ITC", "name": "ITC", "price": 438.90, "change": -0.18, "type": "Equity", "exchange": "NSE"},
    {"symbol": "BHARTIARTL", "name": "Bharti Airtel", "price": 1748.25, "change": 1.06, "type": "Equity", "exchange": "NSE"},
]

NEWS = [
    {"time": "09:42", "tag": "MARKETS", "title": "Indian equities open mixed as investors assess global cues", "source": "EVIL EYE DEMO DESK"},
    {"time": "09:18", "tag": "TECHNOLOGY", "title": "Technology shares in focus ahead of quarterly results", "source": "EVIL EYE DEMO DESK"},
    {"time": "08:55", "tag": "ECONOMY", "title": "Policy watchers track inflation and growth indicators", "source": "EVIL EYE DEMO DESK"},
    {"time": "08:30", "tag": "BANKING", "title": "Banking sector remains on the market watchlist", "source": "EVIL EYE DEMO DESK"},
]

EVENTS = [
    {"date": "12 NOV", "time": "10:00", "region": "IN", "event": "Industrial production (illustrative)", "impact": "MEDIUM"},
    {"date": "13 NOV", "time": "14:30", "region": "US", "event": "Inflation data watch (illustrative)", "impact": "HIGH"},
    {"date": "14 NOV", "time": "09:00", "region": "IN", "event": "Company results watch (illustrative)", "impact": "LOW"},
]

@app.get("/")
def home():
    return FileResponse(FRONTEND / "index.html")

@app.get("/api/health")
def health():
    return {"status": "ok", "app": "EVIL EYE TERMINAL", "version": app.version, "timestamp": datetime.now(timezone.utc).isoformat()}

@app.get("/api/market/overview")
def overview():
    return {
        "as_of": datetime.now(timezone.utc).isoformat(),
        "indices": ASSETS[:3],
        "market_status": "DEMO SESSION",
        "breadth": {"advances": 1248, "declines": 986, "unchanged": 142},
        "notice": "Illustrative demo data. Not live market quotes."
    }

@app.get("/api/market/assets")
def assets(q: Optional[str] = Query(default=None), kind: Optional[str] = Query(default=None)):
    rows = ASSETS
    if q:
        term = q.lower()
        rows = [a for a in rows if term in a["symbol"].lower() or term in a["name"].lower()]
    if kind and kind != "All":
        rows = [a for a in rows if a["type"] == kind]
    return {"items": rows, "count": len(rows)}

@app.get("/api/market/chart")
def chart(symbol: str = "NIFTY", period: str = "1D"):
    asset = next((a for a in ASSETS if a["symbol"] == symbol.upper()), ASSETS[0])
    count = {"1D": 32, "1W": 35, "1M": 30, "3M": 36, "1Y": 40}.get(period, 32)
    seed = sum(ord(c) for c in asset["symbol"])
    points = []
    base = asset["price"] * 0.985
    for i in range(count):
        wave = ((i * 17 + seed * 3) % 23 - 11) / 1000
        drift = (i / max(count - 1, 1)) * (asset["change"] / 100)
        value = round(base * (1 + wave + drift), 2)
        points.append({"label": f"{i + 1:02d}", "value": value})
    return {"symbol": asset["symbol"], "period": period, "points": points, "notice": "Illustrative chart series."}

@app.get("/api/news")
def news():
    return {"items": NEWS, "notice": "Sample headlines for interface demonstration."}

@app.get("/api/calendar")
def calendar():
    return {"items": EVENTS, "notice": "Illustrative events, not an official economic calendar."}
