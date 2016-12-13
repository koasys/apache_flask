from flask import render_template, Blueprint
from flask import Flask, current_app, session
from flask_login import login_user, login_required


# Define the blueprint
facade_views = Blueprint('facade', __name__, template_folder='templates',
    static_folder='static')
    
    
@facade_views.route('/')
def index():
    return render_template('index.html')  

