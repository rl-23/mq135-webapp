from flask import Flask
app = Flask(__name__)

@app.route("/")
def homepage():
    return """
    <!DOCTYPE">
 <html>
   <head>
      <title> Indoor Air Quality</title>
   </head>
   <body>
   <p>hi</p>
   </body>
</html>
    """

if __name__ == '__main__':
    app.run(use_reloader=True, debug=True)
