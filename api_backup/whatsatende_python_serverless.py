"""
WhatsAtende Demo Bot - Versão Python CORRIGIDA para Vercel
Assistente Virtual Inteligente para demonstração comercial
Versão otimizada para ambiente serverless
"""

import time
import datetime
import json
import re
from typing import Dict, Optional

class WhatsAtendeBot:
    def __init__(self):
        # No ambiente serverless, não mantemos sessões persistentes
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

    def is_menu_option(self, message: str) -> bool:
        """Verifica se a mensagem é uma opção de menu"""
        return message.strip() in ['1', '2', '3', '4', '5']

    def is_greeting_or_start(self, message: str) -> bool:
        """Verifica se a mensagem é uma saudação ou tentativa de início"""
        greetings = [
            'ola', 'olá', 'oi', 'hello', 'hi', 'bom dia', 'boa tarde', 'boa noite',
            'opa', 'e ai', 'eai', 'hey', 'hola', 'iniciar', 'começar', 'start',
            'teste', 'testando', 'test'
        ]
        message_lower = message.lower().strip()
        return any(greeting in message_lower for greeting in greetings) or len(message.strip()) <= 10

    def process_message(self, user_id: str, message: str) -> str:
        """
        Processa mensagem - VERSÃO SERVERLESS CORRIGIDA
        Cada mensagem é tratada de forma independente para ambiente serverless
        """
        message = message.strip()
        self.log_message(f"Mensagem de {user_id}: {message}")

        # CORREÇÃO PRINCIPAL: Sempre aceitar entrada como possível início
        # Se a mensagem parece ser uma tentativa de iniciar conversa
        if self.is_greeting_or_start(message) or not self.is_menu_option(message):
            
            # Se é um nome válido, aceita diretamente
            if self.validate_name(message):
                self.log_message(f"Aceitando '{message}' como nome direto")
                return f"""Olá {message.strip().title()}! Sou o assistente Virtual WhatsAtende! 😊

Agora, por favor, informe seu número de celular com DDD:"""
            
            # Se não é nome válido, mas parece ser tentativa de início
            else:
                self.log_message(f"'{message}' não é nome válido, solicitando nome")
                return """Olá! Sou o assistente Virtual WhatsAtende! 😊

Para começarmos, qual é o seu nome?"""

        # Se parece ser resposta a telefone (contém números)
        elif re.search(r'\d{8,}', message):
            if self.validate_phone(message):
                return f"""Perfeito! Agora você pode escolher uma opção:

**1️⃣ - Principais Funcionalidades**
**2️⃣ - Antes do WhatsAtende**  
**3️⃣ - Depois do WhatsAtende**

Digite o número da opção desejada:"""
            else:
                return "Por favor, informe um número de telefone válido no formato: DD XXXXX-XXXX"

        # Se é opção de menu
        elif self.is_menu_option(message):
            return self.handle_menu_option(message)

        # Caso padrão - assumir que é tentativa de início
        else:
            if self.validate_name(message):
                return f"""Olá {message.strip().title()}! Sou o assistente Virtual WhatsAtende! 😊

Agora, por favor, informe seu número de celular com DDD:"""
            else:
                return """Olá! Sou o assistente Virtual WhatsAtende! 😊

Para começarmos, qual é o seu nome?"""

    def handle_menu_option(self, option: str) -> str:
        """Processa opções de menu"""
        if option == "1":
            return self.get_funcionalidades_text() + "\n\n" + self.get_menu_text()
        elif option == "2":
            return self.get_antes_text() + "\n\n" + self.get_menu_text()
        elif option == "3":
            return self.get_depois_text() + "\n\n" + self.get_menu_text()
        elif option == "4":
            return self.handle_transfer()
        elif option == "5":
            return self.handle_goodbye()
        else:
            return """❌ Opção inválida! Por favor, digite:

**1** - Principais Funcionalidades
**2** - Antes do WhatsAtende
**3** - Depois do WhatsAtende
**4** - Falar com o atendente  
**5** - Encerrar conversa"""

    def get_menu_text(self) -> str:
        """Menu padrão para continuar navegação"""
        return """Escolha uma opção:

**1️⃣ - Principais Funcionalidades**
**2️⃣ - Antes do WhatsAtende**
**3️⃣ - Depois do WhatsAtende**
**4️⃣ - Falar com o atendente**
**5️⃣ - Encerrar conversa**

Digite o número da opção desejada:"""

    def handle_transfer(self) -> str:
        """Transferência para humano"""
        self.log_message("[TRANSFERENCIA] Solicitada")
        return "Transferindo para um atendente humano... Por favor, aguarde! 👤"

    def handle_goodbye(self) -> str:
        """Despedida"""
        return f"""Agradecemos muito pelo seu contato! 🙏

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
• Total controle local, sem depender de terceiros

💎 **Nossos Planos e Valores:**

**💎 Licença Única**
• Instalação local
• Uso vitalício  
• Suporte técnico opcional
• **Investimento: R$ 1.289** (pagamento único)

**🚀 Plano Instalação + Suporte**
• Instalação inicial
• Atualizações e backup
• Suporte remoto mensal
• **Investimento: R$ 689** (instalação) + **R$ 89/mês**"""


def main():
    """Função principal para teste do bot"""
    bot = WhatsAtendeBot()

    print("=" * 60)
    print("🤖 WHATSATENDE DEMO BOT - VERSÃO SERVERLESS")
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