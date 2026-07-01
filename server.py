from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <html>
        <head>
            <title>My Server</title>
            <style>
                body {
                    margin: 0;
                    font-family: Arial;
                    background: linear-gradient(135deg, #0f172a, #1e293b);
                    color: white;
                    display: flex;
                    justify-content: center;
                    align-items: center;
                    height: 100vh;
                    flex-direction: column;
                }
                h1 {
                    font-size: 50px;
                    margin: 0;
                }
                p {
                    font-size: 18px;
                    opacity: 0.8;
                }
                .box {
                    padding: 30px;
                    border: 1px solid rgba(255,255,255,0.2);
                    border-radius: 15px;
                    background: rgba(255,255,255,0.05);
                    text-align: center;
                    backdrop-filter: blur(10px);
                }
                button {
                    margin-top: 20px;
                    padding: 10px 20px;
                    border: none;
                    border-radius: 10px;
                    background: #3b82f6;
                    color: white;
                    cursor: pointer;
                }
                button:hover {
                    background: #2563eb;
                }
            </style>
        </head>
        <body>
            <div class="box">
                <h1>🚀 Server Online</h1>
                <p>Your Render web server is working perfectly</p>
                <button onclick="alert('It works! 🔥')">Click Me</button>
            </div>
        </body>
    </html>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
