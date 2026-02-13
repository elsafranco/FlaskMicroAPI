from flask import Flask, jsonify, request
app = Flask(__name__)

DATA = [
    {"id": 1, "major":"computer science", "name":"elsa", "age": 21},
    {"id": 2, "major":"computer science", "name":"will", "age": 22},
    {"id": 3, "major":"behavioral neuroscience", "name": "anna", "age": 21},
]
next_id = 4

@app.route("/")
def index():
    return """
    <h1>Student Database</h1>
    <p> Try these endpoints:</p>
    <ul>
        <li><a href="/hello">hello</a></li>
        <li><a href="/data">data</a></li>
    </ul>
    """


@app.route("/hello")
def hello():
    return jsonify({"message": "Hello! Welcome to my student database"})

@app.route("/data", methods=["GET", "POST"])
def data():
    if request.method == "GET":
        return jsonify({"data": DATA})

    # POST
    new_item = request.get_json()
    DATA.append(new_item)

    return jsonify({"message": "Student added!"}), 201


if __name__ == "__main__":
    app.run(debug=True)
