# BUY THE API KEY HERE: https://platform.openai.com/signup
from flask import Flask,request
import git

app = Flask(__name__)

@app.route('/update_server')
def webhook():
       
    repo = git.Repo('/home/Cookarino/mysite/ICT-FAIR-WEBSITE')
    origin = repo.remotes.origin
    origin.pull()
    return '', 200
        


@app.route("/")
def home():
    return '<a target="_blank" href="https://platform.openai.com/signup">Click here :)</a>'


if __name__ == '__main__' :
    app.run(debug=True)

# testing sync again.8