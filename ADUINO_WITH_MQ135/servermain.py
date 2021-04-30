from flask import Flask, render_template

app = Flask('testapp')

@app.route('/')
def index():
    return render_template('index.html', appdata = 'test', airmine = 'test' )

if __name__ == '__main__':
    app.run()
