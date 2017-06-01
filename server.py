from flask import Flask, render_template  # Import Flask to allow us to create our app.
app = Flask(__name__)    # Global variable __name__ tells Flask whether or not we are running the file
                         # directly, or importing it as a module.
@app.route('/')          # The "@" symbol designates a "decorator" which attaches the following
                         # function to the '/' route. This means that whenever we send a request to
                         # localhost:5000/ we will run the following "hello_world" function.
def index():       
  return 'No ninja here!'  # Return 'Hello World!' to the response.

@app.route('/ninja/')
def ninja():
	return render_template('ninja.html')

@app.route('/ninja/<ninja_color>')
def showNinja(ninja_color):
	if ninja_color == 'blue':
		return render_template('blue.html')
	elif ninja_color == 'orange':
		return render_template('orange.html')
	elif ninja_color == 'red':
		return render_template('red.html')
	elif ninja_color == 'purple':
		return render_template('purple.html')
	else:
		return render_template('else.html')

app.run(debug=True) 