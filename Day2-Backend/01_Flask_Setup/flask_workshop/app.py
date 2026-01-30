# # app.py
# from flask import Flask

# # Create Flask application
# app = Flask(__name__)

# # Define a route - this is the URL path
# @app.route('/')
# def home():
#     return "<h1>Hello from Flask!</h1><p>My first web server! 🚀</p>"

# # Run the app
# if __name__ == '__main__':
#     app.run(debug=True)

#app.py
from flask import Flask

# create flask application
app = Flask(__name__)

#api route
@app.route("/")
def home():
    return "<h1>Hello from Flask!</h1><p>My first web server! 🚀</p>"

#run the app
if __name__ == "__main__":
    app.run(debug=True)