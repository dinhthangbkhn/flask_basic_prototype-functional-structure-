from flask import Blueprint, render_template

mod = Blueprint('about',__name__, url_prefix='/about')

@mod.route('/')
def about():
    return render_template('about/about.html')