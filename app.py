from flask import Flask, render_template

app = Flask(__name__)

@app.route('/youtube')
def youtube():
    return render_template('youtube.html')