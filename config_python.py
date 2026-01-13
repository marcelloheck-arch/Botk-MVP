# Configurações do WhatsAtende Python
# Versão sem dependência do Node.js

# Informações do Bot
BOT_NUMBER = "48000000000"
CONTACT_EMAIL = "seuemail@seuemail.com"
SUPPORT_WHATSAPP = "48000000000"

# Configurações de Sessão
SESSION_TIMEOUT = 300  # 5 minutos em segundos
DEMO_MODE = True
ENABLE_LOGS = True

# Horário de funcionamento (demonstração - 24h)
BUSINESS_HOURS_START = "00:00"
BUSINESS_HOURS_END = "23:59"
BUSINESS_DAYS = [0, 1, 2, 3, 4, 5, 6]  # 0=Segunda, 6=Domingo

# Mensagens personalizadas
WELCOME_MESSAGE = "Olá! Sou o assistente Virtual WhatsAtende! 😊"
DEMO_MESSAGE = "Isso é um teste de demonstração. Escolha uma opção abaixo:"
TRANSFER_MESSAGE = "Transferindo para um atendente humano... Por favor, aguarde! 👤"
GOODBYE_MESSAGE = "Agradecemos muito pelo seu contato! 🙏"

# Configurações dos planos
PLAN_BASIC_PRICE = 1289
PLAN_PREMIUM_INSTALL = 689
PLAN_PREMIUM_MONTHLY = 89

# Configurações de Log
LOG_LEVEL = "INFO"
LOG_FORMAT = "[%(asctime)s] [WHATSATENDE] %(message)s"