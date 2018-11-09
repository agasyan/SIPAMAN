from flask import Flask, render_template, request, redirect, url_for
app = Flask(__name__)

import os
p_antrean = "antrean"
p_user = "user"

def buat_antre_baru(pengaju):
    daftar = os.listdir(p_antrean)
    antre_terakhir = 0
    if len(daftar) > 0:
        antre_terakhir = int(daftar[-1])
    antre_baru = str(antre_terakhir + 1).zfill(4)
    with open(p_antrean + "//" + antre_baru, "w+") as buka:
        buka.write(pengaju)
    return antre_baru

def kredensial_sesuai(username, password):
    try:
        with open(p_user + "//" + username) as user:
            for ps in user:
                if password == ps.split()[2]:
                    return True
    except FileNotFoundError as e:
        pass
    return False

def inkremen_no_kini():
    angka = 0
    with open("noantri", "r") as buka:
        for i in buka:
            angka = int(i)
            break
    with open("noantri", "w") as tulis:
        tulis.write(str(angka + 1).zfill(4))

def antrean_kini():
    with open("noantri", "r") as buka:
        for i in buka:
            return i

def antrean_kini():
    with open("noantri", "r") as buka:
        for i in buka:
            return i

@app.route("/kirim-request", methods=['POST'])
def kirim_request():
    username = request.form['username']
    password = request.form['password']
    if kredensial_sesuai(username, password):
        nomor_baru = buat_antre_baru(username)
        return render_template('berhasil-request.html', no_antrenya = nomor_baru)
    else:
        return redirect((url_for('request_antrean')), code=302)
        

@app.route("/request")
def request_antrean(berhasil = True):
    return render_template('request.html', berhasil = berhasil)

@app.route("/")
def home():
    return render_template('home.html', noantre=antrean_kini())

@app.route("/inkremenkan")
def inkremen_angka_web():
    inkremen_no_kini()
    return render_template('home.html', noantre=antrean_kini())

if __name__ == "__main__":
    app.run(debug=True)