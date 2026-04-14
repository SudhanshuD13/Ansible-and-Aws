from flask import Flask, render_template_string

app = Flask(__name__)

@app.route("/")
def home():
    return render_template_string("""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Ansible App</title>
        <style>
            body {
                margin: 0;
                height: 100vh;
                display: flex;
                justify-content: center;
                align-items: center;
                font-family: Arial, sans-serif;
                color: white;
                text-align: center;
                background: linear-gradient(270deg, #ff7e5f, #feb47b, #6a11cb, #2575fc);
                background-size: 800% 800%;
                animation: gradientBG 10s ease infinite;
            }

            h1 {
                font-size: 2.5rem;
                background: rgba(0, 0, 0, 0.3);
                padding: 20px 40px;
                border-radius: 10px;
            }

            @keyframes gradientBG {
                0% { background-position: 0% 50%; }
                50% { background-position: 100% 50%; }
                100% { background-position: 0% 50%; }
            }
        </style>
    </head>
    <body>
        <h1>A warm welcome to Ansible deployed app<br>By Sudhanshu 🚀</h1>
    </body>
    </html>
    """)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
