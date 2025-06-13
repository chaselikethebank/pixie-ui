from flask import Flask, render_template, request, redirect, url_for, flash
import requests

app = Flask(__name__)

app.secret_key = 'pixie_clock_controller'

CLOCK_URL = "http://192.168.18.1/tubecolor"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/set_color', methods=['POST'])
def set_color():
    for i in range(1, 7):
        hue = request.form.get(f'h{i}')
        sat = request.form.get(f's{i}')
        val = request.form.get(f'v{i}')
        params = {
            "t": i,
            "h": hue,
            "s": sat,
            "v": val
        }
        try:
            requests.get("http://192.168.18.1/tubecolor", params=params, timeout=3)
        except:
            pass
    flash("Colors sent successfully!")
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
