# -*- coding: utf-8 -*-
"""
Created on Thu Apr 30 11:16:14 2026

@author: gilbe
"""
from flask import Flask, request, jsonify

app = Flask(__name__)

# Definimos a rota que receberá os dados. 
# O método deve ser 'POST', pois o serviço externo vai "postar" algo para você.
@app.route('/meu-webhook', methods=['POST'])

def meu_webhook():
    # Captura os dados enviados no corpo da requisição
    dados_recebidos = request.get_json()

    # Retorna a mensagem de sucesso junto com os dados que chegaram
    return jsonify({
        "mensagem": "Recebido com sucesso!",
        "dados_enviados": dados_recebidos
    }), 200


if __name__ == "__main__":
    app.run(port=5000)