# main.py
from fastapi import FastAPI
from scraper import get_live_scores

app = FastAPI()

@app.get("/live-scores")
def live_scores():
return {"score": get_live_scores()}
https://cricketlive-api.onrender.com
@app.get("/")
def home():
    return {"status": "ok"}

