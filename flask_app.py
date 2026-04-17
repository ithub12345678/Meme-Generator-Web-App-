#!/bin/python3

from flask import Flask, render_template
import json
import requests

app = Flask(__name__)

def get_meme():	

    url = "https://api.apileague.com/retrieve-random-meme?min-rating=1.0"
    api_key = "6cc9c5ab4b3f4f5f92fbf27461ddb26a"

    headers = {
        'X-Api-Key': api_key   # use correct capitalization
    }

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()   # convert to dictionary

        # Extract fields safely
        meme_desc = data.get("description")
        meme_url = data.get("url")

      #  print("Description:", description)
      #  print("URL:", meme_url)

        return meme_desc, meme_url
    else:
        return f"Error: {response.status_code}"

@app.route("/")
def index():
	meme_desc,meme_photu = get_meme()
	return render_template("meme_index.html", meme_photu= meme_photu , meme_desc = meme_desc)

app.run(host = "0.0.0.0", port = 5000)
