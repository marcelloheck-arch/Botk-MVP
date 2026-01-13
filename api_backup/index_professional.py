"""
WhatsAtende Demo - Versão Profissional para Vercel
Design sofisticado com bot stateless otimizado
"""

from flask import Flask, jsonify, request
import datetime
import re

app = Flask(__name__)

# Bot integrado e otimizado para Vercel
class WhatsAtendeBotProfessional:
    def __init__(self):
        self.config = {
            'bot_number': '48999314665',
            'contact_email': 'expertdigitalnovo@gmail.com'
        }

    def log_message(self, message):
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"[{timestamp}] [WHATSATENDE] {message}")

    def is_greeting(self, message):
        greetings = [
            'ola', 'olá', 'oi', 'hello', 'hi', 'hey', 'hola',
            'bom dia', 'boa tarde', 'boa noite', 'opa', 'eai', 'e ai',
            'teste', 'testando', 'test', 'iniciar', 'começar', 'start'
        ]
        msg_lower = message.lower().strip()
        return any(greeting == msg_lower or greeting in msg_lower for greeting in greetings)

    def validate_name(self, name):
        if len(name.strip()) < 2:
            return False
        if re.search(r'\d{8,}', name):
            return False
        if self.is_greeting(name):
            return False
        return True

    def validate_phone(self, phone):
        clean_phone = re.sub(r'[^\d]', '', phone)
        return len(clean_phone) >= 10 and len(clean_phone) <= 11

    def looks_like_phone(self, message):
        return bool(re.search(r'\d{8,}', message))

    def is_menu_option(self, message):
        return message.strip() in ['1', '2', '3', '4', '5']

    def process_message(self, user_id, message):
        message = message.strip()
        self.log_message(f"Processando: '{message}'")

        # 1. Opções de menu
        if self.is_menu_option(message):
            return self.handle_menu_option(message)

        # 2. Telefone
        elif self.looks_like_phone(message):
            if self.validate_phone(message):
                return f"""✅ Perfeito! Telefone registrado: {message}

🎯 **Escolha o que deseja saber:**

**1️⃣ - Principais Funcionalidades**
**2️⃣ - Antes do WhatsAtende**
**3️⃣ - Depois do WhatsAtende**
**4️⃣ - Falar com o atendente**
**5️⃣ - Finalizar atendimento**

Digite o número da opção:"""
            else:
                return """❌ Telefone inválido. Use o formato:

**Exemplos:** 48 99999-9999 ou 48999999999

Por favor, digite seu telefone:"""

        # 3. Nome válido
        elif self.validate_name(message):
            name = message.strip().title()
            return f"""👋 Olá {name}! Sou o assistente Virtual WhatsAtende!

É um prazer conhecê-lo! Para continuarmos, preciso do seu telefone:

**Digite:** Seu número com DDD
**Exemplo:** 48 99999-9999"""

        # 4. Saudações
        else:
            return """🤖 Olá! Bem-vindo ao **WhatsAtende Demo**!

Sou seu assistente virtual e vou demonstrar como podemos revolucionar o atendimento do seu negócio!

**Para começar, digite seu nome:**"""

    def handle_menu_option(self, option):
        if option == "1":
            return f"""{self.get_funcionalidades_text()}

{self.get_continue_menu()}"""
        elif option == "2":
            return f"""{self.get_antes_text()}

{self.get_continue_menu()}"""
        elif option == "3":
            return f"""{self.get_depois_text()}

{self.get_continue_menu()}"""
        elif option == "4":
            return f"""🔄 **Transferindo para atendente humano...**

Em instantes nossa equipe entrará em contato!

📞 **Contatos diretos:**
📧 Email: {self.config['contact_email']}
📱 WhatsApp: (48) 99931-4665
🔗 Link direto: https://w.app/q8drou

Aguarde nossa chamada! 👨‍💼"""
        elif option == "5":
            return f"""👋 **Obrigado por conhecer o WhatsAtende!**

Foi um prazer demonstrar nossa solução!

📞 **Entre em contato:**
📧 {self.config['contact_email']}
📱 (48) 99931-4665
🔗 https://w.app/q8drou

**Vamos implementar o WhatsAtende no seu negócio?**

Até breve! 😊"""
        else:
            return """❌ Opção inválida!

**Opções disponíveis:**
**1** - Funcionalidades
**2** - Antes do WhatsAtende
**3** - Depois do WhatsAtende
**4** - Falar com atendente
**5** - Finalizar

Digite um número de 1 a 5:"""

    def get_continue_menu(self):
        return """**Continue explorando:**

**1️⃣ - Principais Funcionalidades**
**2️⃣ - Antes do WhatsAtende**
**3️⃣ - Depois do WhatsAtende**
**4️⃣ - Falar com o atendente**
**5️⃣ - Finalizar atendimento**

**Digite o número da opção:**"""

    def get_funcionalidades_text(self):
        return """🔧 **PRINCIPAIS FUNCIONALIDADES:**

✅ **Atendimento 24h Automatizado**
   → Respostas instantâneas mesmo de madrugada
   → Nunca mais perca vendas por demora

✅ **Consultas Inteligentes**
   → Produtos, serviços, preços automatizados
   → Base de conhecimento sempre atualizada

✅ **Agendamento Automático**
   → Marcação de horários sem intervenção
   → Sincronização com Google Calendar

✅ **Envio de Documentos**
   → PDFs, tabelas, listas automáticas
   → Organização profissional

✅ **Transferência Inteligente**
   → Detecta quando precisa de humano
   → Preserva contexto da conversa"""

    def get_antes_text(self):
        return """😰 **PROBLEMAS ANTES DO WHATSATENDE:**

❌ **Tempo Desperdiçado**
   → Mesmas perguntas 50x por dia
   → Equipe sobrecarregada com básico

❌ **Vendas Perdidas**
   → Clientes desistem por demora
   → Concorrência mais rápida

❌ **Trabalho Sem Parar**
   → Pressão para responder 24h
   → Equipe estressada e cansada

❌ **Custos Abusivos**
   → APIs caras (R$ 300+ /mês)
   → Dependência de terceiros

❌ **Qualidade Inconsistente**
   → Respostas diferentes da equipe
   → Informações desencontradas"""

    def get_depois_text(self):
        return """🚀 **DEPOIS DO WHATSATENDE:**

✅ **Produtividade x10**
   → Equipe focada em vendas complexas
   → Fim das perguntas repetitivas

✅ **Vendas 24 Horas**
   → Atendimento perfeito de madrugada
   → Zero oportunidades perdidas

✅ **Liberdade Total**
   → Equipe pode descansar tranquila
   → Sistema funciona sozinho

✅ **Economia Real**
   → Sem mensalidades abusivas
   → ROI em menos de 60 dias

✅ **Padronização Perfeita**
   → Mesma qualidade sempre
   → Informações consistentes

💰 **INVESTIMENTO E PLANOS:**

**💎 LICENÇA ÚNICA - R$ 1.289**
• Sistema completo instalado no seu PC
• Uso ilimitado e vitalício
• Suporte técnico para implementação
• Sem mensalidades ou taxas extras

**🚀 PLANO PREMIUM - R$ 689 + R$ 89/mês**
• Instalação + configuração personalizada
• Atualizações automáticas mensais
• Backup em nuvem profissional
• Suporte técnico ilimitado

**🎁 AMBOS INCLUEM:**
• Treinamento completo da equipe
• Configuração para seu negócio específico
• 30 dias de garantia total
• Implementação acompanhada"""

# Inicializar bot
bot = WhatsAtendeBotProfessional()

@app.route('/')
def index():
    return '''
<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>WhatsAtende Demo - Simulador Profissional</title>
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
            position: relative;
        }
        
        .header h1 {
            margin-bottom: 5px;
            font-size: 1.5em;
        }
        
        .header p {
            opacity: 0.9;
            font-size: 0.9em;
        }
        
        .contact-info {
            background: rgba(255,255,255,0.1);
            padding: 8px;
            border-radius: 10px;
            margin-top: 10px;
            font-size: 0.8em;
        }
        
        .instructions {
            background: #E3F2FD;
            padding: 15px;
            border-left: 4px solid #2196F3;
            color: #1976D2;
        }
        
        .instructions h3 {
            margin-bottom: 8px;
            display: flex;
            align-items: center;
        }
        
        .instructions ul {
            list-style: none;
            padding-left: 0;
        }
        
        .instructions li {
            margin: 3px 0;
            padding-left: 20px;
            position: relative;
        }
        
        .instructions li::before {
            content: "•";
            color: #2196F3;
            position: absolute;
            left: 0;
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
            background: #F5F5F5;
            border-radius: 15px;
            scroll-behavior: smooth;
        }
        
        .message {
            margin-bottom: 15px;
            padding: 12px 16px;
            border-radius: 18px;
            max-width: 80%;
            word-wrap: break-word;
            line-height: 1.4;
            animation: slideIn 0.3s ease-out;
        }
        
        @keyframes slideIn {
            from { opacity: 0; transform: translateY(10px); }
            to { opacity: 1; transform: translateY(0); }
        }
        
        .user-message {
            background: #DCF8C6;
            margin-left: auto;
            text-align: right;
            border-bottom-right-radius: 5px;
        }
        
        .bot-message {
            background: white;
            border: 1px solid #E0E0E0;
            border-bottom-left-radius: 5px;
            box-shadow: 0 1px 2px rgba(0,0,0,0.1);
        }
        
        .input-container {
            display: flex;
            gap: 10px;
            align-items: center;
            background: #F8F8F8;
            padding: 15px;
            border-radius: 25px;
            border: 2px solid #E0E0E0;
        }
        
        .input-container:focus-within {
            border-color: #25D366;
        }
        
        #messageInput {
            flex: 1;
            border: none;
            outline: none;
            background: transparent;
            font-size: 16px;
            padding: 8px;
        }
        
        .send-button {
            background: #25D366;
            color: white;
            border: none;
            border-radius: 50%;
            width: 45px;
            height: 45px;
            cursor: pointer;
            display: flex;
            align-items: center;
            justify-content: center;
            transition: all 0.2s;
        }
        
        .send-button:hover {
            background: #1EA952;
            transform: scale(1.1);
        }
        
        .send-button:active {
            transform: scale(0.95);
        }
        
        .quick-buttons {
            display: flex;
            gap: 8px;
            margin-bottom: 15px;
            flex-wrap: wrap;
        }
        
        .quick-btn {
            background: #E8F5E8;
            color: #25D366;
            border: 1px solid #25D366;
            padding: 8px 12px;
            border-radius: 20px;
            cursor: pointer;
            font-size: 0.85em;
            transition: all 0.2s;
        }
        
        .quick-btn:hover {
            background: #25D366;
            color: white;
        }
        
        .status {
            text-align: center;
            padding: 8px;
            font-size: 0.85em;
            color: #666;
        }
        
        .typing-indicator {
            background: white;
            border: 1px solid #E0E0E0;
            border-radius: 18px;
            padding: 12px 16px;
            max-width: 80px;
            margin-bottom: 15px;
            animation: pulse 1.5s infinite;
        }
        
        @keyframes pulse {
            0%, 100% { opacity: 1; }
            50% { opacity: 0.5; }
        }
        
        @media (max-width: 768px) {
            .container {
                width: 95%;
                height: 95vh;
                border-radius: 15px;
            }
            
            .header {
                padding: 15px;
            }
            
            .header h1 {
                font-size: 1.3em;
            }
            
            .chat-container {
                padding: 15px;
            }
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>🤖 WhatsAtende Demo</h1>
            <p>Simulador de Demonstração - Versão Vercel</p>
            <div class="contact-info">
                📱 Número: (48) 99931-4665 | 📧 expertdigitalnovo@gmail.com
            </div>
        </div>
        
        <div class="instructions">
            <h3>🎯 Como usar:</h3>
            <ul>
                <li>Digite uma mensagem para iniciar</li>
                <li>Siga o fluxo de demonstração</li>
                <li>Use os botões rápidos ou digite as opções</li>
            </ul>
        </div>
        
        <div class="chat-container">
            <div class="messages" id="messages">
                <div class="message bot-message">
                    Bem-vindo ao WhatsAtende Demo! 🎉<br>
                    Digite qualquer mensagem para começar a demonstração.
                </div>
            </div>
            
            <div class="quick-buttons">
                <button class="quick-btn" onclick="sendMessage('Iniciar Conversa')">Iniciar Conversa</button>
                <button class="quick-btn" onclick="sendMessage('João Silva')">Exemplo Nome</button>
                <button class="quick-btn" onclick="sendMessage('48999887766')">Exemplo Telefone</button>
            </div>
            
            <div class="input-container">
                <input type="text" id="messageInput" placeholder="Digite sua mensagem..." onkeypress="handleKeyPress(event)">
                <button class="send-button" onclick="sendMessage()">
                    <span>▶</span>
                </button>
            </div>
            
            <div class="status" id="status">
                Pronto para conversar! 💬
            </div>
        </div>
    </div>

    <script>
        const messagesContainer = document.getElementById('messages');
        const messageInput = document.getElementById('messageInput');
        const status = document.getElementById('status');
        
        function addMessage(text, isUser = false) {
            const messageDiv = document.createElement('div');
            messageDiv.className = `message ${isUser ? 'user-message' : 'bot-message'}`;
            messageDiv.innerHTML = text.replace(/\\n/g, '<br>').replace(/\\*\\*(.*?)\\*\\*/g, '<strong>$1</strong>');
            messagesContainer.appendChild(messageDiv);
            messagesContainer.scrollTop = messagesContainer.scrollHeight;
        }
        
        function showTyping() {
            const typingDiv = document.createElement('div');
            typingDiv.className = 'typing-indicator';
            typingDiv.id = 'typing';
            typingDiv.innerHTML = '...';
            messagesContainer.appendChild(typingDiv);
            messagesContainer.scrollTop = messagesContainer.scrollHeight;
        }
        
        function hideTyping() {
            const typing = document.getElementById('typing');
            if (typing) typing.remove();
        }
        
        function sendMessage(text = null) {
            const message = text || messageInput.value.trim();
            if (!message) return;
            
            addMessage(message, true);
            if (!text) messageInput.value = '';
            
            status.textContent = 'Bot digitando...';
            showTyping();
            
            fetch('/api/chat', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({
                    user_id: 'demo_user',
                    message: message
                })
            })
            .then(response => response.json())
            .then(data => {
                hideTyping();
                if (data.error) {
                    addMessage(`❌ Erro: ${data.error}`);
                } else {
                    addMessage(data.response);
                }
                status.textContent = 'Pronto para conversar! 💬';
            })
            .catch(error => {
                hideTyping();
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
    </script>
</body>
</html>
    '''

@app.route('/api/chat', methods=['POST'])
def chat():
    try:
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
            'status': 'error'
        }), 500

@app.route('/api/health')
def health():
    return jsonify({
        'status': 'healthy',
        'bot_loaded': True,
        'timestamp': datetime.datetime.now().isoformat()
    })

# Vercel entry point
app = app