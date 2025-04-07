from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return 'Olá, bem vindo ao meu App Loja na Nuvem! 🚀'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
