from flask import Flask, render_template

# initilization flask
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/about')
def about():
    return render_template('about.html')

app.run(debug=True)

# if __name__ == '__main__':
#   app.run(host='127.0.0.1', port=8000, debug=True)