from flask import render_template, request, redirect, url_for
from app import app
from app.controllers import controller

@app.route('/')
def index():
    return render_template('index.html', tasks=controller.task_list.tasks)

@app.route('/add_task', methods=['POST'])
def add_task():
    title = request.form['title']
    description = request.form['description']
    controller.add_task(title, description)
    return redirect(url_for('index'))

@app.route('/remove_task/<int:task_index>')
def remove_task(task_index):
    task = controller.task_list.tasks[task_index]
    controller.remove_task(task)
    return redirect(url_for('index'))

@app.route('/complete_task/<int:task_index>')
def complete_task(task_index):
    task = controller.task_list.tasks[task_index]
    controller.complete_task(task)
    return redirect(url_for('index'))

@app.route('/fail_task/<int:task_index>')
def fail_task(task_index):
    task = controller.task_list.tasks[task_index]
    controller.fail_task(task)
    return redirect(url_for('index'))
