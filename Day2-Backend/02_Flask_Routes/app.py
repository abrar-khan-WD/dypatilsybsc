from flask import Flask

app = Flask(__name__)

# Home page
@app.route('/')
def home():
    return """
    <html>
    <head><title>Home</title></head>
    <body>
        <nav>
            <a href='/'>Home</a> | 
            <a href='/about'>About</a> | 
            <a href='/contact'>Contact</a>
        </nav>
        <h1>Welcome to My Website! 🏠</h1>
        <p>Navigate using the links above!</p>
    </body>
    </html>
    """

# About page
@app.route('/about')
def about():
    return """
    <html>
    <head><title>About</title></head>
    <body>
        <nav>
            <a href='/'>Home</a> | 
            <a href='/about'>About</a> | 
            <a href='/contact'>Contact</a>
        </nav>
        <h1>About Me 👤</h1>
        <p>I'm learning Flask at DY Patil with CodeGyaani!</p>
    </body>
    </html>
    """

# Contact page
@app.route('/contact')
def contact():
    return """
    <html>
    <head><title>Contact</title></head>
    <body>
        <nav>
            <a href='/'>Home</a> | 
            <a href='/about'>About</a> | 
            <a href='/contact'>Contact</a>
        </nav>
        <h1>Contact Me 📧</h1>
        <p>Email: abrar@gmail.com</p>
    </body>
    </html>
    """

#Route that accepts name
@app.route('/user/<name>')
def user(name):
    return "<h1>Hello, {}! Welcome to my website.</h1>".format(name)
if __name__ == '__main__':
    app.run(debug=True)