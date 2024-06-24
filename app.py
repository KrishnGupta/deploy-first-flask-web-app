from flask import Flask

# Create a Flask application instance
app = Flask(__name__)

# Define a route for the root URL (/) - this is the default route
@app.route('/')
def hello():
    return 'Hello, this is your first web app!'

# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True)
