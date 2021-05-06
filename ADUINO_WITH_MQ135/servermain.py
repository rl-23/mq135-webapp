import serial
import time
import re
from flask import Flask, redirect, url_for, render_template
import random

f = open("appdatareads.txt", "r")

while True:

    temp_string = str(f.read())
  

    app = Flask(__name__)

    @app.route("/")
    def home():
        return render_template("index.html", appdata=temp_string, airmine="pog")


    if __name__ == "__main__":
        app.run(host="localhost", port=8000, debug=True)
    
    