from flask import Flask
app = Flask(__name__)


# @ : decorator
# http://localhost/ => root url address -> goto hello world()
@app.route('/')
# http://localhost/hello => path가 /hello인 url address -> goto helloworld()
@app.route('/hello')
@app.route('/world')
def HelloWorld():
    return "Hello World"

if __name__ == '__main__':
    app.debug = True
    app.run(host='127.0.0.1', port=5000)
