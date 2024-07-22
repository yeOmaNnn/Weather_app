from pydantic import BaseModel, Field


class WeatherResponse(BaseModel):
    name: str = Field(..., title="City Name")
    current_temp: float = Field(..., title="Current Temperature")
    wind_speed: float = Field(..., title="Wind speed")
    description: str = Field(..., title="Description")


class CitiResponse(BaseModel):
    label: str = Field(..., title="City Name")
    value: str = Field(..., title="City Name")
    key: int = Field(..., title="City Name")


class AutocompleteResponse(BaseModel):
    cities: list[CitiResponse] = Field(default=[], title="Cities list")
