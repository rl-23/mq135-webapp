import serial
import time
import re
from flask import Flask, redirect, url_for, render_template
import random


while True:

    app = Flask(__name__)

    @app.route("/")
    def home():
        
        f = open("appdatareads.txt", "r")
        temp_string = str(f.read())
        re.sub(r'[^\w]', ' ', temp_string)
        return render_template("index.html", appdata=temp_string)


    if __name__ == "__main__":
        app.run(host="localhost", port=8000, debug=True)
    
    