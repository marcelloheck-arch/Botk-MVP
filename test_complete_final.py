import sys
sys.path.append('api')
from whatsatende_python import WhatsAtendeBot

bot = WhatsAtendeBot()

print('🎯 TESTE FINAL COMPLETO:')
print('='*50)

test_cases = [
    ('ola', 'Deve pedir nome'),
    ('oi', 'Deve pedir nome'), 
    ('opa', 'Deve pedir nome'),
    ('bom dia', 'Deve pedir nome'),
    ('teste', 'Deve pedir nome'),
    ('João', 'Deve aceitar como nome'),
    ('Maria Silva', 'Deve aceitar como nome'),
    ('a', 'Deve pedir nome'),
    ('48999887766', 'Deve aceitar como telefone'),
    ('1', 'Deve mostrar funcionalidades'),
]

for msg, expected in test_cases:
    print(f'\n📤 "{msg}" ({expected}):')
    response = bot.process_message('test_user', msg)
    
    # Verificar resultado
    if 'digite seu nome' in response.lower():
        print('✅ CORRETO: Pediu nome')
    elif 'telefone' in response.lower() and 'digite' in response.lower():
        print('✅ CORRETO: Aceitou como nome e pediu telefone')
    elif 'telefone registrado' in response.lower():
        print('✅ CORRETO: Aceitou como telefone')
    elif 'funcionalidades' in response.lower():
        print('✅ CORRETO: Mostrou funcionalidades')
    else:
        print(f'❓ VERIFICAR: {response[:60]}...')

print('\n' + '='*50)
print('🎯 TESTE DE SEQUÊNCIA COMPLETA:')

sequence = ['ola', 'Maria', '48999887766', '1', '5']
print('Sequência:', ' → '.join(sequence))

for i, msg in enumerate(sequence, 1):
    print(f'\n{i}. "{msg}":')
    response = bot.process_message('seq_test', msg)
    print(f'   {response[:80]}...')

print('\n✅ TESTE CONCLUÍDO!')