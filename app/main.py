
from flask import Flask, request, url_for, render_template, redirect, session, jsonify
import os
import base64

app = Flask(__name__)

@app.route('/')
def index():
	menu = "<div class='menu-bar'>menu</div>"	
	return render_template('public/index.html' ,menus = menu)

@app.route('/login', methods=['POST','GET'])
def login():
	user = None
	Err = "Username atau password salah"
	if request.method == 'POST':
		username = request.form['username']
		password = request.form['password']
		
		data_sementara = {'username':'user', 'password':''}
		if username == data_sementara.get(username) and password == data_sementara.get(password):
			session['user'] = data_sementara.get(username)
			return redirect(url_for('index'))
		else:
			return render_template('public/login.html', error = Err)
	else:
		return jsonify({'ip':request.remote_addr}),200
		
@app.route('/order/<ordername>')
def order(ordername):
	return f"{ordername}"
	
@app.route('/foo', methods=['POST','GET'])
def foo():
	gagal = "Pemesanan tidak berhasil."
	if request.method == 'POST':
		id_pesanan = request.form['id_pesanan']
		enc = base64.b64encode(id_pesanan.encode('utf-8'))
		e = {'order type':enc}
		return redirect(url_for('order', ordername = e))
	else:
		return gagal
@app.route('/test')
def test():
	return "image path here"
app.secret_key = os.urandom(24)
app.run(debug=True)