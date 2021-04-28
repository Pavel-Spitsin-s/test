from flask import Flask

app = Flask(__name__)


@app.route("/")
@app.route("/index")
def index():
    return "Hello World!"


app.run(port=8080, host="127.0.0.1")
