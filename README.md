# Weather API Application

A Python-based application that retrieves and displays real-time weather information using the OpenWeather API.

## Project Overview

This project is a Python-based Weather API Application that retrieves real-time weather information for a user-specified city using the OpenWeather API.

The application demonstrates how Python can communicate with an external API, process JSON responses, handle errors, and display useful weather information in a simple and user-friendly format.

## Features

- Retrieve real-time weather information for a city
- Display current temperature in Celsius
- Display weather conditions
- Display humidity
- Display wind speed
- Handle invalid city names
- Handle API and connection errors
- Securely store the API key using environment variables
- Use `.gitignore` to prevent sensitive files from being uploaded to GitHub

## Technologies Used

- Python
- Requests
- OpenWeather API
- python-dotenv
- Git
- GitHub

## Weather Information Provided

The application retrieves and displays:

- City Name
- Temperature
- Weather Description
- Humidity
- Wind Speed

## Project Structure
```text
Weather-API-Application/
│
├── weather.py
├── requirements.txt
├── README.md
├── .gitignore
└── .env