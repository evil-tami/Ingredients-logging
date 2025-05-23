from App.database import db
from datetime import datetime
from App.models import User
from .recipe import Recipe

class Rating(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
  recipe_id = db.Column(db.Integer, db.ForeignKey('recipe.id'), nullable=False)
  score = db.Column(db.Integer, nullable=False)

  def __init__(self, user_id, recipe_id, score):
    self.user_id = user_id
    self.recipe_id = recipe_id
    self.score = score
    
  def toJSON(self):
    return{
        'id': self.id,
        'recipe_id': self.recipe_id,
        'score': self.score,
        'user_id': self.user_id
    }