# Import Statements
from flask import Flask, render_template
from blueprints.operators import operators_blueprint
from blueprints.loops import loops_blueprint

# Declare flask app instance
app = Flask(__name__)

# Home Page Route
@app.route('/')
def home():
    return render_template('home.html')

# Blueprints (aka Controllers!)
app.register_blueprint(operators_blueprint)
app.register_blueprint(loops_blueprint)

# Listen on port 5000
if __name__ == '__main__':
    app.run()
