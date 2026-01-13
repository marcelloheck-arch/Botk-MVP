"""
WhatsAtende API - Versão com Bot Integrado
Versão otimizada para Vercel com encoding UTF-8
"""

from flask import Flask, jsonify, request
import datetime
import sys
import traceback

app = Flask(__name__)

# Bot inline para evitar problemas de importação
class WhatsAtendeBotSimple:
    def __init__(self):
        self.config = {
            'bot_number': '48999314665',
            'contact_email': 'expertdigitalnovo@gmail.com'
        }

    def log_message(self, message):
        """Sistema de logs"""
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"[{timestamp}] [WHATSATENDE] {message}")

    def is_greeting(self, message):
        """Verifica se é uma saudação comum"""
        greetings = [
            'ola', 'oi', 'hello', 'hi', 'hey', 'hola',
            'bom dia', 'boa tarde', 'boa noite', 'opa', 'eai',
            'teste', 'testando', 'iniciar', 'comecar'
        ]
        msg_lower = message.lower().strip()
        return any(greeting == msg_lower or greeting in msg_lower for greeting in greetings)

    def validate_name(self, name):
        """Valida se pode ser um nome"""
        if len(name.strip()) < 2:
            return False
        if any(char.isdigit() for char in name) and len([c for c in name if c.isdigit()]) > 3:
            return False
        if self.is_greeting(name):
            return False
        return True

    def looks_like_phone(self, message):
        """Verifica se parece ser um telefone"""
        digits = ''.join([c for c in message if c.isdigit()])
        return len(digits) >= 8

    def is_menu_option(self, message):
        """Verifica se é opção de menu"""
        return message.strip() in ['1', '2', '3', '4', '5']

    def process_message(self, user_id, message):
        """Processa mensagem - versão stateless para Vercel"""
        message = message.strip()
        self.log_message(f"Processando: '{message}'")

        # 1. Opções de menu (1-5)
        if self.is_menu_option(message):
            return self.handle_menu_option(message)

        # 2. Telefone (contém 8+ dígitos)
        elif self.looks_like_phone(message):
            return f"""Telefone registrado: {message}

Escolha o que deseja saber:

1 - Principais Funcionalidades
2 - Antes do WhatsAtende  
3 - Depois do WhatsAtende
4 - Falar com o atendente
5 - Finalizar atendimento

Digite o numero da opcao:"""

        # 3. Nome válido
        elif self.validate_name(message):
            name = message.strip().title()
            return f"""Ola {name}! Sou o assistente Virtual WhatsAtende!

E um prazer conhece-lo! Para continuarmos, preciso do seu telefone:

Digite: Seu numero com DDD
Exemplo: 48 99999-9999"""

        # 4. Saudações ou qualquer outra coisa
        else:
            return """Ola! Bem-vindo ao WhatsAtende Demo!

Sou seu assistente virtual e vou demonstrar como podemos revolucionar o atendimento do seu negocio!

Para comecar, digite seu nome:"""

    def handle_menu_option(self, option):
        """Processa opções do menu principal"""
        if option == "1":
            return """PRINCIPAIS FUNCIONALIDADES:

- Atendimento 24h Automatizado
- Consultas Inteligentes 
- Agendamento Automatico
- Envio de Documentos
- Transferencia Inteligente

Continue explorando:
1 - Funcionalidades | 2 - Antes | 3 - Depois | 4 - Atendente | 5 - Finalizar"""
        
        elif option == "2":
            return """PROBLEMAS ANTES DO WHATSATENDE:

- Tempo Desperdicado com repeticoes
- Vendas Perdidas por demora
- Trabalho Sem Parar (24h)
- Custos Abusivos (APIs caras)
- Qualidade Inconsistente

Continue explorando:
1 - Funcionalidades | 2 - Antes | 3 - Depois | 4 - Atendente | 5 - Finalizar"""
        
        elif option == "3":
            return """DEPOIS DO WHATSATENDE:

- Produtividade x10
- Vendas 24 Horas
- Liberdade Total
- Economia Real
- Padronizacao Perfeita

INVESTIMENTO:
- Licenca Unica: R$ 1.289
- Plano Premium: R$ 689 + R$ 89/mes

Continue explorando:
1 - Funcionalidades | 2 - Antes | 3 - Depois | 4 - Atendente | 5 - Finalizar"""
        
        elif option == "4":
            return f"""Transferindo para atendente humano...

Em instantes nossa equipe entrara em contato!

Contatos diretos:
Email: {self.config['contact_email']}
WhatsApp: (48) 99931-4665
Link direto: https://w.app/q8drou

Aguarde nossa chamada!"""
        
        elif option == "5":
            return f"""Obrigado por conhecer o WhatsAtende!

Foi um prazer demonstrar nossa solucao!

Entre em contato:
{self.config['contact_email']}
(48) 99931-4665
https://w.app/q8drou

Vamos implementar o WhatsAtende no seu negocio?

Ate breve!"""
        
        else:
            return """Opcao invalida!

Opcoes disponiveis:
1 - Funcionalidades
2 - Antes do WhatsAtende  
3 - Depois do WhatsAtende
4 - Falar com atendente
5 - Finalizar

Digite um numero de 1 a 5:"""

# Inicializar bot
try:
    bot = WhatsAtendeBotSimple()
    BOT_STATUS = "Bot carregado com sucesso!"
except Exception as e:
    bot = None
    BOT_STATUS = f"Erro ao carregar bot: {str(e)}"

@app.route('/')
def index():
    return f'''
    <!DOCTYPE html>
    <html lang="pt-br">
    <head>
        <meta charset="UTF-8">
        <title>WhatsAtende Demo</title>
        <style>
            body {{ font-family: Arial, sans-serif; padding: 20px; background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); }}
            .container {{ max-width: 600px; margin: 0 auto; background: white; padding: 20px; border-radius: 15px; box-shadow: 0 10px 30px rgba(0,0,0,0.2); }}
            .header {{ text-align: center; background: #25D366; color: white; padding: 15px; border-radius: 10px; margin-bottom: 20px; }}
            .status {{ padding: 10px; border-radius: 5px; margin: 10px 0; text-align: center; }}
            .success {{ color: green; background: #e6ffe6; }}
            .chat-container {{ background: #f8f8f8; border-radius: 10px; padding: 20px; margin: 20px 0; min-height: 200px; }}
            .message {{ margin: 10px 0; padding: 10px; border-radius: 10px; }}
            .user-message {{ background: #dcf8c6; text-align: right; }}
            .bot-message {{ background: white; text-align: left; }}
            input {{ width: 100%; padding: 12px; border: 1px solid #ddd; border-radius: 25px; margin: 10px 0; }}
            button {{ background: #25D366; color: white; border: none; padding: 12px 25px; border-radius: 25px; cursor: pointer; width: 100%; }}
            button:hover {{ background: #1ea952; }}
        </style>
    </head>
    <body>
        <div class="container">
            <div class="header">
                <h1>🤖 WhatsAtende Demo</h1>
                <p>Simulador de Demonstracao - Versao Vercel</p>
            </div>
            
            <div class="status success">✅ {BOT_STATUS}</div>
            
            <div class="chat-container" id="chatContainer">
                <div class="message bot-message">
                    Bem-vindo ao WhatsAtende Demo! 🎉<br>
                    Digite qualquer mensagem para comecar a demonstracao.
                </div>
            </div>
            
            <input type="text" id="messageInput" placeholder="Digite sua mensagem..." onkeypress="handleKeyPress(event)">
            <button onclick="sendMessage()">Enviar Mensagem</button>
        </div>

        <script>
            function addMessage(text, isUser = false) {{
                const chatContainer = document.getElementById('chatContainer');
                const messageDiv = document.createElement('div');
                messageDiv.className = `message ${{isUser ? 'user-message' : 'bot-message'}}`;
                messageDiv.innerHTML = text.replace(/\\n/g, '<br>');
                chatContainer.appendChild(messageDiv);
                chatContainer.scrollTop = chatContainer.scrollHeight;
            }}
            
            function sendMessage() {{
                const input = document.getElementById('messageInput');
                const message = input.value.trim();
                if (!message) return;
                
                addMessage(message, true);
                input.value = '';
                
                fetch('/api/chat', {{
                    method: 'POST',
                    headers: {{ 'Content-Type': 'application/json' }},
                    body: JSON.stringify({{ user_id: 'demo_user', message: message }})
                }})
                .then(response => response.json())
                .then(data => {{
                    if (data.error) {{
                        addMessage(`Erro: ${{data.error}}`);
                    }} else {{
                        addMessage(data.response);
                    }}
                }})
                .catch(error => {{
                    addMessage(`Erro de conexao: ${{error}}`);
                }});
            }}
            
            function handleKeyPress(event) {{
                if (event.key === 'Enter') {{
                    sendMessage();
                }}
            }}
            
            // Foco automático no input
            document.getElementById('messageInput').focus();
        </script>
    </body>
    </html>
    '''

@app.route('/api/chat', methods=['POST'])
def chat():
    try:
        if not bot:
            return jsonify({
                'error': 'Bot não inicializado',
                'status': 'error'
            }), 500
        
        data = request.json or {}
        user_id = data.get('user_id', 'demo_user')
        message = data.get('message', '')
        
        if not message:
            return jsonify({
                'error': 'Mensagem vazia',
                'status': 'error'
            }), 400
        
        response = bot.process_message(user_id, message)
        
        return jsonify({
            'response': response,
            'user_id': user_id,
            'status': 'success'
        })
        
    except Exception as e:
        return jsonify({
            'error': f'Erro interno: {str(e)}',
            'traceback': traceback.format_exc(),
            'status': 'error'
        }), 500

@app.route('/api/health')
def health():
    return jsonify({
        'status': 'healthy' if bot else 'error',
        'bot_loaded': bot is not None,
        'bot_status': BOT_STATUS,
        'timestamp': datetime.datetime.now().isoformat()
    })

# Vercel entry point
app = app