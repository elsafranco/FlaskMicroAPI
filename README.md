# Flask Student Database API

Minimal Flask API with GET and POST endpoints.

## Endpoints
GET /hello → returns welcome message (JSON)  
GET /data → returns student list (JSON)  
POST /data → adds a new student using JSON body

## Run locally
pip install -r requirements.txt  
python app.py

Open:
http://127.0.0.1:5000/hello  
http://127.0.0.1:5000/data

Tested using Postman (GET and POST).
