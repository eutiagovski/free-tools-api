from flask import Flask
from tools.movie_recomendation_system.route import movie_recomendation

app = Flask(__name__)

app.register_blueprint(movie_recomendation)

@app.route("/")
def home():
    return "Hello World!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)