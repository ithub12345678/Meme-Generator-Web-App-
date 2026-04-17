# Meme Generator Web App 🎭

A simple and fun Flask-based web application that fetches and displays random memes using an external API. This project was built as a beginner-friendly exercise to understand the fundamentals of Flask, API integration, and dynamic HTML rendering.

---

## 🚀 Overview

This project demonstrates how to:

* Build a basic web server using Flask
* Integrate third-party APIs using Python (`requests`)
* Render dynamic content using Jinja2 templates
* Auto-refresh content on a webpage

Every time the page loads (or refreshes), a new meme is fetched and displayed.

---

## 🧩 Features

* 🔄 Auto-refresh every 30 seconds
* 🌐 Fetches memes from an external API
* 🖼️ Displays meme image dynamically
* 📝 Shows meme description/caption
* ⚡ Lightweight and beginner-friendly

---

## 🛠️ Tech Stack

* **Backend:** Python (Flask)
* **Frontend:** HTML, CSS
* **API Handling:** `requests` library
* **Templating Engine:** Flask (render_template)

---

## 📁 Project Structure

```
project-folder/
│
├── flask_app.py              # Flask backend
├── templates/
│   └── meme_index.html      # Frontend template
└── README.md
```

---

## ⚙️ Installation & Setup

### 1. Clone the repository

```bash
git clone <your-repo-link>
cd <project-folder>
```

### 2. Install dependencies

```bash
pip install flask requests
```

### 3. Set your API key

Replace your API key in `app.py`:

```python
api_key = "YOUR_API_KEY"
From API LEAGUE website
"https://apileague.com/"
```

*(Optional but recommended: use environment variables instead)*

---

## ▶️ Running the Application

```bash
python app.py
```

Open your browser and go to:

```
http://127.0.0.1:5000/
```

---

## 🔄 How It Works

1. Flask server starts and listens on localhost
2. On visiting `/`, it:

   * Sends a request to the meme API
   * Extracts meme URL and description
3. Passes data to `meme_index.html`
4. HTML renders the meme dynamically
5. Page refreshes every 30 seconds for a new meme

---

## 📌 Example Output

* Meme image displayed on screen
* Caption/description shown below
* Automatically updates without user interaction

---

## ⚠️ Notes

* Ensure your API key is valid
* Avoid exposing API keys publicly (use `.env` if needed)
* API response format may vary slightly

---

## 📈 Future Improvements

* Add a “Next Meme” button (manual refresh)
* Add category/keyword selection
* Improve UI with animations or themes
* Cache memes to reduce API calls
* Add error handling UI (e.g., API failure messages)

---

## 🎯 Learning Outcomes

This project helped reinforce:

* Flask routing and rendering
* Working with REST APIs
* JSON parsing in Python
* Basic frontend-backend integration

---

## 🙌 Acknowledgment

This was a **chill, timepass creative project** built as an entry point into Flask development—focused more on learning than perfection. The API and its content related information was obtained from the web - API LEAGUE website.

---

## 📜 License

Free to use and modify for learning purposes.
