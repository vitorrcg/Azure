from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return 'Olá, Azure! 🚀'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
