import re

print("🔧 Aplicando correção no WhatsAtende Bot...")

# Lê o arquivo original
with open('api/whatsatende_python.py', 'r', encoding='utf-8') as f:
    content = f.read()

# Correção 1: Modificar a chamada na process_message
print("📝 Corrigindo chamada da função...")
content = re.sub(
    r'return self\.handle_initial_state\(session\)',
    'return self.handle_initial_state(session, message)',
    content
)

# Correção 2: Substituir a assinatura da função handle_initial_state
print("🔄 Corrigindo assinatura da função...")
content = re.sub(
    r'def handle_initial_state\(self, session: Dict\) -> str:',
    'def handle_initial_state(self, session: Dict, message: str = "") -> str:',
    content
)

# Correção 3: Substituir o conteúdo da função handle_initial_state
print("⚡ Corrigindo lógica da função...")

old_body = '''"""Estado inicial - solicita nome"""
        session['state'] = self.states['COLLECTING_NAME']
        return """Olá! Sou o assistente Virtual WhatsAtende! 😊

Para começarmos, qual é o seu nome?"""'''

new_body = '''"""Estado inicial - aceita qualquer entrada para iniciar conversa"""
        
        # Se há mensagem e é um nome válido, usa como nome
        if message and self.validate_name(message):
            session['name'] = message.strip().title()
            session['state'] = self.states['COLLECTING_PHONE']
            self.log_message(f"Nome coletado diretamente: {session['name']}")
            return f"""Olá {session['name']}! Sou o assistente Virtual WhatsAtende! 😊

Agora, por favor, informe seu número de celular com DDD:"""
        
        # Se há mensagem mas não é nome válido, ou se não há mensagem
        else:
            session['state'] = self.states['COLLECTING_NAME']
            if message:  # Se digitou algo inválido como nome
                return """Olá! Sou o assistente Virtual WhatsAtende! 😊

Vou precisar de um nome válido com pelo menos 2 caracteres.
Por favor, qual é o seu nome?"""
            else:  # Primeira vez
                return """Olá! Sou o assistente Virtual WhatsAtende! 😊

Para começarmos, qual é o seu nome?"""'''

# Aplica a substituição
content = content.replace(old_body, new_body)

# Salva o arquivo corrigido
with open('api/whatsatende_python.py', 'w', encoding='utf-8') as f:
    f.write(content)

print("✅ Correção aplicada com sucesso!")
print("🎯 Bot agora aceita qualquer entrada para iniciar conversa!")