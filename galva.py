# Musu Flask serveris
from flask import Flask
from flask import request
from flask import url_for
from flask import render_template
#from module import funci


app = Flask(__name__)

@app.route('/',methods=['GET'])
def root():
    aa = float(request.args.get('a',default='0.',type=str))
    bb = float(request.args.get('b',default='0.',type=str))
    cc = float(request.args.get('c',default='0.',type=str))
    
    rez = "Perimetrs=" + funci.tr_per(aa,bb,cc)
    return render_template("sveikaPasaule.html",vards="Trīsstūra parametri",rezultats=rez)

@app.route('/pogasall',methods=['GET'])
def pogasall():
    aa = request.args.get('a',default='0.',type=str)
    aa= "Ievadītā vērtība: " + aa
    
    return render_template("sveikaPasaule.html",vards="Kontroļu pārbaude",rezultats=aa)

@app.route('/pogas')
def pogas():
    return render_template("pogas.html",vards="Podziņas")

@app.route('/tests')
def health():
  return "Serveris darbojas Uh!"

if __name__ == '__main__':
  app.run()
