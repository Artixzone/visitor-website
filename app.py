
from flask import Flask, request
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def home():
   visitor_ip = request.headers.get("CF-Connecting-IP") or request.remote_addr
    visit_time = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

    print("Visitor IP:", visitor_ip)

    return f"""
    <html>
    <head>
        <title>Visitor Information</title>
        <style>
            body {{
                background: #111827;
                color: white;
                font-family: Arial;
                text-align: center;
                padding: 60px;
            }}
            .card {{
                background: #1f2937;
                padding: 30px;
                border-radius: 15px;
                display: inline-block;
            }}
        </style>
    </head>
    <body>
        <div class="card">
            <h1>Visitor Information</h1>
            <h2>Connection successful!</h2>
            <p>Your IP address: {visitor_ip}</p>
            <p>Visit time: {visit_time}</p>
        </div>
    </body>
    </html>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
