from flask import Flask, render_template
import json

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/tests')
def tests():
    return render_template('tests.html')

@app.route('/test')
def test():

    with open('static/question.json', encoding='utf-8') as f:
        questions_dict = json.load(f)

    return render_template('test.html', questions=questions_dict)

@app.route('/info')
def info():
    return render_template('info.html')

@app.route('/contacts')
def contacts():
    return render_template('contacts.html')

if __name__ == '__main__':
    app.run(debug=True)
