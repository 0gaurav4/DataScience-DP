from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello Ujjwal i am here'

if __name__ == '__main__':
    app.run()