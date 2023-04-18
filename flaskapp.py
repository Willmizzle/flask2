# Import the Flask module and create a web app from Flask
from flask import Flask

# Create a new instance of the Flask class
app = Flask(__name__)

# Define a route for the root URL ("/") and associate it with a function, `hello_world`
@app.route('/')
def hello_world():
    return 'Hello, World!'

# Check if the executed file is the main program and run the app
if __name__ == '__main__':
    app.run()
