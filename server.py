import os
import time
import psutil
from flask import Flask, render_template, jsonify
from flask_socketio import SocketIO
from datetime import datetime

app = Flask(__name__)

app.config["SECRET_KEY"] = "neocontrol-secret"

socketio = SocketIO(
    app,
    cors_allowed_origins="*"
)

start_time = time.time()


# -------------------------
# HOME
# -------------------------

@app.route("/")
def home():
    return render_template("dashboard.html")


# -------------------------
# TOOLS PAGE
# -------------------------

@app.route("/tools")
def tools():
    return render_template("tools.html")


# -------------------------
# SERVER STATS API
# -------------------------

@app.route("/api/status")
def status():

    uptime = int(time.time() - start_time)

    return jsonify({

        "status": "online",

        "cpu":
            psutil.cpu_percent(),

        "memory":
            psutil.virtual_memory().percent,

        "uptime":
            uptime,

        "time":
            datetime.now().strftime(
                "%H:%M:%S"
            )
    })


# -------------------------
# LIVE SOCKET UPDATES
# -------------------------

def send_stats():

    while True:

        data = {

            "cpu":
                psutil.cpu_percent(),

            "memory":
                psutil.virtual_memory().percent,

            "time":
                datetime.now().strftime(
                    "%H:%M:%S"
                )
        }


        socketio.emit(
            "stats",
            data
        )

        time.sleep(2)



@socketio.on("connect")
def connected():

    socketio.start_background_task(
        send_stats
    )


# -------------------------
# RUN SERVER
# -------------------------

if __name__ == "__main__":

    port = int(
        os.environ.get(
            "PORT",
            10000
        )
    )

    socketio.run(
        app,
        host="0.0.0.0",
        port=port
    )
