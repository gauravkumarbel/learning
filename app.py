from flask import Flask, render_template_string

app = Flask(__name__)

html_code = """
<!DOCTYPE html>
<html>
<head>
    <title>Technical Knowledge</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f4f6f8;
            text-align: center;
            padding: 50px;
        }
        .container {
            background: white;
            padding: 30px;
            border-radius: 10px;
            box-shadow: 0 0 10px rgba(0,0,0,0.1);
        }
        h1 {
            color: #2c3e50;
        }
        p {
            color: #555;
            font-size: 18px;
        }
        footer {
            margin-top: 20px;
            color: #888;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>Learn By Gaurav</h1>
        <h2>Technical Knowledge</h2>
        <p>Welcome to our learning base website where you can gain technical knowledge easily.</p>
        <footer>© 2026 Learn By Gaurav</footer>
    </div>
</body>
</html>
"""

@app.route("/")
def home():
    return render_template_string(html_code)

if __name__ == "__main__":
    app.run(debug=True)
