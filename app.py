from flask import Flask, render_template, request, redirect, url_for
from pymongo import MongoClient
from bson.objectid import ObjectId
# from functools import reduce
import os

host = os.environ.get('MONGODB_URI', 'mongodb://localhost:27017/my_app_db')
client = MongoClient(host=f'{host}?retryWrites=false')
db = client.get_default_database()
drinks_collection = db.drinks

app = Flask(__name__)

@app.route('/')
def homepage():
    """Show homepage."""
    return render_template('homepage.html', drinks=drinks_collection.find())

@app.route('/drinks/new')
def drinks_new():
    """Create a new drink."""
    return render_template('drinks_new.html', drink={})

@app.route('/drinks', methods=['POST'])
def drinks_submit():
    """Submit a new drink."""
    drink = {
        'name': request.form.get('name'),
        'price': request.form.get('price'),
        'description': request.form.get('description'),
        'images': request.form.get('images').split()
    }
    drink_id = drinks_collection.insert_one(drink).inserted_id
    return redirect(url_for('drinks_show', drink_id=drink_id))

@app.route('/drinks/<drink_id>')
def drinks_show(drink_id):
    """Show a single drink."""
    drink = drinks_collection.find_one({'_id': ObjectId(drink_id)})
    return render_template('drinks_show.html', drink=drink)

@app.route('/drinks/<drink_id>/edit')
def drinks_edit(drink_id):
    """Show the edit form for a drink."""
    drink = drinks_collection.find_one({'_id': ObjectId(drink_id)})
    return render_template('drinks_edit.html', drink=drink)

@app.route('/drinks/<drink_id>', methods=['POST'])
def drinks_update(drink_id):
    """Submit an edited drink."""
    updated_drink = {
        'name': request.form.get('name'),
        'price': request.form.get('price'),
        'description': request.form.get('description'),
        'images': request.form.get('images').split()
    }
    drinks_collection.update_one(
        {'_id': ObjectId(drink_id)},
        {'$set': updated_drink}
    )
    return redirect(url_for('drinks_show', drink_id=drink_id))

@app.route('/drinks/<drink_id>/delete', methods=['POST'])
def drinks_delete(drink_id):
    """Delete one drink."""
    drinks_collection.delete_one({'_id': ObjectId(drink_id)})
    return redirect(url_for('homepage'))

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=os.environ.get('PORT', 5000))
