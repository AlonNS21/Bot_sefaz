# app.py
from flask import Flask, render_template, request, jsonify
from faq import obter_resposta

app = Flask(__name__)

# Rota principal para renderizar a página HTML
@app.route('/')
def index():
    return render_template('index.html')

# Rota para processar a pergunta e retornar a resposta
@app.route('/get_response', methods=['POST'])
def get_response():
    user_message = request.json.get('message').lower()  # Pega a mensagem do usuário e converte para minúsculas
    
    # Obtém a resposta normalizada
    bot_response = obter_resposta(user_message)

    return jsonify({"response": bot_response})

if __name__ == '__main__':
    app.run(debug=True)



