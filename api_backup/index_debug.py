"""
WhatsAtende API Test - Vercel Debug
Versão de teste para identificar problemas
"""

from flask import Flask, jsonify, request, render_template_string
import traceback

app = Flask(__name__)

# Template HTML básico para teste
HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>WhatsAtende Demo - Test</title>
    <style>
        body { font-family: Arial, sans-serif; padding: 20px; background: #f0f0f0; }
        .container { max-width: 600px; margin: 0 auto; background: white; padding: 20px; border-radius: 10px; }
        .error { color: red; background: #ffe6e6; padding: 10px; border-radius: 5px; margin: 10px 0; }
        .success { color: green; background: #e6ffe6; padding: 10px; border-radius: 5px; margin: 10px 0; }
        button { background: #25D366; color: white; border: none; padding: 10px 20px; border-radius: 5px; cursor: pointer; }
        input { width: 100%; padding: 10px; margin: 10px 0; border: 1px solid #ddd; border-radius: 5px; }
    </style>
</head>
<body>
    <div class="container">
        <h1>🤖 WhatsAtende Demo - Debug Mode</h1>
        <div class="success">✅ Sistema carregado com sucesso!</div>
        
        <h3>📱 Teste do Bot:</h3>
        <input type="text" id="messageInput" placeholder="Digite sua mensagem..." onkeypress="handleKeyPress(event)">
        <button onclick="sendMessage()">Enviar</button>
        
        <div id="response" style="margin-top: 20px; padding: 10px; background: #f8f8f8; border-radius: 5px;"></div>
    </div>

    <script>
        function sendMessage() {
            const input = document.getElementById('messageInput');
            const responseDiv = document.getElementById('response');
            const message = input.value.trim();
            
            if (!message) return;
            
            responseDiv.innerHTML = '<div style="color: blue;">Processando...</div>';
            
            fetch('/api/chat', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ user_id: 'test_user', message: message })
            })
            .then(response => response.json())
            .then(data => {
                if (data.error) {
                    responseDiv.innerHTML = `<div class="error">❌ Erro: ${data.error}</div>`;
                } else {
                    responseDiv.innerHTML = `<div class="success">🤖 Bot: ${data.response}</div>`;
                }
                input.value = '';
            })
            .catch(error => {
                responseDiv.innerHTML = `<div class="error">❌ Erro de conexão: ${error}</div>`;
            });
        }
        
        function handleKeyPress(event) {
            if (event.key === 'Enter') {
                sendMessage();
            }
        }
    </script>
</body>
</html>
"""

@app.route('/')
def index():
    return render_template_string(HTML_TEMPLATE)

@app.route('/api/chat', methods=['POST'])
def chat():
    try:
        # Teste de importação
        try:
            from whatsatende_python import WhatsAtendeBot
            bot = WhatsAtendeBot()
        except ImportError as e:
            return jsonify({
                'error': f'Erro de importação: {str(e)}',
                'traceback': traceback.format_exc()
            }), 500
        except Exception as e:
            return jsonify({
                'error': f'Erro ao criar bot: {str(e)}',
                'traceback': traceback.format_exc()
            }), 500
        
        # Processar mensagem
        try:
            data = request.json
            user_id = data.get('user_id', 'demo_user')
            message = data.get('message', '')
            
            response = bot.process_message(user_id, message)
            
            return jsonify({
                'response': response,
                'user_id': user_id,
                'status': 'success'
            })
            
        except Exception as e:
            return jsonify({
                'error': f'Erro ao processar mensagem: {str(e)}',
                'traceback': traceback.format_exc()
            }), 500
            
    except Exception as e:
        return jsonify({
            'error': f'Erro geral: {str(e)}',
            'traceback': traceback.format_exc()
        }), 500

@app.route('/api/health')
def health():
    """Endpoint de health check"""
    try:
        from whatsatende_python import WhatsAtendeBot
        bot = WhatsAtendeBot()
        return jsonify({
            'status': 'healthy',
            'bot_loaded': True,
            'message': 'WhatsAtende API funcionando!'
        })
    except Exception as e:
        return jsonify({
            'status': 'error',
            'bot_loaded': False,
            'error': str(e),
            'traceback': traceback.format_exc()
        }), 500

# Para compatibilidade com Vercel
if __name__ == '__main__':
    app.run(debug=True)

# Vercel entry point
app = app