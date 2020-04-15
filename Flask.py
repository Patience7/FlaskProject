from flask import Flask
from flask import redirect
from flask import url_for
from flask import request
from flask import Response
from flask import render_template
from werkzeug.utils import secure_filename


app = Flask(__name__, template_folder='./static')


@app.route('/success/<name>')
def success(name):
    return 'Welcome %s' % name


@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        user = request.form['nm']
        return redirect(url_for('success', name=user))
    else:
        user = request.args.get('nm')
        return(url_for('success', name=user))


@app.route('/', methods=['GET', 'POST'])
def student():
    # return render_template("index.html")
    # return render_template("student.html")
    return 'HELLO WORLD'


@app.route('/result', methods=['GET', 'POST'])
def result():
    if request.method == 'GET':
        result = request.form
        return render_template('result.html', result=result)


@app.route('/cookie', methods=['GET', 'POST'])
def index():
    return render_template('index.html')


@app.route('/upload', methods=['GET', 'POST'])
def upload():
    return render_template('upload.html')


@app.route('/uploader', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        f = request.files['file']
        f.save(secure_filename(f.filename))
        return "file uploaded successfully"


if __name__ == '__main__':
    app.run(port=5000)
