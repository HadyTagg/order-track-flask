from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///database.db"

db = SQLAlchemy(app)


class Tracker (db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date_created = db.Column(db.DateTime, default=datetime.utcnow(), nullable=False)
    owner = db.Column(db.String(20), nullable=False)
    item = db.Column(db.String(20), nullable=False)
    description = db.Column(db.String(20), nullable=False)
    quantity = db.Column(db.Integer, default=0, nullable=False)
    status = db.Column(db.String(30), nullable=False)
    archived = db.Column(db.Integer, default=0, nullable=False)
    notes = db.Column(db.String(9999999), nullable=False)

    def __repr__(self):
        return '<Task %r>' % self.id


@app.route('/')
def index():
    return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True)
