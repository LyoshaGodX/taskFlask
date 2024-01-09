from flask import render_template, request, redirect, url_for
from app import app
from app.controllers import controller

@app.route('/')
def index():
    tasks = controller.task_list.get_all_tasks()
    return render_template('index.html', tasks=tasks)

@app.route('/add_task', methods=['POST'])
def add_task():
    title = request.form['title']
    description = request.form['description']
    controller.add_task(title, description)
    return redirect(url_for('index'))

@app.route('/remove_task/<int:task_id>')
def remove_task(task_id):
    controller.task_list.remove_task(task_id)
    return redirect(url_for('index'))

@app.route('/complete_task/<int:task_id>')
def complete_task(task_id):
    controller.task_list.complete_task(task_id)
    return redirect(url_for('index'))

@app.route('/fail_task/<int:task_id>')
def fail_task(task_id):
    controller.task_list.fail_task(task_id)
    return redirect(url_for('index'))
