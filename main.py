from flask import Flask, render_template, request, redirect, url_for
import random
app = Flask(__name__)

import os
p_antrean = "antrean"

def generate_random_number():
    return "".join([str(random.randint(0, 9)) for i in range (4)])

def buat_antre_baru():
    daftar = os.listdir(p_antrean)
    antre_terakhir = 0
    if len(daftar) > 0:
        antre_terakhir = int(daftar[-1])
    antre_baru = str(antre_terakhir + 1).zfill(4)
    password = generate_random_number()
    with open(p_antrean + "//" + antre_baru, "w+") as buka:
        buka.write(password)
    return (antre_baru, password)

def reset():
    for antrean in os.listdir(p_antrean):
        os.remove(p_antrean + "//" + antrean)
    with open("noantre", "w") as tulis:
        tulis.write("0000")

def kredensial_sesuai(id_antre, password):
    try:
        with open(p_antrean + "//" + id_antre) as user:
            for ps in user:
                if password == ps:
                    return True
    except FileNotFoundError as e:
        pass
    return False

def inkremen_no_kini():
    angka = 0
    with open("noantre", "r") as buka:
        for i in buka:
            angka = int(i)
            break
    with open("noantre", "w") as tulis:
        tulis.write(str(angka + 1).zfill(4))

def antrean_kini():
    with open("noantre", "r") as buka:
        for i in buka:
            return i

@app.route("/request")
def request_antrean(berhasil = True):
    no_antre, password = buat_antre_baru()
    return render_template('berhasil-request.html',
        no_antre = no_antre, password = password)

@app.route("/")
def home():
    return render_template('home.html', noantre = antrean_kini())

@app.route("/inkremenkan")
def inkremen_angka_web():
    inkremen_no_kini()
    return redirect(url_for("home"))

@app.route("/reset")
def reset_angka_web():
    reset()
    return redirect(url_for("home"))
    
if __name__ == "__main__":
    app.run(debug=True)