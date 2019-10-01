from flask import Blueprint, redirect, render_template, request
from datetime import datetime
from models.index import db
from bson.objectid import ObjectId

operators_blueprint = Blueprint('operators', __name__, url_prefix='/operators')

@operators_blueprint.route('/', methods=('GET', 'POST'))
def index():
    if request.method == 'GET':
        operators = list(db.operators.find())
        return render_template('operators/index.html', operators=operators)
    elif request.method == 'POST':
        # langs = [x.strip() for x in request.form['languages'].split(',')]
        # # print('You typed the languages:', langs)
        # if request.form['birthday']:
        #     date = datetime.strptime(request.form['birthday'], '%Y-%m-%d')
        #     # print(date)
        # else:
        #     date = None


        db.operators.insert_one({
          'name': request.form['name'],
          'symbol': request.form['symbol'],
          'description': request.form['description'],
          'example': request.form['example'],
          'usage': request.form['usage']
        })
        return redirect('/operators')

@operators_blueprint.route('/<operator_id>')
def show(operator_id):
  operator = db.operators.find_one({'_id': ObjectId(operator_id)})
  return render_template('operators/show.html', operator = operator)

