"""
WhatsAtende Demo Bot - Versão Python CORRIGIDA para Vercel
Assistente Virtual Inteligente para demonstração comercial
Versão STATELESS otimizada para ambiente serverless
"""

import time
import datetime
import json
import re
from typing import Dict, Optional

class WhatsAtendeBot:
    def __init__(self):
        # Configurações básicas
        self.config = {
            'bot_number': '48999314665',
            'contact_email': 'expertdigitalnovo@gmail.com',
            'demo_mode': True
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
        clean_phone = re.sub(r'[^\d]', '', phone)
        return len(clean_phone) >= 10 and len(clean_phone) <= 11

    def is_menu_option(self, message: str) -> bool:
        """Verifica se a mensagem é uma opção de menu"""
        return message.strip() in ['1', '2', '3', '4', '5']

    def contains_numbers(self, message: str) -> bool:
        """Verifica se a mensagem contém números (possível telefone)"""
        return bool(re.search(r'\d{8,}', message))

    def process_message(self, user_id: str, message: str) -> str:
        """
        Processa mensagem - VERSÃO STATELESS PARA VERCEL
        Cada mensagem é tratada de forma completamente independente
        """
        message = message.strip()
        self.log_message(f"Processando mensagem: '{message}'")

        # ESTRATÉGIA STATELESS: Identificar tipo de mensagem e responder adequadamente

        # 1. Se é opção de menu (1, 2, 3, 4, 5)
        if self.is_menu_option(message):
            return self.handle_menu_option(message)

        # 2. Se contém números (provável telefone)
        elif self.contains_numbers(message):
            if self.validate_phone(message):
                return f"""Perfeito! Telefone registrado: {message}

Agora escolha uma opção para saber mais:

**1️⃣ - Principais Funcionalidades**
**2️⃣ - Antes do WhatsAtende**  
**3️⃣ - Depois do WhatsAtende**
**4️⃣ - Falar com o atendente**
**5️⃣ - Encerrar conversa**

Digite o número da opção desejada:"""
            else:
                return """Por favor, informe um número de telefone válido no formato: DD XXXXX-XXXX

Exemplo: 48 99999-9999 ou 48999999999"""

        # 3. Se é um nome válido (mais de 2 caracteres, sem números longos)
        elif self.validate_name(message) and not self.contains_numbers(message):
            name = message.strip().title()
            self.log_message(f"Aceitando '{name}' como nome")
            return f"""Olá {name}! Sou o assistente Virtual WhatsAtende! 😊

Prazer em conhecê-lo! Agora, por favor, informe seu número de celular com DDD:

Exemplo: 48 99999-9999"""

        # 4. Qualquer outra entrada (saudações, palavras curtas, etc.)
        else:
            self.log_message(f"Entrada '{message}' tratada como saudação inicial")
            return """Olá! Sou o assistente Virtual WhatsAtende! 😊

Bem-vindo à nossa demonstração! Para começarmos, qual é o seu nome?"""

    def handle_menu_option(self, option: str) -> str:
        """Processa opções de menu"""
        self.log_message(f"Processando opção de menu: {option}")
        
        if option == "1":
            return self.get_funcionalidades_text() + "\n\n" + self.get_continue_menu()
        elif option == "2":
            return self.get_antes_text() + "\n\n" + self.get_continue_menu()
        elif option == "3":
            return self.get_depois_text() + "\n\n" + self.get_continue_menu()
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

    def get_continue_menu(self) -> str:
        """Menu para continuar navegação"""
        return """Continue explorando:

**1️⃣ - Principais Funcionalidades**
**2️⃣ - Antes do WhatsAtende**
**3️⃣ - Depois do WhatsAtende**
**4️⃣ - Falar com o atendente**
**5️⃣ - Encerrar conversa**

Digite o número da opção desejada:"""

    def handle_transfer(self) -> str:
        """Transferência para humano"""
        self.log_message("Transferência solicitada")
        return f"""🔄 Transferindo para um atendente humano...

Em instantes você será conectado com nossa equipe!

📧 **Email direto:** {self.config['contact_email']}
📱 **WhatsApp:** (48) 99931-4665

Aguarde um momento! 👤"""

    def handle_goodbye(self) -> str:
        """Despedida"""
        self.log_message("Despedida solicitada")
        return f"""👋 Obrigado por conhecer o WhatsAtende!

Foi um prazer demonstrar nossa solução para você.

📧 **Contato:** {self.config['contact_email']}
📱 **WhatsApp:** (48) 99931-4665
🌐 **WhatsApp direto:** https://w.app/q8drou

Estamos à disposição para implementar o WhatsAtende em seu negócio!

Até breve! 😊"""

    def get_funcionalidades_text(self) -> str:
        return """🔧 **Principais Funcionalidades do WhatsAtende:**

✅ **Atendimento Automatizado 24/7**
   • Respostas instantâneas a qualquer hora
   • Nunca mais perca clientes por demora

✅ **Consulta de Serviços e Produtos**
   • Informações completas automatizadas
   • Catálogo sempre atualizado

✅ **Sistema de Agendamento Inteligente**
   • Marcação automática de horários
   • Sincronização com sua agenda

✅ **Envio Automático de Documentos**
   • Listas, tabelas e arquivos
   • Organização profissional

✅ **Transferência Inteligente**
   • Passa para humano quando necessário
   • Contexto preservado na transferência"""

    def get_antes_text(self) -> str:
        return """😰 **Problemas ANTES do WhatsAtende:**

❌ **Tempo perdido com repetições**
   • Mesmas perguntas dezenas de vezes por dia
   • Equipe sobrecarregada com tarefas básicas

❌ **Clientes abandonando por demora**
   • Espera de horas para respostas simples
   • Perda de vendas por falta de agilidade

❌ **Trabalho fora do horário**
   • Pressão para responder à noite/fins de semana
   • Equipe sobrecarregada e estressada

❌ **Custos com APIs e mensalidades**
   • Soluções em nuvem caras
   • Dependência de terceiros"""

    def get_depois_text(self) -> str:
        return """🚀 **Benefícios DEPOIS do WhatsAtende:**

✅ **Produtividade multiplicada**
   • Equipe focada em vendas e negociação
   • Fim das perguntas repetitivas

✅ **Atendimento 24 horas automático**
   • Clientes atendidos mesmo de madrugada
   • Zero perda de oportunidades

✅ **Controle total e local**
   • Funciona no seu computador
   • Sem dependência de internet para funcionar

✅ **Economia real**
   • Sem mensalidades abusivas
   • Investimento único com retorno garantido

💎 **Nossos Planos e Valores:**

**💎 LICENÇA ÚNICA - R$ 1.289**
• Instalação completa no seu PC
• Uso vitalício sem mensalidades
• Suporte técnico inicial incluído
• Todas as funcionalidades liberadas

**🚀 PLANO PREMIUM - R$ 689 + R$ 89/mês**
• Instalação + configuração personalizada
• Atualizações automáticas mensais
• Backup em nuvem seguro
• Suporte técnico ilimitado

**🎯 AMBOS OS PLANOS INCLUEM:**
• Treinamento completo da equipe
• Configuração personalizada para seu negócio
• Garantia de 30 dias
• Suporte durante implementação"""


def main():
    """Função principal para teste do bot"""
    bot = WhatsAtendeBot()

    print("=" * 60)
    print("🤖 WHATSATENDE DEMO BOT - VERSÃO STATELESS")
    print("=" * 60)
    print("📱 Número: (48) 99931-4665")
    print("📧 Email: expertdigitalnovo@gmail.com")
    print("🔗 WhatsApp: https://w.app/q8drou")
    print("📧 Digite 'sair' para encerrar")
    print("=" * 60)

    test_user = "demo_user"

    print("\n🎯 SIMULAÇÃO DE CONVERSA STATELESS...")
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