from contextlib import asynccontextmanager

import requests
import uvicorn
from fastapi import FastAPI, Request, Query
from fastapi import HTTPException
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from starlette.staticfiles import StaticFiles

from app.config import DIR, DELLIN_API_KEY, DELLIN_URL, FASTAPI_HOST, FASTAPI_PORT
from app.schema import WeatherResponse, AutocompleteResponse
from app.weather import get_weather


@asynccontextmanager
async def lifespan(app: FastAPI):
    yield


app = FastAPI(lifespan=lifespan)
app.mount("/static", StaticFiles(directory=str(DIR) + "/static"), name="static")
templates = Jinja2Templates(directory=str(DIR) + "/templates")


@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {
        "request": request
    })


@app.get("/weather", response_model=WeatherResponse)
async def get_weather_info(city: str = Query("", title="City name")):
    weather_data = get_weather(city)
    if weather_data:
        return weather_data
    else:
        raise HTTPException(status_code=404, detail="City not found")


@app.get("/autocomplete", response_model=AutocompleteResponse)
async def autocomplete(q: str = Query("", title="City name")):
    try:
        if not q:
            return AutocompleteResponse()
        response = requests.post(DELLIN_URL + "/v2/public/kladr.json", json={
            "appkey": DELLIN_API_KEY,
            "q": q,
            "limit": 10
        })
        response.raise_for_status()
        cities = response.json()
        suggestions = [{"label": city["aString"], "value": city["searchString"], "key": city["cityID"], } for city in
                       cities["cities"]]
        return AutocompleteResponse(
            cities=suggestions
        )
    except requests.RequestException as e:
        print(e)
        raise HTTPException(status_code=500, detail="City not found - {}".format(e))


def run():
    uvicorn.run(app, host=FASTAPI_HOST, port=FASTAPI_PORT)


if __name__ == "__main__":
    run()
