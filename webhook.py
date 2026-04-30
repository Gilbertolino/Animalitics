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
def receber_dados():
    # 1. Pegamos os dados enviados (formato JSON)
    dados = request.get_json()
    
    # 2. Mostramos no console o que chegou (para debug)
    print("--- Nova Notificação Recebida ---")
    print(dados)
    
    # 3. Aqui você processa a informação
    # Exemplo: se chegar um "status: pago", você libera um acesso.
    
    # 4. Respondemos ao serviço que enviou (Status 200 = Sucesso)
    # É importante responder rápido para o serviço não achar que deu erro.
    return jsonify({"mensagem": "Recebido com sucesso!","Dados recebidos": dados}), 200



if __name__ == "__main__":
    app.run(port=5000)