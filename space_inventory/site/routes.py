from flask import Blueprint, render_template

"""
Note that in the code below,
some argumenets are specifie when creating the Blueprint object
The firs argument, "site", is the Blueprints name, 
which is used by Flask's routing mechanism

The second argument, __name__, is the BLueprint's import name
which flask uses to locate the Blueprint's resources
"""

site = Blueprint('site', __name__, template_folder='site_templates')

@site.route('/')
def home():
    return render_template('index.html')

@site.route('/profile')
def profile():
    return render_template('profile.html')

