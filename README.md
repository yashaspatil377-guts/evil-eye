# EVIL EYE TERMINAL
**See Beyond The Market.**

A responsive, Bloomberg-inspired educational market-intelligence interface built with FastAPI and vanilla JavaScript.

## Run locally (Windows)

```bat
py -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
uvicorn backend.main:app --reload
```

Open http://127.0.0.1:8000

## Included
- Responsive dark terminal workspace
- Overview dashboard with index cards, chart periods, breadth and watchlist
- Market directory with search and CSV export
- Equity screener with filters
- Research snapshots, sample news desk and event calendar
- FastAPI endpoints under /api

## Important data notice
This repository currently uses **illustrative sample data**. It does not provide live market prices, official news, verified financial statements, investment advice, or trading functionality. Connect a properly licensed market-data provider before relying on market information or launching a commercial service.

## Project structure
```
backend/
  main.py
  __init__.py
frontend/
  index.html
  styles.css
  app.js
requirements.txt
```

## Version
0.2.0 — initial GitHub build.
