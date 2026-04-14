from flask import Flask
app = Flask(__name__)

@app.route("/")
def home():
    return "A warm welcome to Ansible deployed app By Sudhanshu!"

app.run(host="0.0.0.0", port=5000)
