from flask import Flask, render_template
import requests
import urllib.parse

app = Flask(__name__)

API_URL = "https://cats-api-sigma.vercel.app/"

@app.route('/')
def index():
    response = requests.get(f"{API_URL}/racas")
    racas = response.json().get("racas", [])
    return render_template('index.html', racas=racas)

@app.route('/racas/<nome_raca>')
def raca_info(nome_raca):
    # Codifica o nome da raça para garantir que caracteres especiais sejam tratados corretamente
    nome_raca_encoded = urllib.parse.quote(nome_raca)
    response = requests.get(f"{API_URL}/racas/{nome_raca_encoded}")
    
    raca = response.json()
    return render_template('raca_info.html', raca=raca)

if __name__ == '__main__':
    app.run(debug=True)

