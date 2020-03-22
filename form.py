from flask_wtf import FlaskForm
import wtforms


class myForm(FlaskForm):
    streamChoices = ['stream1', 'stream2', 'stream3']
    id = wtforms.TextField('stdid',
                           validators=[wtforms.validators.InputRequired()])
    stream = wtforms.SelectField('streams', choices=streamChoices)
