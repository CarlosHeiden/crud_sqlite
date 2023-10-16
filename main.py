from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/hello')
def hello_word():
    return 'HELLO WORD, voce acessou site teste FLASK'

import socket

def get_server_ip():
    hostname = socket.gethostname()
    server_ip = socket.gethostbyname(hostname)
    return server_ip




if __name__ == "__main__":

    server_ip = get_server_ip()
    app.run(host=f"{server_ip}", port=80, debug=True)

