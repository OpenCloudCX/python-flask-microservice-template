from flask import Flask
app = Flask(__name__)
@app.route('/status')
def status():
    return 'glhfdd', 200
if __name__ == '__main__':
    app.run('0.0.0.0', debug=True)
