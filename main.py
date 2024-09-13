from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return '''<!DOCTYPE html>
<html>
<head></head>
<body><h1>Hello, World!</h1><script></script>
</body>
</html>'''

if __name__ == '__main__':
    with app.test_request_context():
        html_content = app.dispatch_request()

    print(html_content)
