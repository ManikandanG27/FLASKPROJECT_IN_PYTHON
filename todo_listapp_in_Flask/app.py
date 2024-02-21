from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# List to store todos
todos = []

# Route to render the home page
@app.route("/home")
def index_1():
    return render_template('a.html')

# Route to render the index page with the todos
@app.route('/')
def index():
    return render_template('index.html', todos=todos)

# Route to add a new todo
@app.route('/add', methods=['POST'])
def add():
    # Retrieve todo task from the form
    todo = request.form['todo']
    # Add the new todo to the list
    todos.append({'task': todo, 'done': False})
    # Redirect to the index page
    return redirect(url_for('index'))

# Route to edit a todo
@app.route('/edit/<int:index>', methods=['GET', 'POST'])
def edit(index):
    # Retrieve the todo to be edited
    todo = todos[index]
    if request.method == 'POST':
        # If the request method is POST, update the todo task
        todo['task'] = request.form['todo']
        # Redirect to the index page
        return redirect(url_for('index'))
    else:
        # If the request method is GET, render the edit page
        return render_template('edit.html', todo=todo, index=index)

# Route to mark a todo as done or undone
@app.route('/check/<int:index>')
def check(index):
    # Toggle the 'done' status of the todo
    todos[index]['done'] = not todos[index]['done']
    # Redirect to the index page
    return redirect(url_for('index'))

# Route to delete a todo
@app.route('/delete/<int:index>')
def delete(index):
    # Delete the todo from the list
    del todos[index]
    # Redirect to the index page
    return redirect(url_for('index'))

if __name__ == '__main__':
    # Run the Flask app in debug mode
    app.run(debug=True)
