from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)

# Konfigurasi Database SQLite
db_path = os.path.join(os.path.dirname(__file__), 'finance.db')
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{db_path}'
db = SQLAlchemy(app)

# Model Database
class Transaction(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(100), nullable=False)
    amount = db.Column(db.Float, nullable=False)

with app.app_context():
    db.create_all()

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        desc = request.form.get('description')
        amt = request.form.get('amount')
        new_transaction = Transaction(description=desc, amount=float(amt))
        db.session.add(new_transaction)
        db.session.commit()
        return redirect('/')
    
    transactions = Transaction.query.all()
    total = sum(t.amount for t in transactions)
    return render_template('index.html', transactions=transactions, total=total)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
    