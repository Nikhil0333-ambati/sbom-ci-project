from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "SBOM CI Project Running!"

if __name__ == "__main__":
    app.run(debug=True)
