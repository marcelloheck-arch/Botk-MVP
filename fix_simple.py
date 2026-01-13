import re

print("🔧 Aplicando correção SIMPLES no WhatsAtende Bot...")

# Lê o arquivo original
with open('api/whatsatende_python.py', 'r', encoding='utf-8') as f:
    content = f.read()

# Correção 1: Adicionar o parâmetro message na assinatura
print("📝 Adicionando parâmetro message...")
content = re.sub(
    r'def handle_initial_state\(self, session: Dict\) -> str:',
    'def handle_initial_state(self, session: Dict, message: str = "") -> str:',
    content
)

# Correção 2: Modificar a chamada na process_message
print("🔄 Corrigindo chamada da função...")
content = re.sub(
    r'return self\.handle_initial_state\(session\)',
    'return self.handle_initial_state(session, message)',
    content
)

# Correção 3: Modificar APENAS o conteúdo da função para aceitar qualquer entrada
print("⚡ Modificando lógica da função...")

# Encontrar e substituir o conteúdo da função
old_content = '''"""Estado inicial - solicita nome"""
        session['state'] = self.states['COLLECTING_NAME']
        return """Olá! Sou o assistente Virtual WhatsAtende! 😊

Para começarmos, qual é o seu nome?""""'''

new_content = '''"""Estado inicial - aceita qualquer entrada para iniciar conversa"""
        
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

Para começarmos, qual é o seu nome?""""'''

content = content.replace(old_content, new_content)

# Salva o arquivo corrigido
with open('api/whatsatende_python.py', 'w', encoding='utf-8') as f:
    f.write(content)

print("✅ Correção SIMPLES aplicada com sucesso!")
print("🎯 Bot agora deve aceitar qualquer entrada para iniciar!")