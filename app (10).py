#7. Integrate a SQLite database with Flask to perform CRUD operations on a list of items.
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key_here'  # Change this to a random secret key
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///items.db'  # SQLite database file
db = SQLAlchemy(app)


class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)

    def __repr__(self):
        return f'<Item {self.name}>'


# Creating tables within the application context
with app.app_context():
    db.create_all()


# Routes and other code remain the same...




@app.route('/')
def index():
    items = Item.query.all()
    return render_template('index.html', items=items)


@app.route('/add', methods=['POST'])
def add():
    item_name = request.form['item']
    new_item = Item(name=item_name)
    try:
        db.session.add(new_item)
        db.session.commit()
        flash('Item added successfully!', 'success')
    except:
        db.session.rollback()
        flash('Error occurred while adding item.', 'error')
    return redirect(url_for('index'))


@app.route('/delete/<int:item_id>', methods=['POST'])
def delete(item_id):
    item_to_delete = Item.query.get_or_404(item_id)
    try:
        db.session.delete(item_to_delete)
        db.session.commit()
        flash('Item deleted successfully!', 'success')
    except:
        db.session.rollback()
        flash('Error occurred while deleting item.', 'error')
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(host="0.0.0.0",debug=True,port=5005)
