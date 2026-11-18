import os
import requests
from dotenv import load_dotenv
load_dotenv()


api_key = os.environ.get("OPENWEATHER_API_KEY")

while True:
    city = input("Enter city name: ")
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"



    try:
        response = requests.get(url)
        if response.status_code == 200:
                data = response.json()

                city_name = data["name"]
                temperature = data["main"]["temp"]
                humidity = data["main"]["humidity"]
                description = data["weather"][0]["description"]
                wind_speed = data["wind"]["speed"]

                print("\n===== WEATHER INFORMATION =====")
                print("City:", city_name)
                print("Temperature:", temperature, "°C")
                print("Weather:", description)
                print("Humidity:", humidity, "%")
                print("Wind Speed:", wind_speed, "m/s")

        elif response.status_code == 404:
                print("City not found. Please enter a valid city name.")
        
        else:
                print("Unable to fetch weather data.")
                print("Status Code:", response.status_code)

    except requests.exceptions.RequestException:
         print("Unable to connect to the weather service.")
         print("Please check your internet connection.")
                         
         
    choice = input("Do you want to enter another city?(yes/no): ")

    if choice.lower() == "no":
          break
        




