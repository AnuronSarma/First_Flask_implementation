from flask import Flask

# Creates an instance of the Flask class which will be the WSGI application
app = Flask(__name__)

@app.route("/")
def welcome():
    print("Home route accessed")  # Print to debug
    return "Welcome to my flask home page"

@app.route("/index")
def index():
    print("Index route accessed")  # Print to debug
    return "Welcome to my index page!!"

# Optional root route for testing
@app.route("/")
def root():
    print("Root route accessed")  # Print to debug
    return "This is the root page. Try /home or /index."

if __name__ == "__main__":
    app.run(debug=True, use_reloader=False)
