from flask import Flask, render_template
import camCommands
from os import listdir

app = Flask(__name__)


@app.route('/')
def index():
    imageList = os.listdir('./static/images/')
    return render_template('index.html', response="", message="", images=imageList)


@app.route('/takeStill')
def takeStill():
    print("take still triggered")
    photoResult = camCommands.photo()
    imageList = os.listdir('./static/images/')
    return render_template('index.html', response="Photo Taken", message=photoResult, images=imageList)


# make externally visible
# doesn't appear to do anything have to launch as flask run --host=0.0.0.0
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
