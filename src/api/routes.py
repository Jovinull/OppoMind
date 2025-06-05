from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

@app.route('/mensagem', methods=['POST'])
def receber_mensagem():
    # Exemplo de corpo esperado: {"texto": "oi"}
    dados = request.json
    texto = dados.get("texto")

    # Chama o Rasa (já deve estar rodando em background)
    resposta = requests.post("http://localhost:5005/webhooks/rest/webhook", json={
        "sender": "usuario",
        "message": texto
    })

    return jsonify(resposta.json())
