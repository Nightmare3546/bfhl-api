BFHL API

A simple FastAPI-based web service built for the Bajaj Finserv Hackathon Lab (BFHL) task.
It takes an input list of strings and classifies them into numbers, alphabets, and special characters, while also computing additional metadata like sum of numbers and custom concatenated string.

🚀 Deployment

This project is deployed on Render.
Public Base URL:

https://bfhl-api-x8po.onrender.com

📌 API Endpoints
1. Health Check
GET /


Response

{ "detail": "Not Found" }


(This is expected – the main logic is in /bfhl.)

2. Process Data
POST /bfhl

Request Body
{
  "data": ["a", "1", "334", "4", "R", "$"]
}

Example Response
{
  "is_success": true,
  "user_id": "YourName_ddmmyyyy",
  "email": "your_email@example.com",
  "roll_number": "ABCD123",
  "odd_numbers": ["1"],
  "even_numbers": ["334", "4"],
  "alphabets": ["a", "R"],
  "special_characters": ["$"],
  "sum": "339",
  "concat_string": "aR"
}

🛠️ Local Setup

Clone the repository:

git clone https://github.com/Nightmare3546/bfhl-api.git
cd bfhl-api


Create a virtual environment and install dependencies:

python -m venv venv
venv\Scripts\activate   # On Windows
pip install -r requirements.txt


Run the server locally:

uvicorn main:app --reload


Open in browser:

http://127.0.0.1:8000/docs


This opens the Swagger UI, where you can test the /bfhl endpoint.

📦 Tech Stack

Python 3.10+

FastAPI

Uvicorn

Deployed on Render

📷 Sample Run (Swagger UI)

Go to:

https://bfhl-api-x8po.onrender.com/docs


Expand POST /bfhl → Try it out

Enter:

{
  "data": ["x", "7", "12", "#", "y"]
}


Click Execute → Get the JSON response.

✍️ Author

Nightmare3546 (Dhruv Pisharody)
