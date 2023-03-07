# Musu Flask serveris
from flask import Flask
from flask import request
from flask import url_for
from flask import render_template
from flask import jsonify

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
 
@app.route('/dati')
def dati():
  aa = {'name':"bumba",'vecums':"16"}
  return jsonify(aa)   

@app.route('/tests')
def health():
  return render_template("tests.html")

if __name__ == '__main__':
  app.run(debug=True,port=5000) # ,host='0.0.0.0' host='0.0.0.0' - datora IP adrese
