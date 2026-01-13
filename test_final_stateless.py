import sys
sys.path.append('api')
from whatsatende_python import WhatsAtendeBot

bot = WhatsAtendeBot()
print('🧪 TESTE VERSÃO STATELESS FINAL:')
print('=' * 50)

# Testar os casos problemáticos que você mencionou
test_cases = [
    ('ola', 'Saudação simples'),
    ('oi', 'Saudação curta'),
    ('opa', 'Interjeição'), 
    ('bom dia', 'Saudação composta'),
    ('teste', 'Palavra teste'),
    ('João', 'Nome próprio'),
    ('Maria Silva', 'Nome completo'),
    ('48999887766', 'Telefone'),
    ('1', 'Opção menu'),
    ('a', 'Letra única'),
]

for msg, desc in test_cases:
    print(f'\n📝 "{msg}" ({desc}):')
    # Simular requisição independente no Vercel
    response = bot.process_message('user_vercel', msg)
    print(f'🤖 {response[:100]}...\n{"-"*50}')
    
print('\n✅ Teste stateless concluído!')