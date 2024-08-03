import requests

def get_weather(api_key, city, units='metric'):
    """
    Fetches the current temperature and humidity for a given city.

    Parameters:
    - api_key (str): Your API key for OpenWeatherMap.
    - city (str): The city name.
    - units (str): Units of measurement. 'metric' for Celsius, 'imperial' for Fahrenheit.

    Returns:
    - dict: A dictionary containing temperature and humidity.
    """
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units={units}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        weather = {
            'temperature': data['main']['temp'],
            'humidity': data['main']['humidity']
        }
        return weather
    else:
        return None

if __name__ == "__main__":
    api_key = '4f54453d8fd4dd72e02dbf850fa8fbf8'  # Replace with your actual API key
    city = 'Singapore'  # Replace with your desired city
    weather = get_weather(api_key, city)

    if weather:
        print(f"Temperature in {city}: {weather['temperature']}°C")
        print(f"Humidity in {city}: {weather['humidity']}%")
    else:
        print("Failed to retrieve weather data.")
