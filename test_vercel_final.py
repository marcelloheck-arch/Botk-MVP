import sys
sys.path.append('api')
from whatsatende_python import WhatsAtendeBot

bot = WhatsAtendeBot()
print('🎯 TESTE FINAL - VERSÃO STATELESS PARA VERCEL')
print('=' * 60)

# Casos que você mencionou que estavam falhando
problem_cases = ['ola', 'oi', 'opa', 'bom dia', 'teste', 'qualquer coisa']

print('\n📝 TESTANDO CASOS PROBLEMÁTICOS:')
for i, case in enumerate(problem_cases, 1):
    print(f'\n{i}. Entrada: "{case}"')
    response = bot.process_message('user', case)
    if 'Desculpe, não entendi' in response:
        print('❌ AINDA TEM ERRO!')
    elif 'Olá!' in response and 'WhatsAtende' in response:
        print('✅ FUNCIONOU! Reconheceu como início de conversa')
    else:
        print('⚠️  Resposta diferente:', response[:50] + '...')

print('\n' + '='*60)
print('🔍 TESTE DETALHADO COM SEQUÊNCIA NORMAL:')

sequence = [
    ('ola', 'Saudação inicial'),
    ('João', 'Nome após saudação'), 
    ('48999887766', 'Telefone após nome'),
    ('1', 'Opção menu funcionalidades'),
    ('5', 'Finalizar')
]

for msg, desc in sequence:
    print(f'\n📤 "{msg}" ({desc})')
    response = bot.process_message('seq_user', msg)
    print(f'📥 {response[:100]}...')

print('\n✅ TESTE CONCLUÍDO!')