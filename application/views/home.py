from flask import Blueprint, render_template

mod = Blueprint('home',__name__, url_prefix='/home')

@mod.route('/')
def home():
    return render_template('home/home.html')