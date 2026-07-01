from flask import Flask, render_template_string
from flask_socketio import SocketIO, send

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret'
socketio = SocketIO(app, cors_allowed_origins="*")

# -------------------------
# GAME-STYLE HOME PAGE
# -------------------------
@app.route("/")
def home():
    return render_template_string("""
<!DOCTYPE html>
<html>
<head>
<title>NeoChat Lobby</title>

<style>
body {
    margin: 0;
    font-family: Arial;
    background: radial-gradient(circle at top, #1f2937, #0b0f1a);
    color: white;
}

.lobby {
    text-align: center;
    padding-top: 80px;
}

.card {
    display: inline-block;
    padding: 30px;
    border-radius: 15px;
    background: rgba(255,255,255,0.05);
    border: 1px solid rgba(255,255,255,0.1);
}

button {
    padding: 12px 20px;
    margin-top: 20px;
    border: none;
    border-radius: 10px;
    background: #6366f1;
    color: white;
    cursor: pointer;
}

button:hover {
    background: #4f46e5;
}
</style>

</head>

<body>
<div class="lobby">
    <div class="card">
        <h1>🎮 NeoChat Lobby</h1>
        <p>Join the live chat server</p>
        <button onclick="window.location.href='/chat'">Enter Chat</button>
    </div>
</div>
</body>
</html>
""")

# -------------------------
# CHAT PAGE
# -------------------------
@app.route("/chat")
def chat():
    return render_template_string("""
<!DOCTYPE html>
<html>
<head>
<title>Chat Room</title>

<style>
body {
    margin: 0;
    font-family: Arial;
    background: #0b0f1a;
    color: white;
}

#chat {
    height: 80vh;
    overflow-y: scroll;
    padding: 20px;
}

input {
    width: 80%;
    padding: 10px;
    border-radius: 10px;
    border: none;
}

button {
    padding: 10px;
    border-radius: 10px;
    border: none;
    background: #4f46e5;
    color: white;
    cursor: pointer;
}

.msg {
    padding: 8px;
    margin: 5px 0;
    background: rgba(255,255,255,0.05);
    border-radius: 8px;
}
</style>

</head>

<body>

<div id="chat"></div>

<input id="msg" placeholder="Type message..." />
<button onclick="sendMsg()">Send</button>

<script src="https://cdn.socket.io/4.5.0/socket.io.min.js"></script>
<script>
var socket = io();

function sendMsg() {
    var input = document.getElementById("msg");
    socket.send(input.value);
    input.value = "";
}

socket.on("message", function(msg) {
    var div = document.createElement("div");
    div.className = "msg";
    div.innerHTML = msg;
    document.getElementById("chat").appendChild(div);
});
</script>

</body>
</html>
""")

# -------------------------
# CHAT BACKEND
# -------------------------
@socketio.on('message')
def handle_message(msg):
    send(msg, broadcast=True)

# -------------------------
# RUN SERVER
# -------------------------
if __name__ == "__main__":
    socketio.run(app, host="0.0.0.0", port=10000)
