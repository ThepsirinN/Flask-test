from flask import Flask

app = Flask(__name__)

@app.route("eiei/")
def hello_world():
    return "<p>Thepsirin Nawngerndee eiei</p>"