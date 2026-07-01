from flask import Flask, jsonify
import time

app = Flask(__name__)

# -------------------------
# HOME PAGE (modern UI)
# -------------------------
@app.route("/")
def home():
    return """
    <html>
    <head>
        <title>My Web Server</title>
        <style>
            body {
                margin: 0;
                font-family: Arial;
                background: radial-gradient(circle at top, #1e293b, #0f172a);
                color: white;
                text-align: center;
            }

            .container {
                padding-top: 120px;
            }

            .card {
                display: inline-block;
                padding: 30px;
                border-radius: 20px;
                background: rgba(255,255,255,0.06);
                border: 1px solid rgba(255,255,255,0.1);
                backdrop-filter: blur(10px);
            }

            h1 {
                font-size: 40px;
                margin-bottom: 10px;
            }

            button {
                margin-top: 15px;
                padding: 10px 20px;
                border-radius: 10px;
                border: none;
                cursor: pointer;
                background: #3b82f6;
                color: white;
            }

            button:hover {
                background: #2563eb;
            }

            a {
                color: #60a5fa;
                display: block;
                margin-top: 10px;
            }
        </style>
    </head>

    <body>
        <div class="container">
            <div class="card">
                <h1>🚀 Advanced Server</h1>
                <p>Your Render web server is running</p>

                <button onclick="alert('Server is alive 🔥')">Test Button</button>

                <a href="/dashboard">Go to Dashboard →</a>
            </div>
        </div>
    </body>
    </html>
    """

# -------------------------
# DASHBOARD PAGE
# -------------------------
@app.route("/dashboard")
def dashboard():
    return """
    <html>
    <head>
        <title>Dashboard</title>
        <style>
            body {
                background: #0f172a;
                color: white;
                font-family: Arial;
                text-align: center;
                padding-top: 80px;
            }

            .box {
                display: inline-block;
                padding: 25px;
                border-radius: 15px;
                background: rgba(255,255,255,0.05);
                border: 1px solid rgba(255,255,255,0.1);
            }

            #time {
                font-size: 28px;
                margin-top: 10px;
            }
        </style>
    </head>

    <body>
        <div class="box">
            <h1>📊 Dashboard</h1>
            <p>Live server info</p>

            <div id="time">Loading...</div>

            <script>
                setInterval(() => {
                    document.getElementById("time").innerHTML =
                        "⏱ " + new Date().toLocaleTimeString();
                }, 1000);
            </script>
        </div>
    </body>
    </html>
    """

# -------------------------
# API ENDPOINT (backend)
# -------------------------
@app.route("/api/status")
def status():
    return jsonify({
        "status": "online",
        "time": time.time(),
        "message": "Server is working"
    })

# -------------------------
# RUN SERVER
# -------------------------
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
