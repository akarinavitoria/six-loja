from Flask import Flask, jsonify
from Flask_SQLAlchemy import SQLAlchemy
from Flask_Cors import CORS

app = Flask(__name__)
CORS(app)

# Configuração do SQLite
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Rota inicial de teste
@app.route('/')
def home():
    return jsonify({"message": "Backend está rodando!"})

if __name__ == '__main__':
    app.run(debug=True)
