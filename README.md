# EVIL EYE TERMINAL
**See Beyond The Market.**

A pure-black, responsive, cross-market educational research workspace built with FastAPI and vanilla JavaScript.

## v0.3.0 — India + global reference universe
- India: NSE/BSE indices and selected company reference instruments
- Americas: S&P 500, Dow Jones, NASDAQ Composite and Russell 2000
- Europe: FTSE 100, DAX and CAC 40
- Asia Pacific: Nikkei 225, Hang Seng and S&P/ASX 200
- Global reference instruments: gold, Brent crude and selected FX pairs
- Region filters, instrument search, screener and session watchlist
- SVG reference chart with selectable display periods
- Sample news desk and illustrative event calendar
- CSV export, responsive layout and FastAPI JSON endpoints
- Pure black background (#000000), charcoal surfaces, white typography and restrained amber/green accents; no blue theme

## Run locally (Windows)
```bat
py -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
uvicorn backend.main:app --reload
```
Open http://127.0.0.1:8000

## API
- `GET /api/health`
- `GET /api/market/overview`
- `GET /api/market/assets?q=&kind=&region=`
- `GET /api/market/chart?symbol=NIFTY&period=1D`
- `GET /api/news`
- `GET /api/calendar`

## Data integrity and next integration
The bundled dataset is **illustrative demo data**. It is not real-time, delayed exchange data, official news, investment research or a source for financial decisions. Chart history is generated as a visual placeholder and must not be interpreted as historical market performance. No order entry or trading functionality is provided.

A production data adapter must be connected to a market-data vendor whose contract explicitly permits the intended instruments, exchanges, display, storage, redistribution and user access. Keep credentials server-side in environment variables; never commit API keys. Before commercial use, review provider terms, exchange licensing, privacy, security and applicable legal requirements.

## Project structure
```
backend/main.py
backend/__init__.py
frontend/index.html
frontend/styles.css
frontend/app.js
requirements.txt
```

## Version
0.3.0 — cross-market black-theme research workspace.
