"""
WhatsAtende Web Interface
Versão Python com interface web simples usando Flask
Sem necessidade de Node.js
"""

from flask import Flask, render_template_string, request, jsonify
import json
import threading
import webbrowser
import time
from whatsatende_python import WhatsAtendeBot

app = Flask(__name__)
bot = WhatsAtendeBot()

# Template HTML simples
HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>botK - Simulador de Demonstração</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }
        
        body {
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 50%, #f093fb 100%);
            background-size: 400% 400%;
            animation: gradientShift 8s ease infinite;
            height: 100vh;
            display: flex;
            align-items: center;
            justify-content: center;
            overflow: hidden;
        }
        
        @keyframes gradientShift {
            0%, 100% { background-position: 0% 50%; }
            50% { background-position: 100% 50%; }
        }
        
        @keyframes slideInUp {
            from {
                opacity: 0;
                transform: translateY(50px);
            }
            to {
                opacity: 1;
                transform: translateY(0);
            }
        }
        
        @keyframes pulse {
            0%, 100% { transform: scale(1); }
            50% { transform: scale(1.05); }
        }
        
        .pulse-animation {
            animation: pulse 2s ease-in-out infinite;
        }
        
        .container {
            background: rgba(255, 255, 255, 0.95);
            backdrop-filter: blur(20px);
            border-radius: 25px;
            border: 1px solid rgba(255, 255, 255, 0.3);
            box-shadow: 0 25px 50px rgba(0,0,0,0.2), 0 0 0 1px rgba(255,255,255,0.1);
            width: 95%;
            max-width: 900px;
            height: 95vh;
            display: flex;
            flex-direction: column;
            overflow: hidden;
            animation: slideInUp 0.8s ease-out;
        }
        
        .header {
            background: linear-gradient(135deg, #25D366 0%, #128C7E 50%, #075E54 100%);
            color: white;
            padding: 25px;
            text-align: center;
            position: relative;
            overflow: hidden;
        }
        
        .header::before {
            content: '';
            position: absolute;
            top: 0;
            left: -100%;
            width: 100%;
            height: 100%;
            background: linear-gradient(90deg, transparent, rgba(255,255,255,0.2), transparent);
            animation: shimmer 2s infinite;
        }
        
        .header h1 {
            margin-bottom: 10px;
            font-size: 2.2em;
            text-shadow: 0 2px 4px rgba(0,0,0,0.3);
            position: relative;
            z-index: 1;
        }
        
        .header p {
            position: relative;
            z-index: 1;
            opacity: 0.9;
            font-size: 1.1em;
        }
        
        @keyframes shimmer {
            0% { left: -100%; }
            100% { left: 100%; }
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
            padding: 15px;
            border: none;
            border-radius: 20px;
            background: linear-gradient(145deg, #f0f2f5 0%, #e4e6ea 100%);
            box-shadow: inset 0 2px 10px rgba(0,0,0,0.1);
            scroll-behavior: smooth;
        }
        
        .message {
            margin-bottom: 15px;
            padding: 12px 18px;
            border-radius: 20px;
            max-width: 85%;
            word-wrap: break-word;
            opacity: 0;
            animation: messageSlide 0.5s ease-out forwards;
            box-shadow: 0 2px 8px rgba(0,0,0,0.1);
        }
        
        .user-message {
            background: linear-gradient(135deg, #DCF8C6 0%, #B8E6B8 100%);
            margin-left: auto;
            text-align: right;
            border-bottom-right-radius: 5px;
            transform: translateX(20px);
        }
        
        .bot-message {
            background: linear-gradient(135deg, #ffffff 0%, #f8f9fa 100%);
            margin-right: auto;
            border-bottom-left-radius: 5px;
            border: 1px solid rgba(0,0,0,0.05);
            transform: translateX(-20px);
        }
        
        @keyframes messageSlide {
            to {
                opacity: 1;
                transform: translateX(0);
            }
        }
        
        .input-container {
            display: flex;
            gap: 10px;
        }
        
        .message-input {
            flex: 1;
            padding: 18px 25px;
            border: 2px solid #e0e0e0;
            border-radius: 30px;
            font-size: 16px;
            outline: none;
            background: rgba(255, 255, 255, 0.9);
            backdrop-filter: blur(10px);
            transition: all 0.3s ease;
            box-shadow: 0 2px 10px rgba(0,0,0,0.1);
        }
        
        .message-input:focus {
            border-color: #25D366;
            box-shadow: 0 0 0 3px rgba(37, 211, 102, 0.2);
            transform: scale(1.02);
        }
        
        .send-button {
            padding: 18px 30px;
            background: linear-gradient(135deg, #25D366 0%, #128C7E 100%);
            color: white;
            border: none;
            border-radius: 30px;
            cursor: pointer;
            font-size: 16px;
            font-weight: bold;
            transition: all 0.3s ease;
            box-shadow: 0 4px 15px rgba(37, 211, 102, 0.3);
        }
        
        .send-button:hover {
            background: linear-gradient(135deg, #1db954 0%, #0f7a6b 100%);
            transform: translateY(-2px);
            box-shadow: 0 6px 20px rgba(37, 211, 102, 0.4);
        }
        
        .send-button:active {
            transform: translateY(0);
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
            <h1>🤖 botK</h1>
            <p>Simulador de Demonstração</p>
            <p>📱 Número: 48000000000 | 📧 seuemail@seuemail.com</p>
        </div>
        
        <div class="chat-container">
            <div class="demo-info">
                <strong>🎯 Como usar:</strong><br>
                Olá 👋 Pra te atender melhor, me diga o que você precisa agora!
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
            
            fetch('/chat', {
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
            addMessage('🚀 **BEM-VINDO À REVOLUÇÃO!**<br>Descubra como o botK vai <strong>TRANSFORMAR</strong> seu negócio!<br><br>💎 Esta demo vai <strong>MUDAR</strong> sua visão sobre automação!<br>Digite qualquer mensagem para começar!');
        }, 500);
    </script>
</body>
</html>
"""

@app.route('/')
def index():
    return render_template_string(HTML_TEMPLATE)

@app.route('/chat', methods=['POST'])
def chat():
    data = request.json
    user_id = data.get('user_id', 'demo_user')
    message = data.get('message', '')
    
    response = bot.process_message(user_id, message)
    
    return jsonify({
        'response': response,
        'user_id': user_id
    })

def open_browser():
    """Abre o navegador após um pequeno delay"""
    time.sleep(1.5)
    webbrowser.open('http://localhost:5000')

def main():
    print("=" * 60)
    print("🌐 WHATSATENDE WEB DEMO - VERSÃO DEMONSTRATIVA")
    print("=" * 60)
    print("🚀 Iniciando servidor web...")
    print("📱 Número configurado: 48000000000")
    print("📧 Email: seuemail@seuemail.com")
    print("🌐 URL: http://localhost:5000")
    print("=" * 60)
    
    # Inicia thread para abrir navegador
    threading.Thread(target=open_browser, daemon=True).start()
    
    # Inicia servidor Flask
    app.run(host='localhost', port=5000, debug=False)

if __name__ == "__main__":
    main()