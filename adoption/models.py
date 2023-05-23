from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


def connect_db(app):
    """Connect to database."""

    db.app = app
    db.init_app(app)


class Pet(db.model):

    __tablename__= "pets"

    id= db.column(db.integer, 
        primarykey= True, 
        autoincrement=True)
    name = db.column(db.string(20), 
        nullable=False)
    species = db.column(db.string(20), 
        nullable=False)
    photo_url= db.column(db.string)
    age= db.column(db.integer)
    notes=db.column(db.string(100))
    available= db.column(db.boolean, 
        nullable=False, 
        default=True)


