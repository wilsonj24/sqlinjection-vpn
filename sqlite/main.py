from flask import Flask
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.config['SQLAlCHEMY_DATABASE_URI'] = 'sqlite:///mnt/Users/jordanwilson/Public/curricularEthics/privacy/sqlite/data.db'
