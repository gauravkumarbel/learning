from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "<h1>Welcome to Gaurav Kumar Website</h1><p>This is my first Python website 🚀</p>"

@app.route("/about")
def about():
    return "<h2>About Page</h2><p>This is about my website.</p>"

if __name__ == "__main__":
    app.run(debug=True)
