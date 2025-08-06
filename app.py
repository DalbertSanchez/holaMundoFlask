from flask import Flask
import os

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "¡Hola Mundo desde Flask en Render y Docker, Dalbert Sanchez 2023-0213!"

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 10000))  
    app.run(host='0.0.0.0', port=port)
