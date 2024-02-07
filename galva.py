# Musu Flask serveris
from flask import Flask, g
from flask import request
from flask import url_for
from flask import render_template
from flask import json
from flask import jsonify
import sqlite3          # importējam SQLite3

app = Flask(__name__)
'''
  Šeit ir sākotnēji pildāmā daļa. Varam izmantot datu bāzes izveidei.
  Šī daļa ir tikai paraugam, jo datu bāzi izveidoju ar SQLite Brovser un failu
  iekopēju pamatmapē << virtuve.db >>
  Kods:
'''
# Izveidojam datubāzi ar vienu tabulu vai vairākām
# def create_table():
#    conn = sqlite3.connect('tasks.db')
#    cursor = conn.cursor()
#    cursor.execute('''
#        CREATE TABLE IF NOT EXISTS "Pasutijums" (
#	              "ID_Pasutijums"	INTEGER UNIQUE,
#	              "vards"	TEXT,
#	              "uzvards"	TEXT,
#	              "kontakti"	TEXT,
#	              "tips"	TEXT,
#	              "skaits"	INTEGER,
#	              "datums1"	TEXT,
#	              "datums2"	TEXT,
#	               PRIMARY KEY("ID_Pasutijums" AUTOINCREMENT)
#        )
#    ''')
#    conn.commit()
#    conn.close()

app.config['DATABASE'] = 'virtuve.db'  # Šeit norādiet savu datu bāzes nosaukumu
app.config['SECRET_KEY'] = 'your_secret_key' # Šo frāzi izmanto šifrēšanai, jābūt pietiekami sarežģītai
                                            # citi nedrīkst zināt

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(app.config['DATABASE'])
    return db

def init_db():
    with app.app_context():
        db = get_db()

# Šī ir Flask dekorācija, kas nosaka funkciju, kas tiks izpildīta pēc katras Flask 
# lietojumprogrammas konteksta darbības beigām. Nodrošina, lai datubāze nepaliek vaļā.
@app.teardown_appcontext
def close_db(error):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

# Izveidojiet vai savienojiet ar datu bāzi (ja vēl nav izveidota)
def create_or_connect_database():
    conn = sqlite3.connect('virtuve.db')
    return conn

# Pievienojiet jaunu ierakstu tabulā "Pasutijumi"
def pievienot_pasutijumu(conn, dati):
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO Pasutijums (vards, uzvards, skaits, tips)
        VALUES (?, ?, ?, ?)
    ''', (dati["vards"], dati["uzvards"], dati["skaits"], dati["tips"]))
    conn.commit()

# Izgūst visus ierakstus no tabulas "Pasutijumi"
def izgut_pasutijumus(conn):
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM Pasutijumi')
    pasutijumi = cursor.fetchall()
    print("Datu tabulas dati")
    print(pasutijumi)
    return pasutijumi




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
  personas = []
  with open("static/personas.txt","r",encoding="UTF-8") as f1:
    for rinda in f1:
      personas.append(rinda)
  return jsonify({"personas": personas})
#----------------------------------------------------------------------
# Paraugs Fetch apstrādei
@app.route('/dts', methods=['POST'])
def receive_data():
    dati1 = request.json  # Saņem datus no POST pieprasījuma no Fetch
    # Veiciet vajadzīgos apstrādes soļus ar datiem
    print(dati1)

# Izveidojiet jaunu ierakstu, izmantojot datus no vārdnīcas
    print("DB daļa")
    conn = create_or_connect_database()
    pievienot_pasutijumu(conn, dati1)



    # Visus pasūtījumus paņamam no bāzes
    visi_pasutijumi = izgut_pasutijumus(conn)
    response_data = {'message': 'Dati saņemti veiksmīgi'}
    return jsonify(response_data),200 # Atgriež vērtību Fetch izsaukumam
#----------------------------------------------------------------------
@app.route('/data')
def dataa():
  return render_template("data.html")


# Tukšas formas izsaukums
# Šo izsauc ar http://127.0.0.1:5000/visi
@app.route('/visi')
def visi():
  return render_template("personas.html")

#----------------------------------------------------      

@app.route('/tests')
def health():
  return render_template("tests.html")

if __name__ == '__main__':
  init_db() #
  app.run(debug=True,port=5000) # ,host='0.0.0.0' host='0.0.0.0' - datora IP adrese
