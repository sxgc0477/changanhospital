from flask import Flask, render_template, url_for, redirect
from flask_bootstrap import Bootstrap
import json

app = Flask(__name__)

bootstrap = Bootstrap(app)
msg = json.load(open('resources/index_msg_en.json', 'r', encoding='utf-8'))


@app.route('/')
def index_echo():
    return index()


@app.route('/index')
def index():
    return render_template('index.html', msg=msg)


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html', msg=msg), 404


@app.errorhandler(500)
def internal_error(e):
    return render_template('500.html', msg=msg), 500


if __name__ == '__main__':
    app.run(port='80', debug=True)
