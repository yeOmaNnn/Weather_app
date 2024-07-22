import requests

from app.schema import WeatherResponse

API_KEY = "f80c313b3cd1d190d87bcaa3ac0302cc"

def get_weather(city: str):
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric'
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        temp = float(data["main"]["temp"])
        wind_speed = float(data["wind"]["speed"])
        description = data['weather'][0]['description']
        return WeatherResponse(name=data["name"], current_temp=temp, wind_speed=wind_speed, description=description)
    else:
        return None



