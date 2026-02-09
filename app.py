from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return """
    <h1>Welcome!</h1>
    <ul>
        <li><a href="/hello">/hello</a></li>
        <li><a href="/info">/info</a></li>
        <li><a href="/calc/3/5">/calc/3/5</a></li>
        <li><a href="/reverse/hello">/reverse/hello</a></li>
        <li><a href="/user/Anna/25">/user/Anna/25</a></li>
    </ul>
    """

#1
@app.route('/hello')
def hello_world():
    return "Hello, world!"

@app.route('/info')
def info():
    return "This is an informational page."


#2
@app.route('/calc/<int:a>/<int:b>')
def calc(a, b):
    return f"The sum of {a} and {b} is {a + b}."


#3
@app.route('/reverse/<text>')
def reverse_text(text):
    if len(text) == 0:
        return "Text must contain at least one character.", 400
    return text[::-1]

#4
@app.route('/user/<name>/<int:age>')
def user(name, age):
    if age < 0:
        return "Age cannot be negative.", 400
    return f"Hello, {name}. You are {age} years old."


if __name__ == "__main__":
    app.run(debug=True)
