from Flask import Flask, jsonify
from FlaskSQLAlchemy import SQLAlchemy
from FlaskCors import CORS

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
