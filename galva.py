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

@app.route('/uzruna',methods=['GET', 'POST'])
def uzruna():
   if request.method == 'POST':
      vards1 = request.form['vards']
      uzvards1 = request.form['uzvards']
      return render_template("sveiciens.html",vards=vards1,uzvards=uzvards1)  
   else:
      vards1 = request.args.get('vards')
      uzvards1 = request.args.get('uzvards')
      return vards1, uzvards1
  
  

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
