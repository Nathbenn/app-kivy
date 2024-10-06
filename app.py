from flask import Flask, render_template, jsonify

app = Flask(__name__)

@app.route('/')
@app.route('/beranda')
def home():
    return render_template('index.html')

@app.route('/menu')
def menu():
    return render_template('menu.html')

@app.route('/tentang')
def about():
    return render_template('tentang.html')

@app.route('/kontak')
def contact():
    return render_template('kontak.html')

@app.route('/get_promo')
def get_promo():
    return jsonify({"message": "Selamat! Anda mendapatkan diskon 20% untuk kunjungan berikutnya!"})

if __name__ == '__main__':
    app.run(debug=True)