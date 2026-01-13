"""
botK - Versão Profissional para Vercel
Design sofisticado com bot stateless otimizado
"""

from flask import Flask, jsonify, request
import datetime
import re

app = Flask(__name__)

# Bot integrado e otimizado para Vercel
class BotKProfessional:
    def __init__(self):
        self.config = {
            'bot_number': '48999314665',
            'contact_email': 'expertdigitalnovo@gmail.com'
        }

    def log_message(self, message):
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"[{timestamp}] [BOTK] {message}")

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
        return message.strip() in ['1', '2', '3', '4']

    def is_submenu_option(self, message):
        """Verifica se é opção de submenu"""
        msg = message.strip().lower()
        return msg in ['sim', 'não', 'nao', 'ainda não', 'ainda nao', 
                       'sim, já sou cliente', 'já sou cliente', 'sou cliente',
                       '✅ sim, já sou cliente', '❌ ainda não']

    def process_message(self, user_id, message):
        message = message.strip()
        self.log_message(f"Processando: '{message}'")

        # 1. Opções de menu principal
        if self.is_menu_option(message):
            return self.handle_menu_option(message)

        # 2. Subopções do fluxo "Fazer pedido"
        elif self.is_submenu_option(message):
            return self.handle_submenu_option(message)

        # 3. Opção "3" do submenu dúvidas (produtos mais vendidos)
        elif message.strip() == "3" and hasattr(self, '_last_menu') and self._last_menu == 'duvidas':
            return """Esses são os produtos mais pedidos hoje:
- Whey Protein 
- Barras proteicas 
- Vitaminas

Quer ajuda para escolher?

Obrigado pelo contato 😊 Sempre que precisar, é só chamar."""

        # 4. Telefone
        elif self.looks_like_phone(message):
            if self.validate_phone(message):
                return f"""✅ Perfeito! Telefone registrado: {message}

Olá 👋 
Pra te atender melhor, me diga o que você precisa agora:

1️⃣ Fazer um pedido 
2️⃣ Tirar dúvida sobre produtos 
3️⃣ Entrega / horário 
4️⃣ Falar com um atendente

**Digite o número da opção:**"""
            else:
                return """❌ Telefone inválido. Use o formato:

**Exemplos:** 48 99999-9999 ou 48999999999

Por favor, digite seu telefone:"""

        # 5. Nome válido
        elif self.validate_name(message):
            name = message.strip().title()
            return f"""👋 Olá {name}!

Para continuarmos, preciso do seu telefone:

**Digite:** Seu número com DDD
**Exemplo:** 48 99999-9999"""

        # 6. Saudações
        else:
            return f"""Olá 👋 
Pra te atender melhor, me diga o que você precisa agora:

1️⃣ Fazer um pedido 
2️⃣ Tirar dúvida sobre produtos 
3️⃣ Entrega / horário 
4️⃣ Falar com um atendente

**Digite o número da opção:**"""

    def handle_menu_option(self, option):
        if option == "1":
            return """Perfeito 👍 Você já é cliente cadastrado?

✅ Sim, já sou cliente
❌ Ainda não

**Digite sua opção:**"""
        elif option == "2":
            self._last_menu = 'duvidas'  # Controle de contexto
            return """Selecione o tipo de dúvida:

1️⃣ Preço 
2️⃣ Composição / benefício 
3️⃣ Produtos mais vendidos
4️⃣ Outra dúvida

**Digite o número da opção:**"""
        elif option == "3":
            return """Sobre entregas 👇

✔ As entregas são feitas por rota 
✔ O prazo depende da região 
✔ Um atendente confirma o horário após o pedido

Obrigado pelo contato 😊 Sempre que precisar, é só chamar."""
        elif option == "4":
            return """Certo 👍 Vou encaminhar você para um atendente.

Obrigado pelo contato 😊 Sempre que precisar, é só chamar."""
        else:
            return """❌ Opção inválida!

**Opções disponíveis:**
**1** - Fazer um pedido
**2** - Dúvida sobre produtos
**3** - Entrega / horário
**4** - Falar com atendente

Digite um número de 1 a 4:"""

    def handle_submenu_option(self, message):
        """Lida com respostas das subopções"""
        msg = message.strip().lower()
        
        # Fluxo 1: Respostas sobre cadastro de cliente
        if msg in ['sim', 'sim, já sou cliente', 'já sou cliente', 'sou cliente', '✅ sim, já sou cliente']:
            return """Ótimo. Para agilizar seu pedido, clique abaixo para acessar o sistema de pedidos.

[Link do sistema de pedidos da empresa]

Nesse piloto, o pedido vai direto pro sistema que vocês já usam.

Obrigado pelo contato 😊 Sempre que precisar, é só chamar."""
            
        elif msg in ['não', 'nao', 'ainda não', 'ainda nao', '❌ ainda não']:
            return """Sem problema 🙂 Um atendente vai te orientar rapidinho para cadastro.

Obrigado pelo contato 😊 Sempre que precisar, é só chamar."""
            
        else:
            return """Não entendi sua resposta. Digite:

✅ Sim, já sou cliente
❌ Ainda não"""

    def get_continue_menu(self):
        return """**Continue explorando:**

**1️⃣ - Principais Funcionalidades**
**2️⃣ - Antes do botK**
**3️⃣ - Depois do botK**
**4️⃣ - Falar com o atendente**
**5️⃣ - Finalizar atendimento**

**Digite o número da opção:**"""

    def get_funcionalidades_text(self):
        return """� **RECURSOS QUE REVOLUCIONAM SEU NEGÓCIO:**

💎 **Automação Completa 24/7**
   → Atendimento profissional mesmo dormindo
   → Converte leads enquanto você descansa
   → ROI comprovado em menos de 30 dias

🧠 **Inteligência Empresarial Avançada**
   → Respostas personalizadas por categoria de cliente
   → Aprendizado contínuo do comportamento
   → Integração total com seu CRM/sistema

📅 **Gestão Automática de Agenda**
   → Agendamentos sem conflitos ou erros humanos
   → Confirmações e lembretes automáticos
   → Sincronização multi-plataforma

📋 **Envio Inteligente de Materiais**
   → Catálogos e orçamentos na hora certa
   → Personalização por perfil de cliente
   → Rastreamento de engajamento

🎯 **Escalada Inteligente para Vendas**
   → Identifica oportunidades qualificadas
   → Transfere com contexto completo
   → Multiplica sua capacidade de conversão"""

    def get_antes_text(self):
        return """� **PREJUÍZOS ANTES DO BOTK:**

🔥 **Sangria de Receita Diária**
   → Clientes abandonam por demora (78% em 5min)
   → Concorrentes capturam seus prospects
   → Equipe perdendo vendas por saturação

⏰ **Armadilha do Tempo Improdutivo**
   → 6-8h diárias em perguntas básicas repetitivas
   → Zero foco em vendas estratégicas e complexas
   → Burnout e rotatividade alta da equipe

🌙 **Escuridão Comercial Noturna**
   → 16h por dia sem atendimento = 0 vendas
   → Mercado internacional perdido
   → Fins de semana sem faturamento

💰 **Custos Explosivos e Dependência**
   → Ferramentas caras: R$ 500-2000/mês
   → Dependência total de terceiros
   → Licenças que drenam o fluxo de caixa

🎯 **Inconsistência que Mata Vendas**
   → Cada atendente responde diferente
   → Informações desencontradas confundem clientes
   → Imagem não profissional prejudica conversões"""

    def get_depois_text(self):
        return """🏆 **TRANSFORMAÇÃO TOTAL COM BOTK:**

💎 **Explosão de Produtividade (300-500%)**
   → Equipe vendendo apenas oportunidades qualificadas
   → 8h diárias livres para estratégia e fechamentos
   → Cada vendedor rende como 3-5 pessoas

🌟 **Máquina de Vendas 24/7/365**
   → Faturamento noturno e fins de semana automático
   → Captação internacional sem barreira de fuso
   → Zero oportunidades desperdiçadas NUNCA MAIS

🗽 **Liberdade Empresarial Verdadeira**
   → Viaje tranquilo: negócio funciona sozinho
   → Equipe descansa sem stress de "perder clientes"
   → Escalabilidade sem contratar mais pessoas

💰 **Economia Brutal + ROI Explosivo**
   → Elimina R$ 500-2000/mês em ferramentas
   → ROI típico: 300-800% em 90 dias
   → Investimento único se paga em 1-2 meses

🎯 **Excelência Operacional Garantida**
   → Atendimento padrão Forbes 500 sempre
   → Clientes impressionados com profissionalismo
   → Marca posicionada como líder de mercado

� **INVESTIMENTO TRANSFORMADOR:**

**� IMPLEMENTAÇÃO COMPLETA - R$ 2.497**
• Sistema proprietário instalado no seu servidor
• Configuração 100% personalizada para seu negócio
• Treinamento completo da equipe (16h)
• 90 dias de suporte técnico premium
• Garantia total de 60 dias ou dinheiro de volta

**� DIFERENCIAIS EXCLUSIVOS:**
• Tecnologia proprietária (não terceirizada)
• Customização ilimitada para seu segmento
• Integração com seus sistemas existentes
• Atualizações e melhorias vitalícias
• Consultoria estratégica inclusa"""

# Inicializar bot
bot = BotKProfessional()

@app.route('/')
def index():
    return '''
<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>botK Demo - Simulador Profissional</title>
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
            <h1>🤖 botK Demo</h1>
            <p>Simulador de Automação - Versão Vercel</p>
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
                    Bem-vindo ao botK Demo! 🎉<br>
                    Digite qualquer mensagem para começar a demonstração da automação.
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
# Para o Vercel funcionar corretamente
if __name__ == '__main__':
    app.run(debug=True)