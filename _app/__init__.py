import random

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def main_page():
    pil, jaw = [*range(1, 7)], [*range(1, 7)]
    random.shuffle(pil)
    random.shuffle(jaw)
    return render_template('main.html', pil=pil, jaw=jaw)
