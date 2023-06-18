from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Fields(db.Model):
    """ Класс Поля """
    id = db.Column(db.Integer, primary_key=True)
    field_id = db.Column(db.String, unique=True, nullable=False)
    field_name = db.Column(db.String, nullable=False)

    """Метод для вывода объекта при print()"""
    def __repr__(self):
        return '<Field {} {}>'.format(self.field_id, self.field_name)
