"""
WhatsAtende Web Interface - Vercel Version
Versão Python adaptada para deploy no Vercel
"""

from flask import Flask, render_template_string, request, jsonify
import json
import os
import sys

# Import do bot (agora na mesma pasta)
from whatsatende_python import WhatsAtendeBot

app = Flask(__name__)
bot = WhatsAtendeBot()

# Template HTML adaptado para Vercel
HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>WhatsAtende Demo - Simulador</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }
        
        body {
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            height: 100vh;
            display: flex;
            align-items: center;
            justify-content: center;
        }
        
        .container {
            background: white;
            border-radius: 20px;
            box-shadow: 0 20px 40px rgba(0,0,0,0.1);
            width: 90%;
            max-width: 800px;
            height: 90vh;
            display: flex;
            flex-direction: column;
            overflow: hidden;
        }
        
        .header {
            background: #25D366;
            color: white;
            padding: 20px;
            text-align: center;
        }
        
        .header h1 {
            margin-bottom: 10px;
        }
        
        .chat-container {
            flex: 1;
            display: flex;
            flex-direction: column;
            padding: 20px;
            overflow: hidden;
        }
        
        .messages {
            flex: 1;
            overflow-y: auto;
            margin-bottom: 20px;
            padding: 10px;
            border: 1px solid #e0e0e0;
            border-radius: 10px;
            background: #f9f9f9;
        }
        
        .message {
            margin-bottom: 15px;
            padding: 12px 16px;
            border-radius: 18px;
            max-width: 80%;
            word-wrap: break-word;
            line-height: 1.4;
        }
        
        .user-message {
            background: #DCF8C6;
            margin-left: auto;
            text-align: right;
        }
        
        .bot-message {
            background: white;
            border: 1px solid #e0e0e0;
        }
        
        .input-container {
            display: flex;
            gap: 10px;
        }
        
        .message-input {
            flex: 1;
            padding: 12px 16px;
            border: 1px solid #ddd;
            border-radius: 25px;
            outline: none;
            font-size: 16px;
        }
        
        .message-input:focus {
            border-color: #25D366;
        }
        
        .send-button {
            background: #25D366;
            color: white;
            padding: 12px 24px;
            border: none;
            border-radius: 25px;
            cursor: pointer;
            font-size: 16px;
            font-weight: bold;
        }
        
        .send-button:hover {
            background: #1db954;
        }
        
        .status {
            text-align: center;
            padding: 10px;
            font-size: 14px;
            color: #666;
        }
        
        .demo-info {
            background: #e3f2fd;
            padding: 15px;
            margin-bottom: 20px;
            border-radius: 10px;
            border-left: 4px solid #2196f3;
        }
        
        .quick-buttons {
            display: flex;
            gap: 10px;
            margin-bottom: 10px;
            flex-wrap: wrap;
        }
        
        .quick-button {
            padding: 8px 15px;
            background: #f0f0f0;
            border: 1px solid #ddd;
            border-radius: 20px;
            cursor: pointer;
            font-size: 14px;
            transition: all 0.3s;
        }
        
        .quick-button:hover {
            background: #25D366;
            color: white;
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>🤖 WhatsAtende Demo</h1>
            <p>Simulador de Demonstração - Versão Vercel</p>
            <p>📱 Número: (48) 99931-4665 | 📧 expertdigitalnovo@gmail.com</p>
        </div>
        
        <div class="chat-container">
            <div class="demo-info">
                <strong>🎯 Como usar:</strong><br>
                • Digite uma mensagem para iniciar<br>
                • Siga o fluxo de demonstração<br>
                • Use os botões rápidos ou digite as opções
            </div>
            
            <div class="quick-buttons">
                <button class="quick-button" onclick="sendMessage('Olá')">Iniciar Conversa</button>
            </div>
            
            <div class="messages" id="messages"></div>
            
            <div class="input-container">
                <input type="text" id="messageInput" class="message-input" placeholder="Digite sua mensagem..." onkeypress="handleKeyPress(event)">
                <button class="send-button" onclick="sendMessage()">Enviar</button>
            </div>
        </div>
        
        <div class="status" id="status">
            Pronto para conversar! 💬
        </div>
    </div>

    <script>
        const messagesContainer = document.getElementById('messages');
        const messageInput = document.getElementById('messageInput');
        const status = document.getElementById('status');
        
        // Usuário fictício para demonstração
        const userId = '5511999999999';
        
        function addMessage(text, isUser = false) {
            const messageDiv = document.createElement('div');
            messageDiv.className = `message ${isUser ? 'user-message' : 'bot-message'}`;
            messageDiv.innerHTML = text.replace(/\\n/g, '<br>').replace(/\\*\\*(.*?)\\*\\*/g, '<strong>$1</strong>');
            messagesContainer.appendChild(messageDiv);
            messagesContainer.scrollTop = messagesContainer.scrollHeight;
        }
        
        function sendMessage(text = null) {
            const message = text || messageInput.value.trim();
            if (!message) return;
            
            addMessage(message, true);
            if (!text) messageInput.value = '';
            
            status.textContent = 'Processando...';
            
            fetch('/api/chat', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({
                    user_id: userId,
                    message: message
                })
            })
            .then(response => response.json())
            .then(data => {
                addMessage(data.response);
                status.textContent = 'Pronto para conversar! 💬';
            })
            .catch(error => {
                addMessage('❌ Erro de conexão. Tente novamente.');
                status.textContent = 'Erro de conexão';
                console.error('Erro:', error);
            });
        }
        
        function handleKeyPress(event) {
            if (event.key === 'Enter') {
                sendMessage();
            }
        }
        
        // Foco automático no input
        messageInput.focus();
        
        // Mensagem de boas-vindas
        setTimeout(() => {
            addMessage('Bem-vindo ao WhatsAtende Demo! 🎉<br>Digite qualquer mensagem para começar a demonstração.');
        }, 500);
    </script>
</body>
</html>
"""

@app.route('/')
def index():
    return render_template_string(HTML_TEMPLATE)

@app.route('/api/chat', methods=['POST'])
def chat():
    data = request.json
    user_id = data.get('user_id', 'demo_user')
    message = data.get('message', '')
    
    response = bot.process_message(user_id, message)
    
    return jsonify({
        'response': response,
        'user_id': user_id
    })

# Para compatibilidade com Vercel
app = app