import sys
sys.path.append('api')
from whatsatende_python import WhatsAtendeBot

bot = WhatsAtendeBot()
cases = ['ola', 'oi', 'opa', 'bom dia', 'João', 'a', 'teste']

print('🎯 TESTE COMPORTAMENTOS ATUAIS:')
for case in cases:
    print(f'\n"{case}": ', end='')
    response = bot.process_message('test', case)
    if 'Digite seu nome' in response:
        print('✅ Pediu nome (correto)')
    elif 'telefone' in response.lower():
        print('⚠️ Aceitou como nome')
    elif 'opção' in response.lower():
        print('🔍 Mostrou menu')
    else:
        print('❓ Outra resposta')