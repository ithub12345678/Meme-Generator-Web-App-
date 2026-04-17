#!/bin.python3
import requests

def my_custom_function():
    url = "https://api.apileague.com/retrieve-random-meme?keywords=rocket"
    api_key = "6cc9c5ab4b3f4f5f92fbf27461ddb26a"

    headers = {
        'X-Api-Key': api_key   # use correct capitalization
    }

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()   # convert to dictionary

        # Extract fields safely
        description = data.get("description")
        meme_url = data.get("url")

        print("Description:", description)
        print("URL:", meme_url)

        return data
    else:
        return f"Error: {response.status_code}"

if __name__ == "__main__":
    print(my_custom_function())
