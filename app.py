from flask import Flask, render_template, request, redirect, url_for
import json
import os

app = Flask(__name__)
app.secret_key = 'your-secret-key-here'  # Needed for session security

# Function to load tasks from JSON file
def load_tasks():
    """Load tasks from JSON file"""
    if os.path.exists('tasks.json'):
        with open('tasks.json', 'r') as f:
            return json.load(f)
    return []

# Function to save tasks to JSON file
def save_tasks(tasks):
    """Save tasks to JSON file"""
    with open('tasks.json', 'w') as f:
        json.dump(tasks, f, indent=4)

# Route to display the task list with sorting feature
@app.route("/")
def index():
    filter_type = request.args.get("filter", "all")  # Get filter type (default: all)
    tasks = load_tasks()  # Load tasks from file

    # Apply filtering
    if filter_type == "pending":
        tasks = [task for task in tasks if not task["done"]]
    elif filter_type == "completed":
        tasks = [task for task in tasks if task["done"]]

    return render_template("index.html", tasks=tasks, filter_type=filter_type)

# Route to add a task
@app.route("/add", methods=["POST"])
def add_task():
    task_text = request.form.get("task", "").strip()
    if task_text:
        tasks = load_tasks()  # Load tasks from file
        tasks.append({"task": task_text, "done": False})
        save_tasks(tasks)  # Save tasks to file
    return redirect(url_for("index"))

# Route to mark a task as done
@app.route("/done/<int:task_id>")
def mark_done(task_id):
    tasks = load_tasks()
    if 0 <= task_id < len(tasks):
        tasks[task_id]['done'] = True
        save_tasks(tasks)  # Save tasks to file
    return redirect(url_for("index"))

# Route to delete a task
@app.route("/delete/<int:task_id>")
def delete_task(task_id):
    tasks = load_tasks()
    if 0 <= task_id < len(tasks):
        del tasks[task_id]
        save_tasks(tasks)  # Save tasks to file
    return redirect(url_for("index"))

# Run the Flask app
if __name__ == "__main__":
    app.run(debug=True)
