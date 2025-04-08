# ============================================================
# Columbia University Challenge: Implement the "weather" command.
#
# When a user sends a message like "weather London",
# your agent should fetch live weather data for the given city.
#
# Hints:
# 1. Use the 'requests' library for HTTP GET requests.
# 2. Consider using the OpenWeatherMap API: https://openweathermap.org/api.
#    (You will need to sign up for a free API key.)
# 3. Parse the input to extract the city name.
# 4. Construct the API URL using the city name and your API key.
# 5. Check if the response is successful, then parse the JSON to extract temperature and weather conditions.
#
# Useful resources:
# - Requests documentation: https://docs.python-requests.org/en/latest/
# - OpenWeatherMap API: https://openweathermap.org/api
# ============================================================

import requests

WEATHER_KEY = "4fce4250d574a98fce6a1867539175ea"

def handle_message(message: str) -> str:
    message = message.lower()
    if "hello" in message:
        return "Hello, welcome to NEAR AI!"
    elif message.startswith("weather"):
        # TODO: Implement the weather command.
        words = message.split()
        city = words[1]
        response = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={OPEN_AI_KEY}")

        if response.status_code == 200:
            data = response.json()
            temperature = data.get("main", {}).get("temp")
            condition = data.get("weather", [{}])[0].get("description")
            return f"The weather in {city} is {temperature}°C and {condition}."
        else:
            return "Failed to fetch weather data. Please try again later."
        # Steps:
        #   1. Split the message to extract the city name.
        #   2. Verify that a city name was provided.
        #   3. Build the API URL using the city name and your OpenWeatherMap API key.
        #      (Replace 'YOUR_API_KEY' with your actual key.)
        #   4. Make a GET request to the weather API.
        #   5. If the response is successful, parse the JSON to extract temperature and condition details.
        #   6. Return a formatted string with the weather information.
        pass
    else:
        return "I'm sorry, I didn't understand your message."

# Optional testing block:
if __name__ == "__main__":
   user_input = input("Enter a message for the agent: ")
   print(handle_message(user_input))
