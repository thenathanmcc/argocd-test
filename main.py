from flask import Flask
import os

app = Flask(__name__)

@app.route("/")
def hello():
    return "If you are seeing this, that means v0.0.7 deployed automatically :)"


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True,host='0.0.0.0',port=port)