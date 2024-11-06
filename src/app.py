from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "CS2 Bot Analysis Tool"

if __name__ == "__main__":
    app.run(debug=True)
