"""
WhatsAtende Simple Test - Minimal Version
"""

from flask import Flask, jsonify
import datetime

app = Flask(__name__)

@app.route('/')
def index():
    return '''
    <!DOCTYPE html>
    <html>
    <head>
        <title>WhatsAtende Simple Test</title>
        <style>
            body { font-family: Arial, sans-serif; padding: 20px; background: #f0f0f0; }
            .container { max-width: 400px; margin: 0 auto; background: white; padding: 20px; border-radius: 10px; text-align: center; }
            .success { color: green; background: #e6ffe6; padding: 10px; border-radius: 5px; margin: 10px 0; }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>🤖 WhatsAtende Test</h1>
            <div class="success">✅ Vercel funcionando!</div>
            <p>Timestamp: ''' + datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + '''</p>
            <button onclick="testBot()">Testar Bot</button>
            <div id="result"></div>
        </div>
        
        <script>
            function testBot() {
                fetch('/api/test')
                .then(response => response.json())
                .then(data => {
                    document.getElementById('result').innerHTML = 
                        '<div style="margin-top: 20px; padding: 10px; background: #f8f8f8; border-radius: 5px;">' +
                        JSON.stringify(data, null, 2) +
                        '</div>';
                })
                .catch(error => {
                    document.getElementById('result').innerHTML = 
                        '<div style="margin-top: 20px; padding: 10px; background: #ffe6e6; color: red; border-radius: 5px;">' +
                        'Erro: ' + error +
                        '</div>';
                });
            }
        </script>
    </body>
    </html>
    '''

@app.route('/api/test')
def test():
    """Endpoint de teste simples"""
    return jsonify({
        'status': 'success',
        'message': 'API funcionando!',
        'timestamp': datetime.datetime.now().isoformat(),
        'test_response': 'Olá! Teste básico funcionando!'
    })

@app.route('/api/chat', methods=['POST'])  
def chat():
    """Chat endpoint - versão mínima"""
    return jsonify({
        'response': 'Olá! Esta é uma resposta de teste. O sistema está funcionando!',
        'status': 'test_mode'
    })

# Vercel entry point
app = app