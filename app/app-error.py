from flask import Flask 
app = Flask(__name__)


@app.route("/")
def index():
    return jsonify({"testim":"test"})


@app.route("/health")
def health():
    return jsonify({"health":"check"})





if __name__ == "__main__":
    app.run(host="0.0.0.0")

_
