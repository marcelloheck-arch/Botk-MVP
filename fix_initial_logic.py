# Patch para corrigir a lógica inicial do WhatsAtende Bot
# Vou substituir a função process_message e handle_initial_state

# PROBLEMA IDENTIFICADO:
# A função handle_initial_state ignora a mensagem inicial do usuário
# Isso causa o erro "Desculpe, não entendi" após o primeiro acesso

# SOLUÇÃO:
# Modificar handle_initial_state para processar a mensagem como nome se válida
# ou solicitar nome se inválida

def new_process_message(self, user_id: str, message: str) -> str:
    """Processa mensagem recebida e retorna resposta - VERSÃO CORRIGIDA"""
    session = self.get_session(user_id)
    message = message.strip()

    self.log_message(f"Mensagem de {user_id}: {message}")

    if session['state'] == self.states['INITIAL']:
        # CORREÇÃO: Processar a mensagem inicial como nome se válida
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
        # CORREÇÃO: Resetar para inicial em caso de erro
        session['state'] = self.states['INITIAL']
        return self.handle_initial_state(session, message)

def new_handle_initial_state(self, session: Dict, message: str = "") -> str:
    """Estado inicial - VERSÃO CORRIGIDA - aceita qualquer entrada"""
    
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
            return f"""Olá! Sou o assistente Virtual WhatsAtende! 😊

Vou precisar de um nome válido com pelo menos 2 caracteres.
Por favor, qual é o seu nome?"""
        else:  # Primeira vez
            return """Olá! Sou o assistente Virtual WhatsAtende! 😊

Para começarmos, qual é o seu nome?"""

print("Correção preparada! Agora vou aplicar no arquivo original...")