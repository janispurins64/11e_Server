# Musu Flask serveris
from flask import Flask
from flask import request
from flask import url_for
from flask import render_template

app = Flask(__name__)

@app.route('/',methods=['GET'])
def root():
    return render_template("tests.html")

@app.route('/uzruna')
def uzruna():
      
      
  return render_template("sveiciens.html",skaits="otrais")  
  

@app.route('/vards')
def katevisauc():
  return render_template("katevisauc.html")  
  

@app.route('/tests')
def health():
  return render_template("tests.html")

if __name__ == '__main__':
  app.run(debug=True,port=5000) # ,host='10.1.15.44' host='0.0.0.0' - datora IP adrese
