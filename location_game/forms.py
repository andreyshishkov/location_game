from flask_wtf import FlaskForm
from wtforms import SelectField, IntegerField, SubmitField
from wtforms.validators import DataRequired, NumberRange


class MessageForm(FlaskForm):
    way = SelectField(
        'Выберете сторону света, в которую желаете отправиться',
        choices=[
            'Север',
            'Восток',
            'Юг',
            'Запад',
        ],
        render_kw={
            'class': 'form-control',
        }
    )

    number_steps = IntegerField(
        'Как далеко планируется двигаться?',
        validators=[DataRequired(), NumberRange(min=1)],
        default=1,
        render_kw={
            'class': 'form-control',
        }
    )

    submit = SubmitField('В путь!')
