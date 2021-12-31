from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return '''
    <html>
        <head>
            <title> Flask App </title>
        </head>
        <body>
            <center>  <h1> Welcome to Home Page </h1> </center>
            <hr>
            <div>
                <br>
                <center>
                    <button>
                        <a href="http://127.0.0.1:5000/login">Login</a>
                    </button>
                    <button>
                        <a href="http://127.0.0.1:5000/signup">Signup</a>
                    </button>
                </center>
            </div>
            <hr>
        </body>
    </html>
    '''

@app.route("/login")
def login():
    return '''
    <html>
        <head>
            <title> Flask App </title>
        </head>
        <body>
            <center>  <h1> Welcome to Login Page </h1> </center>
            <hr>
            <form action="#">
                <center>
                <div>
                    <label for="email">
                        <input placeholder="Email" type="email">
                    </label>
                    <br><br>
                    <label for="password">
                        <input placeholder="Password" type="password">
                    </label>
                    <br><br>
                    <input id="CheckLogin" type="checkbox">
                    <label for="CheckLogin">
                        <span >Remember me</span>
                    </label>
                    <br><br>
                    <a href="#">Forgot Password?</a>
                    <br><br>
                    <a href="http://127.0.0.1:5000/"><button type="button">Cancel</button></a>
                    <button type="button">Sign in</button>
                </div>
                </center>
            </form>
        </body>
    </html>
    '''

@app.route("/signup")
def signup():
    return '''
    <html>
        <head>
            <title> Flask App </title>
        </head>
        <body>
            <center>  <h1> Welcome to Signup Page </h1> </center>
            <hr>
            <form action="#">
                <center>
                <div>
                    <label for="user">
                        <input placeholder="Username" type="user">
                    </label>
                    <br><br>
                    <label for="email">
                        <input placeholder="Email" type="email">
                    </label>
                    <br><br>
                    <label for="phone">
                        <input placeholder="Phone Number" type="phone">
                    </label>
                    <br><br>
                    <label for="password">
                        <input placeholder="Password" type="password">
                    </label>
                    <br><br>
                    <a href="http://127.0.0.1:5000"><button type="button">Reset</button></a>
                    <button type="button">Sign in</button>
                </div>
                </center>
            </form>
        </body>
    </html>
    '''