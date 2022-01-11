import os
from flask from Flask
app = Flask(_name_)

@app.route("/")
def main():
  return "welcome!"

@app.route("/how are you")
def hello():
  return 'im good, how about u'
if _name_ == "_main_":
  app.run()
