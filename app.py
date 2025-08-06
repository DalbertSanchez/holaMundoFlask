from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "¡Hola Mundo desde Flask y Docker, Dalbert Sanchez 2023-0213!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
