from flask import Flask, render_template
import camCommands

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/takeStill')
def takeStill():
    print ("take still triggered")
    photoResult = camCommands.photo()
    return render_template('index.html', message=photoResult)

# make externally visible
# doesn't appear to do anything have to launch as flask run --host=0.0.0.0
if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')
