# Musu Flask serveris
from flask import Flask
from flask import request
from flask import url_for
from flask import render_template
from flask import json
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

#----------------------------------------------------  
# Lapa ar izkrītošo sarakstu.
# Šo izsauc ar http://127.0.0.1:5000/saraksts
@app.route('/virtuve')
def virtuve():
  return render_template("virtuve.html")
# Rezervējam virtuves piederumus
# Šo izsauc ar http://127.0.0.1:5000/rezerveshana
@app.route('/rezerveshana')
def rezerveshana():
  piederumi = request.args.get('riiki')
  skaits = request.args.get('skaits')
  print("Izvēlētais piederums: ",piederumi)
  print("Skaits: ",skaits)
#------
# Saglabāsim saņemtos datus teksta failā, bet var arī
# datu bāzē. Izmantojam json formātu.
  dati = {}
  dati["v_piederums"] = piederumi
  dati["skaits"] = skaits
  with open("static/trauki.txt","a",encoding="UTF-8") as f1:
    f1.write(json.dumps(dati))
  return render_template("virtuve.html")

# Tukšas formas izsaukums
# Šo izsauc ar http://127.0.0.1:5000/personas
@app.route('/personas')
def personas():

  return render_template("personas.html")


#----------------------------------------------------      

@app.route('/tests')
def health():
  return render_template("tests.html")

if __name__ == '__main__':
  app.run(debug=True,port=5000) # ,host='0.0.0.0' host='0.0.0.0' - datora IP adrese
