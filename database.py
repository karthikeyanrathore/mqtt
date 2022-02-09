#!/usr/bin/env python3
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/shack.db'
db = SQLAlchemy(app)


# one - many relation
# one category - multiple post

class Post(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  title = db.Column(db.String(20))
  body = db.Column(db.String(50))

  category_id = db.Column(db.Integer, db.ForeignKey('category.id'), nullable=False)
  category = db.relationship('Category', backref=db.backref('posts', lazy=True))

  def __repr__(self):
    return "Post id: %d and title: %s , body: %s" % (self.id , self.title, self.body)

class Category(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(20))
  
  def __repr__(self):
    return "Comment id: %d and name: %s" % (self.id , self.name)



