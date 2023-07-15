from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired


class SearchForm(FlaskForm):
    token = PasswordField('Персональный токен', validators=[DataRequired()],
                          render_kw={"class": "form-control"})
    filter = StringField('ID фильтра', validators=[DataRequired()],
                         render_kw={"class": "form-control"})
    download = SubmitField('Скачать', render_kw={"class": "btn btn-primary"})
