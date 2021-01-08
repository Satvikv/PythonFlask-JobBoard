from flask import Blueprint, render_template
from flask import Flask

app = Flask(__name__)

@app.route('/')
@app.route('/jobs')
def jobs():
    return render_template('index.html')

if __name__ == '__main__':
    app.run()
