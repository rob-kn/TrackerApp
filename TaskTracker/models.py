from TaskTracker import db
from sqlalchemy.sql import func
from datetime import datetime


class Tasks(db.Model):
    # to do list
    id = db.Column('task_id', db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    status = db.Column(db.String(50))
    priority = db.Column(db.Integer)
    desc = db.Column(db.String(500))
    date_created = db.Column(db.DateTime(timezone=True), server_default=func.now())

    def __init__(self, title, status, priority, desc):
        self.title = title
        self.status = status
        self.priority = priority
        self.desc = desc
        self.date_created = datetime.now()

    def __repr__(self):
        return '<Task {0}: {1}>'.format(self.id, self.title)


class Items(db.Model):
    # shopping list
    id = db.Column('item_id', db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    status = db.Column(db.String(50))
    desc = db.Column(db.String(500))
    date_created = db.Column(db.DateTime(timezone=True), server_default=func.now())

    def __init__(self, title, status, desc):
        self.title = title
        self.status = status
        self.desc = desc
        self.date_created = datetime.now()

    def __repr__(self):
        return '<Item {0}: {1}>'.format(self.id, self.title)


class Expenses(db.Model):
    # track expense categories and cost
    id = db.Column('expense_id', db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    cost = db.Column(db.Float())
    category = db.Column(db.String(50))
    desc = db.Column(db.String(500))
    date_created = db.Column(db.DateTime(timezone=True), server_default=func.now())

    def __init__(self, title, cost, category, desc):
        self.title = title
        self.cost = cost
        self.category = category
        self.desc = desc
        self.date_created = datetime.now()

    def __repr__(self):
        return '<Expense {0}: {1}>'.format(self.id, self.title)
