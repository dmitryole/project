from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

"""Класс Поля"""
class Fields(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    field_id = db.Column(db.String, unique=True, nullable=False)
    field_name = db.Column(db.String, nullable=False)

    """Метод для вывода объекта при print()"""
    def __repr__(self):
        return '<Fields {} {}>'.format(self.field_id, self.field_name)