from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/hello/<name>')
def hello(name):
    return render_template('hello.html', name=name)

@app.route('/echo', methods=['POST'])
def echo():
    message = request.form.get('message', '')
    return render_template('echo.html', message=message)

if __name__ == '__main__':
    app.run(debug=True)
