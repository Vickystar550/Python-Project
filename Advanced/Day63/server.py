from flask import Flask, render_template
from flask_bootstrap import Bootstrap5
from flask_wtf import FlaskForm


app = Flask(__name__)
bootstrap = Bootstrap5(app)

