from flask import Flask, render_template
import camCommands

app = Flask(__name__)

@app.route('/')
    return "Hello World"
#def index():
#    return render_template('index.html')

@app.route('/takeStill')
def takeStill():
    camCommands.photo()
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')