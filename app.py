
from flask import Flask,render_template,jsonify, request
from flask import send_file

from pyhtml2pdf import converter

import socket
## getting the hostname by socket.gethostname() method
hostname = socket.gethostname()
## getting the IP address using socket.gethostbyname() method
ip_address = socket.gethostbyname(hostname)

app = Flask(__name__)


@app.route("/url")
def change_ip() :
    name = request.args.get('name')
    converter.convert(name, 'sample.pdf',timeout=4, print_options={"scale": 1,"paperHeight":12})
    return send_file("sample.pdf", as_attachment=True)

if __name__ == "__main__":
    app.run(debug=True,host=ip_address)
