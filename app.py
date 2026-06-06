import os
from flask import Flask, render_template
from model import db, Ticket, Note
from routes import bp
from datetime import datetime
 
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(os.path.abspath(os.path.dirname(__file__)), 'crm.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
 
db.init_app(app)
 
# ✅ FIX: Remove url_prefix here because routes.py already has /api/tickets
#    If you kept url_prefix='/api', the URL would become /api/api/tickets
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
