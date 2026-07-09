import os
import time
import psutil
import socket
from datetime import datetime

from flask import Flask, render_template_string, jsonify
from flask_socketio import SocketIO


app = Flask(__name__)

app.config["SECRET_KEY"] = "neocontrol"

socketio = SocketIO(
    app,
    cors_allowed_origins="*"
)


start_time = time.time()



HTML = """
<!DOCTYPE html>
<html>

<head>

<title>NeoControl</title>

<script src="https://cdn.socket.io/4.5.0/socket.io.min.js"></script>


<style>

body {

    margin:0;
    background:
    radial-gradient(circle at top,#1e293b,#020617);

    color:white;
    font-family:Arial;

}


.container {

    padding:40px;

}


h1 {

    font-size:45px;

}


.grid {

    display:grid;
    grid-template-columns:
    repeat(auto-fit,minmax(220px,1fr));

    gap:20px;

}


.card {

    background:
    rgba(255,255,255,.08);

    border:
    1px solid rgba(255,255,255,.15);

    border-radius:20px;

    padding:25px;

    backdrop-filter:blur(10px);

}


.value {

    font-size:35px;
    margin-top:15px;

}


.online {

    color:#22c55e;
    font-size:25px;

}



.logs {

    margin-top:30px;

    background:
    rgba(0,0,0,.4);

    padding:20px;

    border-radius:15px;

    height:250px;

    overflow:auto;

}


button {

    margin-top:30px;

    padding:15px 25px;

    border:none;

    border-radius:12px;

    background:#6366f1;

    color:white;

    cursor:pointer;

}



</style>

</head>



<body>


<div class="container">


<h1>
⚡ NeoControl
</h1>


<p>
Personal Server Command Center
</p>



<div class="grid">



<div class="card">

<h2>Status</h2>

<div class="online">
🟢 ONLINE
</div>

</div>



<div class="card">

<h2>CPU</h2>

<div class="value" id="cpu">
0%
</div>

</div>




<div class="card">

<h2>RAM</h2>

<div class="value" id="ram">
0%
</div>

</div>




<div class="card">

<h2>Time</h2>

<div class="value" id="time">
--
</div>

</div>



<div class="card">

<h2>Host</h2>

<div class="value" id="host">
--
</div>

</div>


</div>




<h2>
📡 Live Logs
</h2>


<div class="logs" id="logs">

[System] Starting NeoControl...

</div>



</div>






<script>


let socket = io();



socket.on(
"stats",
(data)=>{


cpu.innerHTML =
data.cpu+"%";


ram.innerHTML =
data.ram+"%";


time.innerHTML =
data.time;


host.innerHTML =
data.host;



let line =
document.createElement("div");


line.innerHTML =
"["+data.time+"] Server update";


logs.prepend(line);


}

);


</script>


</body>

</html>
"""




@app.route("/")
def home():

    return render_template_string(
        HTML
    )




def stats_loop():

    while True:


        socketio.emit(
            "stats",
            {

            "cpu":
            psutil.cpu_percent(),


            "ram":
            psutil.virtual_memory().percent,


            "time":
            datetime.now()
            .strftime("%H:%M:%S"),


            "host":
            socket.gethostname()

            }
        )


        time.sleep(2)





@socketio.on("connect")
def connect():

    socketio.start_background_task(
        stats_loop
    )






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
