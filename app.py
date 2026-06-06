import os
from flask import Flask, render_template
from model import db, Ticket, Note
from routes import bp
from datetime import datetime
 
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///crm.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
 
db.init_app(app)
 
app.register_blueprint(bp)
 
@app.route('/')
def index():
    return render_template('index.html')
 
with app.app_context():
    print("Attempting to create database")
    db.create_all()
    print("Database creation attempt finished!")
 
if __name__ == '__main__':
    app.run(debug=True)
