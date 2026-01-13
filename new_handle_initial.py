    def handle_initial_state(self, session: Dict, message: str = "") -> str:
        """Estado inicial - aceita qualquer entrada para iniciar conversa"""
        
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