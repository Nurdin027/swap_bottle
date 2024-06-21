from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def main_page():
    import random
    pil, jaw = [], []
    while len(pil) < 6 or len(jaw) < 6:
        p = random.randint(1, 6)
        j = random.randint(1, 6)
        if p not in pil and len(pil) < 6:
            pil.append(p)
        if j not in jaw and len(jaw) < 6:
            jaw.append(j)
    return render_template('main.html', pil=pil, jaw=jaw)
