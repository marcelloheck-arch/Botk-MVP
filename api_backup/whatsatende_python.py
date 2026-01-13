"""
WhatsAtende Demo Bot - Versão COMPLETAMENTE STATELESS para Vercel
Cada mensagem é processada de forma totalmente independente
"""

import datetime
import re

class WhatsAtendeBot:
    def __init__(self):
        # Apenas configurações básicas, sem sessions
        self.config = {
            'bot_number': '48999314665',
            'contact_email': 'expertdigitalnovo@gmail.com'
        }

    def log_message(self, message: str):
        """Sistema de logs"""
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"[{timestamp}] [WHATSATENDE] {message}")

    def is_greeting(self, message: str) -> bool:
        """Verifica se é uma saudação comum"""
        greetings = [
            'ola', 'olá', 'oi', 'hello', 'hi', 'hey', 'hola',
            'bom dia', 'boa tarde', 'boa noite', 'opa', 'eai', 'e ai',
            'teste', 'testando', 'test', 'iniciar', 'começar', 'start'
        ]
        msg_lower = message.lower().strip()
        return any(greeting == msg_lower or greeting in msg_lower for greeting in greetings)

    def validate_name(self, name: str) -> bool:
        """Valida se pode ser um nome (não é saudação nem tem números)"""
        if len(name.strip()) < 2:
            return False
        if re.search(r'\d{8,}', name):
            return False
        if self.is_greeting(name):
            return False
        return True

    def validate_phone(self, phone: str) -> bool:
        """Valida formato de telefone"""
        clean_phone = re.sub(r'[^\d]', '', phone)
        return len(clean_phone) >= 10 and len(clean_phone) <= 11

    def is_menu_option(self, message: str) -> bool:
        """Verifica se é opção de menu"""
        return message.strip() in ['1', '2', '3', '4', '5']

    def looks_like_phone(self, message: str) -> bool:
        """Verifica se parece ser um telefone"""
        return bool(re.search(r'\d{8,}', message))

    def process_message(self, user_id: str, message: str) -> str:
        """
        Processa mensagem - VERSÃO COMPLETAMENTE STATELESS
        Sem qualquer persistência de estado entre mensagens
        """
        message = message.strip()
        self.log_message(f"Processando: '{message}'")

        # 1. Opções de menu (1-5)
        if self.is_menu_option(message):
            return self.handle_menu_option(message)

        # 2. Telefone (contém 8+ dígitos)
        elif self.looks_like_phone(message):
            if self.validate_phone(message):
                return f"""✅ Telefone registrado: {message}

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

        # 3. Nome válido (sem números longos)  
        elif self.validate_name(message):
            name = message.strip().title()
            return f"""👋 Olá {name}! Sou o assistente Virtual WhatsAtende!

É um prazer conhecê-lo! Para continuarmos, preciso do seu telefone:

**Digite:** Seu número com DDD
**Exemplo:** 48 99999-9999"""

        # 4. Qualquer outra coisa (saudações, etc.)
        else:
            return """🤖 Olá! Bem-vindo ao **WhatsAtende Demo**!

Sou seu assistente virtual e vou demonstrar como podemos revolucionar o atendimento do seu negócio!

**Para começar, digite seu nome:**"""

    def handle_menu_option(self, option: str) -> str:
        """Processa opções do menu principal"""
        if option == "1":
            return f"""{self.get_funcionalidades_text()}

{self.get_continue_options()}"""
        
        elif option == "2":
            return f"""{self.get_antes_text()}

{self.get_continue_options()}"""
        
        elif option == "3":
            return f"""{self.get_depois_text()}

{self.get_continue_options()}"""
        
        elif option == "4":
            return """🔄 **Transferindo para atendente humano...**

Em instantes nossa equipe entrará em contato!

📞 **Contatos diretos:**
📧 Email: expertdigitalnovo@gmail.com
📱 WhatsApp: (48) 99931-4665
🔗 Link direto: https://w.app/q8drou

Aguarde nossa chamada! 👨‍💼"""
        
        elif option == "5":
            return """👋 **Obrigado por conhecer o WhatsAtende!**

Foi um prazer demonstrar nossa solução!

📞 **Entre em contato:**
📧 expertdigitalnovo@gmail.com  
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

    def get_continue_options(self) -> str:
        """Opções para continuar navegando"""
        return"""**Continue explorando:**

**1️⃣ - Principais Funcionalidades**
**2️⃣ - Antes do WhatsAtende**
**3️⃣ - Depois do WhatsAtende**  
**4️⃣ - Falar com o atendente**
**5️⃣ - Finalizar atendimento**

**Digite o número da opção:**"""

    def get_funcionalidades_text(self) -> str:
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

    def get_antes_text(self) -> str:
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

    def get_depois_text(self) -> str:
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


def main():
    """Teste do bot stateless"""
    bot = WhatsAtendeBot()
    
    print("🤖 WHATSATENDE - VERSÃO STATELESS PARA VERCEL")
    print("=" * 60)
    
    while True:
        msg = input("\n👤 Digite: ").strip()
        if msg.lower() in ['sair', 'quit', 'exit']:
            break
            
        response = bot.process_message('test', msg)
        print(f"\n🤖 {response}")
        print("-" * 60)


if __name__ == "__main__":
    main()