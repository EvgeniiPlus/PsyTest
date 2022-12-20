from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from flask_migrate import Migrate

from datetime import datetime

app = Flask(__name__)
app.debug = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://postgres:root@localhost:5432/eiro_db'


db = SQLAlchemy(app)
migrate = Migrate(app, db)


class Value(db.Model):
    __tablename__ = 'values'
    id = db.Column(db.Integer(), primary_key=True)
    inventory_number = db.Column(db.Integer(), nullable=False)
    name = db.Column(db.String(255), nullable=False)
    unit = db.Column(db.String(10), nullable=False)
    quantity = db.Column(db.Float(), nullable=False)
    room = db.Column(db.String(255), nullable=False)
    cost = db.Column(db.Float(), nullable=False)
    employee = db.Column(db.String(100), nullable=False)
    fin_account = db.Column(db.Integer(), nullable=False)
    financial_source = db.Column(db.String(100), nullable=False)
    created_on = db.Column(db.DateTime(), default=datetime.utcnow)

    def __repr__(self):
        return f"<{self.inventory_number} | {self.name[:15]} | {self.quantity} | {self.cost} | " \
               f"{self.employee_id} | {self.financial_source_id}>"
