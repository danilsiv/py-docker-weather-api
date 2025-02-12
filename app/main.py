import os
import requests


def get_weather() -> None:
    URL = "https://api.weatherapi.com/v1/current.json?"
    FILTERING = "Paris"

    API_KEY = os.getenv("API_KEY")
    if not API_KEY:
        raise ValueError("The API_KEY must be set!")

    response = requests.get(URL + f"key={API_KEY}&q={FILTERING}")
    data = response.json()

    city = data["location"]["name"]
    country = data["location"]["country"]
    local_time = data["location"]["localtime"]
    temp = data["current"]["temp_c"]
    weather = data["current"]["condition"]["text"]

    print(f"{city}/{country} {local_time} Weather: {temp} Celsius, {weather}")


if __name__ == "__main__":
    get_weather()
