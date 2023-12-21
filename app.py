
from flask import Flask,render_template,jsonify, request
from flask import send_file

from pyhtml2pdf import converter

import socket
## getting the hostname by socket.gethostname() method
hostname = socket.gethostname()
## getting the IP address using socket.gethostbyname() method
ip_address = socket.gethostbyname(hostname)


import os
os.system("wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb")
os.system("dpkg -x deb_package.deb .")


from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

options = Options()
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)



def create_app():
    app = Flask(__name__)
    @app.route("/")
    def index():
         return 'hello world'
    @app.route("/url")
    def change_ip() :
         name = request.args.get('name')
         converter.convert(name, 'sample.pdf',timeout=4, print_options={"scale": 1,"paperHeight":12})
         return send_file("sample.pdf", as_attachment=True)
    return app
    
app = create_app()
    



if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080)
