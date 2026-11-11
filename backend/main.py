from datetime import datetime, timezone
from pathlib import Path
from typing import Optional

from fastapi import FastAPI, Query
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles

ROOT = Path(__file__).resolve().parent.parent
FRONTEND = ROOT / "frontend"

app = FastAPI(
    title="EVIL EYE TERMINAL",
    version="0.3.0",
    description="Cross-market educational research workspace. Demo data unless a licensed provider is configured.",
)
app.mount("/assets", StaticFiles(directory=FRONTEND), name="assets")

# Static illustrative values only. They are deliberately not presented as live quotes.
ASSETS = [
    {"symbol":"NIFTY","name":"NIFTY 50","price":24196.35,"change":0.72,"type":"Index","exchange":"NSE","region":"India","currency":"INR"},
    {"symbol":"SENSEX","name":"S&P BSE SENSEX","price":79624.10,"change":0.64,"type":"Index","exchange":"BSE","region":"India","currency":"INR"},
    {"symbol":"BANKNIFTY","name":"NIFTY BANK","price":51842.70,"change":-0.31,"type":"Index","exchange":"NSE","region":"India","currency":"INR"},
    {"symbol":"RELIANCE","name":"Reliance Industries","price":1428.50,"change":1.18,"type":"Equity","exchange":"NSE","region":"India","currency":"INR"},
    {"symbol":"TCS","name":"Tata Consultancy Services","price":3892.20,"change":-0.46,"type":"Equity","exchange":"NSE","region":"India","currency":"INR"},
    {"symbol":"HDFCBANK","name":"HDFC Bank","price":1682.75,"change":0.28,"type":"Equity","exchange":"NSE","region":"India","currency":"INR"},
    {"symbol":"INFY","name":"Infosys","price":1544.60,"change":1.92,"type":"Equity","exchange":"NSE","region":"India","currency":"INR"},
    {"symbol":"ICICIBANK","name":"ICICI Bank","price":1261.30,"change":0.51,"type":"Equity","exchange":"NSE","region":"India","currency":"INR"},
    {"symbol":"ITC","name":"ITC","price":438.90,"change":-0.18,"type":"Equity","exchange":"NSE","region":"India","currency":"INR"},
    {"symbol":"BHARTIARTL","name":"Bharti Airtel","price":1748.25,"change":1.06,"type":"Equity","exchange":"NSE","region":"India","currency":"INR"},
    {"symbol":"SPX","name":"S&P 500","price":5842.47,"change":0.43,"type":"Index","exchange":"NYSE","region":"Americas","currency":"USD"},
    {"symbol":"DJI","name":"Dow Jones Industrial Average","price":43958.19,"change":0.21,"type":"Index","exchange":"NYSE","region":"Americas","currency":"USD"},
    {"symbol":"IXIC","name":"NASDAQ Composite","price":18680.12,"change":0.88,"type":"Index","exchange":"NASDAQ","region":"Americas","currency":"USD"},
    {"symbol":"RUT","name":"Russell 2000","price":2218.34,"change":-0.24,"type":"Index","exchange":"NYSE","region":"Americas","currency":"USD"},
    {"symbol":"FTSE","name":"FTSE 100","price":8291.იღ,"change":0.16,"type":"Index","exchange":"LSE","region":"Europe","currency":"GBP"},
    {"symbol":"DAX","name":"DAX","price":19324.80,"change":0.37,"type":"Index","exchange":"XETRA","region":"Europe","currency":"EUR"},
    {"symbol":"CAC","name":"CAC 40","price":7421.55,"change":-0.12,"type":"Index","exchange":"Euronext","region":"Europe","currency":"EUR"},
    {"symbol":"N225","name":"Nikkei 225","price":39376.09,"change":0.55,"type":"Index","exchange":"TSE","region":"Asia Pacific","currency":"JPY"},
    {"symbol":"HSI","name":"Hang Seng Index","price":20311.ರಿ,"change":-0.62,"type":"Index","exchange":"HKEX","region":"Asia Pacific","currency":"HKD"},
    {"symbol":"ASX200","name":"S&P/ASX 200","price":8324.70,"change":0.19,"type":"Index","exchange":"ASX","region":"Asia Pacific","currency":"AUD"},
    {"symbol":"GOLD","name":"Gold spot reference","price":2684.20,"change":0.34,"type":"Commodity","exchange":"REFERENCE","region":"Global","currency":"USD"},
    {"symbol":"BRENT","name":"Brent crude reference","price":74.82,"change":-0.41,"type":"Commodity","exchange":"REFERENCE","region":"Global","currency":"USD"},
    {"symbol":"EURUSD","name":"Euro / US dollar","price":1.0834,"change":0.08,"type":"FX","exchange":"FX REFERENCE","region":"Global","currency":"USD"},
    {"symbol":"USDINR","name":"US dollar / Indian rupee","price":84.36,"change":-0.05,"type":"FX","exchange":"FX REFERENCE","region":"Global","currency":"INR"},
]

NEWS = [
    {"time":"09:42","tag":"INDIA","title":"Indian equities open mixed as investors assess global cues","source":"EE SAMPLE DESK"},
    {"time":"09:18","tag":"US","title":"US index futures and technology shares remain in focus","source":"EE SAMPLE DESK"},
    {"time":"08:55","tag":"EUROPE","title":"European markets monitor growth and policy signals","source":"EE SAMPLE DESK"},
    {"time":"08:30","tag":"ASIA","title":"Asia-Pacific benchmarks show a mixed regional picture","source":"EE SAMPLE DESK"},
    {"time":"08:05","tag":"MACRO","title":"Currency and commodity reference levels updated in demo dataset","source":"EE SAMPLE DESK"},
]
EVENTS = [
    {"date":"12 NOV","time":"10:00","region":"IN","event":"Industrial production watch (illustrative)","impact":"MEDIUM"},
    {"date":"13 NOV","time":"14:30","region":"US","event":"Inflation data watch (illustrative)","impact":"HIGH"},
    {"date":"14 NOV","time":"09:00","region":"EU","event":"Economic indicators watch (illustrative)","impact":"LOW"},
    {"date":"17 NOV","time":"12:00","region":"GLOBAL","event":"Central bank commentary watch (illustrative)","impact":"MEDIUM"},
]

@app.get("/")
def home():
    return FileResponse(FRONTEND / "index.html")

@app.get("/api/health")
def health():
    return {"status":"ok","app":"EVIL EYE TERMINAL","version":app.version,"data_mode":"illustrative_demo","timestamp":datetime.now(timezone.utc).isoformat()}

@app.get("/api/market/overview")
def overview():
    indices = [a for a in ASSETS if a["type"] == "Index"]
    return {
        "as_of":datetime.now(timezone.utc).isoformat(),
        "indices":indices,
        "regions":["India","Americas","Europe","Asia Pacific","Global"],
        "market_status":"DEMO SNAPSHOT",
        "breadth":{"advances":1248,"declines":986,"unchanged":142},
        "notice":"Illustrative reference values. Not live market quotes."
    }

@app.get("/api/market/assets")
def assets(q: Optional[str] = Query(default=None), kind: Optional[str] = Query(default=None), region: Optional[str] = Query(default=None)):
    rows = ASSETS
    if q:
        term=q.lower()
        rows=[a for a in rows if term in a["symbol"].lower() or term in a["name"].lower()]
    if kind and kind != "All":
        rows=[a for a in rows if a["type"] == kind]
    if region and region != "All":
        rows=[a for a in rows if a["region"] == region or (region == "Global" and a["region"] == "Global")]
    return {"items":rows,"count":len(rows),"data_mode":"illustrative_demo"}

@app.get("/api/market/chart")
def chart(symbol: str = "NIFTY", period: str = "1D"):
    asset=next((a for a in ASSETS if a["symbol"] == symbol.upper()),ASSETS[0])
    count={"1D":32,"1W":35,"1M":30,"3M":36,"1Y":40}.get(period,32)
    seed=sum(ord(c) for c in asset["symbol"])
    base=asset["price"]*0.985
    points=[]
    for i in range(count):
        wave=((i*17+seed*3)%23-11)/1000
        drift=(i/max(count-1,1))*(asset["change"]/100)
        points.append({"label":f"{i+1:02d}","value":round(base*(1+wave+drift),4)})
    return {"symbol":asset["symbol"],"period":period,"points":points,"data_mode":"illustrative_demo"}

@app.get("/api/news")
def news():
    return {"items":NEWS,"data_mode":"sample_headlines"}

@app.get("/api/calendar")
def calendar():
    return {"items":EVENTS,"data_mode":"illustrative_events"}
