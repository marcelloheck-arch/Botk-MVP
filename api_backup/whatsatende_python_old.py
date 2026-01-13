"""
WhatsAtende Demo Bot - Versão Python
Assistente Virtual Inteligente para demonstração comercial
Sem necessidade de Node.js
"""

import time
import datetime
import json
import re
from typing import Dict, Optional

class WhatsAtendeBot:
    def __init__(self):
        self.sessions = {}
        self.config = {
            'bot_number': '48999314665',
            'contact_email': 'expertdigitalnovo@gmail.com',
            'demo_mode': True,
            'session_timeout': 300  # 5 minutos
        }

        self.states = {
            'INITIAL': 'initial',
            'COLLECTING_NAME': 'collecting_name',
            'COLLECTING_PHONE': 'collecting_phone',
            'MAIN_MENU': 'main_menu',
            'SECONDARY_MENU': 'secondary_menu',
            'FULL_MENU': 'full_menu',
            'TRANSFER': 'transfer',
            'FINISHED': 'finished'
        }

    def get_session(self, user_id: str) -> Dict:
        """Obtém ou cria uma sessão para o usuário"""
        current_time = time.time()

        if user_id in self.sessions:
            session = self.sessions[user_id]
            # Verifica timeout
            if current_time - session['last_activity'] > self.config['session_timeout']:
                self.log_message(f"⏰ Sessão expirou para {user_id}")
                del self.sessions[user_id]
                return self.create_new_session(user_id)
            else:
                session['last_activity'] = current_time
                return session
        else:
            return self.create_new_session(user_id)

    def create_new_session(self, user_id: str) -> Dict:
        """Cria uma nova sessão"""
        session = {
            'user_id': user_id,
            'state': self.states['INITIAL'],
            'name': '',
            'phone': '',
            'created_at': time.time(),
            'last_activity': time.time(),
            'menu_choices': []
        }
        self.sessions[user_id] = session
        self.log_message(f"✨ Nova sessão criada para {user_id}")
        return session

    def log_message(self, message: str):
        """Sistema de logs"""
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"[{timestamp}] [WHATSATENDE] {message}")

    def validate_name(self, name: str) -> bool:
        """Valida se o nome tem pelo menos 2 caracteres"""
        return len(name.strip()) >= 2

    def validate_phone(self, phone: str) -> bool:
        """Valida formato de telefone brasileiro"""
        # Remove espaços e caracteres especiais
        clean_phone = re.sub(r'[^\d]', '', phone)
        # Aceita formatos: 11999999999, 48999999999, etc.
        return len(clean_phone) >= 10 and len(clean_phone) <= 11

    def process_message(self, user_id: str, message: str) -> str:
        """Processa mensagem recebida e retorna resposta"""
        session = self.get_session(user_id)
        message = message.strip()

        self.log_message(f"Mensagem de {user_id}: {message}")

        if session['state'] == self.states['INITIAL']:
            return self.handle_initial_state(session, message)

        elif session['state'] == self.states['COLLECTING_NAME']:
            return self.handle_name_collection(session, message)

        elif session['state'] == self.states['COLLECTING_PHONE']:
            return self.handle_phone_collection(session, message)

        elif session['state'] == self.states['MAIN_MENU']:
            return self.handle_main_menu(session, message)

        elif session['state'] == self.states['SECONDARY_MENU']:
            return self.handle_secondary_menu(session, message)

        elif session['state'] == self.states['FULL_MENU']:
            return self.handle_full_menu(session, message)

        else:
            return "❌ Desculpe, não entendi. Vamos recomeçar nossa conversa!"

    def handle_initial_state(self, session: Dict, message: str = "") -> str:
        """Estado inicial - aceita qualquer entrada para iniciar conversa"""
        
        # Se há mensagem e é um nome válido, usa como nome
        if message and self.validate_name(message):
            session['name'] = message.strip().title()
            session['state'] = self.states['COLLECTING_PHONE']
            self.log_message(f"Nome coletado diretamente: {session['name']}")
            return f"""Olá {session['name']}! Sou o assistente Virtual WhatsAtende! 😊

Agora, por favor, informe seu número de celular com DDD:"""
        
        # Caso contrário, solicita o nome
        else:
            session['state'] = self.states['COLLECTING_NAME']
            return """Olá! Sou o assistente Virtual WhatsAtende! 😊

Para começarmos, qual é o seu nome?"""

    def handle_name_collection(self, session: Dict, message: str) -> str:
        """Coleta o nome do usuário"""
        if not self.validate_name(message):
            return "Por favor, informe um nome válido com pelo menos 2 caracteres:"

        session['name'] = message.strip().title()
        session['state'] = self.states['COLLECTING_PHONE']
        
        self.log_message(f"Nome coletado para {session['user_id']}: {session['name']}")

        return "Agora, por favor, informe seu número de celular com DDD:"

    def handle_phone_collection(self, session: Dict, message: str) -> str:
        """Coleta o telefone do usuário"""
        if not self.validate_phone(message):
            return "Por favor, informe um número de telefone válido no formato: DD XXXXX-XXXX"     

        session['phone'] = message.strip()
        session['state'] = self.states['MAIN_MENU']

        self.log_message(f"Telefone coletado para {session['user_id']}: {session['phone']}")

        return f"""{session['name']}, é um prazer ter você aqui! 🎉

Isso é um teste de demonstração. Escolha uma opção abaixo:

**1️⃣ - Principais Funcionalidades**
**2️⃣ - Antes do WhatsAtende**
**3️⃣ - Depois do WhatsAtende**

Digite o número da opção desejada:"""

    def handle_main_menu(self, session: Dict, message: str) -> str:
        """Menu principal"""
        if message == "1":
            response = self.get_funcionalidades_text()
        elif message == "2":
            response = self.get_antes_text()
        elif message == "3":
            response = self.get_depois_text()
        else:
            return """❌ Opção inválida! Por favor, digite:

**1** - Principais Funcionalidades
**2** - Antes do WhatsAtende
**3** - Depois do WhatsAtende"""

        session['menu_choices'].append(message)
        session['state'] = self.states['SECONDARY_MENU']

        return response + "\n\n" + self.get_secondary_menu_text()

    def handle_secondary_menu(self, session: Dict, message: str) -> str:
        """Menu secundário"""
        if message == "1":
            response = self.get_funcionalidades_text()
        elif message == "2":
            response = self.get_antes_text()
        elif message == "3":
            response = self.get_planos_text()
        else:
            return """❌ Opção inválida! Por favor, digite:

**1** - Quero ver o menu 2
**2** - Quero ver o menu 3
**3** - Conhecer nossos planos e valores"""

        session['menu_choices'].append(message)
        session['state'] = self.states['FULL_MENU']
        
        if message == "3":
            return response + "\n\n" + self.get_full_menu_text(session['name'])
        else:
            return response + "\n\n" + self.get_full_menu_text(session['name'])

    def handle_full_menu(self, session: Dict, message: str) -> str:
        """Menu completo"""
        if message == "1":
            return self.get_funcionalidades_text() + "\n\n" + self.get_full_menu_text(session['name'])
        elif message == "2":
            return self.get_antes_text() + "\n\n" + self.get_full_menu_text(session['name'])
        elif message == "3":
            return self.get_depois_text() + "\n\n" + self.get_full_menu_text(session['name'])        
        elif message == "4":
            return self.handle_transfer(session)
        elif message == "5":
            return self.handle_goodbye(session)
        else:
            return f"""❌ Opção inválida! Por favor, digite:

**1** - Principais Funcionalidades
**2** - Antes do WhatsAtende
**3** - Depois do WhatsAtende
**4** - Falar com o atendente
**5** - Encerrar conversa

Digite o número da opção desejada:"""

    def handle_transfer(self, session: Dict) -> str:
        """Transferência para humano"""
        self.log_message(f"[TRANSFERENCIA] Nome: {session['name']}, Telefone: {session['phone']}, WhatsApp: {session['user_id']}")
        session['state'] = self.states['TRANSFER']

        return "Transferindo para um atendente humano... Por favor, aguarde! 👤"

    def handle_goodbye(self, session: Dict) -> str:
        """Despedida"""
        session['state'] = self.states['FINISHED']

        return f"""{session['name']}, agradecemos muito pelo seu contato! 🙏

Estamos à disposição sempre que precisar.
Até breve! 😊

📧 **Contato:** {self.config['contact_email']}
📱 **WhatsApp:** {self.config['bot_number']}"""

    def get_funcionalidades_text(self) -> str:
        return """🔧 **Principais Funcionalidades:**

• **Atendimento Automatizado** - Respostas instantâneas 24/7
• **Consulta de Serviços ou Produtos** - Informações completas
• **Sistema de Agendamento** - Marcação automática de horários
• **Relação de Documentos** - Envio automático de listas
• **Transferência para Humano** - Suporte quando necessário"""

    def get_antes_text(self) -> str:
        return """😰 **Antes do WhatsAtende:**

• Clientes esperam muito tempo por respostas
• Perguntas repetitivas tomam tempo da equipe
• Falhas de atendimento geram perda de oportunidades
• APIs e bots em nuvem são caros e exigem mensalidades"""

    def get_depois_text(self) -> str:
        return """🚀 **Depois do WhatsAtende:**

• Atendimento automático direto no seu computador
• Respostas instantâneas, mesmo fora do horário
• Agendamentos, consultas e envio de documentos simples
• Total controle local, sem depender de terceiros"""

    def get_planos_text(self) -> str:
        return """💎 **Nossos Planos e Valores:**

**💎 3.1 Licença Única**
• Instalação local
• Uso vitalício
• Suporte técnico opcional
• **Investimento: R$ 1.289** (pagamento único)

**🚀 3.2 Plano Instalação + Suporte**
• Instalação inicial
• Atualizações e backup
• Suporte remoto mensal
• **Investimento: R$ 689** (instalação) + **R$ 89/mês**"""

    def get_secondary_menu_text(self) -> str:
        return """Agora você pode:

**1️⃣ - Quero ver o menu 2**
**2️⃣ - Quero ver o menu 3**
**3️⃣ - Conhecer nossos planos e valores**

Digite o número da opção desejada:"""

    def get_full_menu_text(self, name: str) -> str:
        return f"""{name}, agora você pode explorar todas as opções:

**1️⃣ - Principais Funcionalidades**
**2️⃣ - Antes do WhatsAtende**
**3️⃣ - Depois do WhatsAtende**
**4️⃣ - Falar com o atendente**
**5️⃣ - Encerrar conversa**

Digite o número da opção desejada:"""


def main():
    """Função principal para teste do bot"""
    bot = WhatsAtendeBot()

    print("=" * 60)
    print("🤖 WHATSATENDE DEMO BOT - VERSÃO PYTHON")
    print("=" * 60)
    print("📱 Número configurado: 48999314665")
    print("📧 Email: expertdigitalnovo@gmail.com")
    print("📧 Digite 'sair' para encerrar o teste")
    print("=" * 60)

    # Simula um usuário de teste
    test_user = "5511999999999"  # Número fictício para teste

    print("\n🎯 INICIANDO SIMULAÇÃO DE CONVERSA...")
    print("-" * 40)

    while True:
        user_input = input("\n👤 Você: ").strip()

        if user_input.lower() in ['sair', 'exit', 'quit']:
            print("\n✅ Teste encerrado!")
            break

        if user_input:
            response = bot.process_message(test_user, user_input)
            print(f"\n🤖 Bot: {response}")
            print("-" * 40)


if __name__ == "__main__":
    main()