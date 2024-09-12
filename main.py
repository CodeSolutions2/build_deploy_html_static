from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return '<h1>Hello, World!</h1>'

if __name__ == '__main__':
    with app.test_request_context():
        html_content = app.dispatch_request()
    
    with open('index.html', 'w') as f:
        f.write(html_content)
