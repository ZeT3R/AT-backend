from flask import Flask, redirect, url_for, request, send_from_directory, render_template, url_for
from flask_mysqldb import MySQL
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from sqlalchemy.sql import text
from sqlalchemy import func
import app_project.json_post.load_to_json as form_json
from flask_cors import cross_origin

app = Flask(__name__)

# app.config['MYSQL_HOST'] = '188.120.234.77'
# app.config['MYSQL_USER'] = 'sammy'
# app.config['MYSQL_PASSWORD'] = '1xtv34bs'
# app.config['MYSQL_DB'] = 'efring'
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://sammy:1xtv34bs@188.120.234.77:3306/efring"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
mysql = MySQL(app)
db = SQLAlchemy(app)

migrate = Migrate(app, db)

import app_project.views