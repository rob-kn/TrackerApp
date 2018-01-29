from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, SelectField, SubmitField
from wtforms.validators import DataRequired, input_required, ValidationError

status_choices = [(0, ''),
                  (1, 'NOT_STARTED'),
                  (2, 'IN_PROGRESS'),
                  (3, 'COMPLETE')]
priority_choices = [(0, '')] + [(i, i) for i in range(1, 10)]

class DefaultCheck(object):
    def __init__(self, message=None):
        if not message:
            message = u'No selection made!'
        self.message = message

    def __call__(self, form, field):
        if field.data == 0:
            raise ValidationError(self.message)


class AddTask(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    status = SelectField('Status', choices=status_choices, coerce=int, validators=[DefaultCheck()])
    priority = SelectField('Priority', choices=priority_choices, coerce=int, validators=[DefaultCheck()])
    desc = StringField('Description', validators=[DataRequired()])
    submit = SubmitField('Submit')


class AddItem(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    desc = StringField('Description', validators=[DataRequired()])
    submit = SubmitField('Submit')


class AddExpense(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    cost = FloatField('Cost', validators=[DataRequired()])
    desc = StringField('Description', validators=[DataRequired()])
    submit = SubmitField('Submit')
