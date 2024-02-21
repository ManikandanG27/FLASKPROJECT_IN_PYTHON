from flask import Flask

# Create a Flask application instance
app = Flask(__name__)

# Route for the home page
@app.route('/')
def hello_world():
   return '<h1>Hello World<h1>'  # Return a simple HTML string

# Route with two integer parameters in the URL
@app.route('/score/<int:score>/<int:score_2>')
def hello_name(score, score_2):
   return ("the score you entered: {} {}".format(score, score_2))  # Return a string with the two scores

# Route for the '/world' URL
@app.route('/world')
def world():
   return "<h1>World<h1>"  # Return a simple HTML string

# Run the Flask app in debug mode if this script is executed directly
if __name__ == '__main__':
   app.run(debug=True)
