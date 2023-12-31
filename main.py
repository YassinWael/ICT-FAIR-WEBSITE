# BUY THE API KEY HERE: https://platform.openai.com/signup
from flask import Flask

app = Flask(__name__)


@app.route("/")
def home():
    return '<a target="_blank" href="https://platform.openai.com/signup">Click here</a>'


if __name__ == '__main__' :
    app.run(debug=True)