from flask import Flask, request, jsonify, render_template
from datetime import datetime

app = Flask(__name__)

leituras = []

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/api/ruido", methods=["POST"])
def receber_ruido():
    dados = request.get_json()

    leitura = {
        "operador": dados.get("operador", 1),
        "decibeis": float(dados.get("decibeis", 0)),
        "data_hora": datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    }

    leituras.insert(0, leitura)

    if len(leituras) > 100:
        leituras.pop()

    return jsonify({"status": "ok", "leitura": leitura}), 200

@app.route("/api/ultimas", methods=["GET"])
def ultimas():
    return jsonify(leituras[:30])

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)