from flask import Blueprint, redirect, render_template, request

loops_blueprint = Blueprint('loops', __name__, url_prefix='/loops')

@loops_blueprint.route('/')
def index():
  loops = [
    {'name': 'for-in loop', 'description': 'description text about for-in loops'},
    {'name': 'while loop', 'description': 'description text about while loops'},
    {'name': 'ranges', 'description': 'description text about ranges'},
  ]
  return render_template('loops/index.html', loops=loops)

