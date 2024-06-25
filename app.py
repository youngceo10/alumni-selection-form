from flask import Flask, render_template, request, redirect, url_for
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    data = request.form.to_dict()
    # Process the data or save to a database/Google Drive
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
