from flask import render_template, redirect, flash, url_for, request
from TaskTracker import app, db
from TaskTracker.forms import AddTask, AddItem, AddExpense
from TaskTracker.models import Tasks, Items, Expenses


@app.route('/')
def home():
    return "Homepage"


@app.route('/all')
def show_all():
    return render_template('show_all.html', tasks=Tasks.query.all(), items=Items.query.all(),
                           expenses=Expenses.query.all())


@app.route('/new_task', methods=['GET', 'POST'])
def new_task():
    form = AddTask(request.form)
    if request.method == 'POST':
        if form.validate():
            task = Tasks(request.form['title'], request.form['desc'])

            db.session.add(task)
            db.session.commit()
            flash('Record was successfully added')
            return redirect(url_for('show_all'))
        else:
            flash('Please enter all the fields', 'error')
    return render_template('new_task.html', form=form)


@app.route('/new_item', methods=['GET', 'POST'])
def new_item():
    form = AddItem(request.form)
    if request.method == 'POST':
        print(form.validate())
        if form.validate():
            item = Items(request.form['title'], request.form['desc'])

            db.session.add(item)
            db.session.commit()
            flash('Record was successfully added')
            return redirect(url_for('show_all'))
        else:
            flash('Please enter all the fields', 'error')
    return render_template('new_item.html', form=form)


@app.route('/new_expense', methods=['GET', 'POST'])
def new_expense():
    form = AddExpense(request.form)
    if request.method == 'POST':
        if form.validate():
            expense = Expenses(request.form['title'], request.form['cost'], request.form['desc'])

            db.session.add(expense)
            db.session.commit()
            flash('Record was successfully added')
            return redirect(url_for('show_all'))
        else:
            flash('Please enter all the fields', 'error')
    return render_template('new_expense.html', form=form)


@app.route('/task/<task_id>')
def show_task(task_id):
    task = db.session.query(Tasks).filter_by(id=task_id).first()
    if task:
        return task.title + ' - ' + task.desc
    else:
        return 'No task found with this id.'


@app.route('/clear_db')
def clear_db():
    num_del_rows = Tasks.query.delete()
    num_del_rows = Items.query.delete()
    num_del_rows = Expenses.query.delete()
    task = Tasks('Task1', 'NOT_STARTED', 3, 'This is task 1')
    db.session.add(task)
    task = Tasks('Task2', 'IN_PROGRESS', 2, 'This is task 2')
    db.session.add(task)
    task = Tasks('Task3', 'NOT_STARTED', 8, 'This is task 3')
    db.session.add(task)

    item = Items('Item1', 'BOUGHT', 'This is item 1')
    db.session.add(item)
    item = Items('Item2', 'NOT BOUGHT', 'This is item 2')
    db.session.add(item)
    item = Items('Item3', 'NOT BOUGHT', 'This is item 3')
    db.session.add(item)

    expense = Expenses('Expense1', 12.0, 'Travel', 'This is expense 1')
    db.session.add(expense)
    expense = Expenses('Expense2', 6.0, 'Food', 'This is expense 2')
    db.session.add(expense)
    expense = Expenses('Expense3', 37.0, 'Travel', 'This is expense 3')
    db.session.add(expense)

    db.session.commit()
    return redirect(url_for('show_all'))
