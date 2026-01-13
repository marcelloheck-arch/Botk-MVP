import sys
sys.path.append('api')
from whatsatende_python import WhatsAtendeBot

bot = WhatsAtendeBot()
print('🧪 TESTE VERSÃO SERVERLESS CORRIGIDA:')
print('=' * 50)

# Simular várias interações como se fossem requisições separadas no Vercel
test_messages = ['ola', 'oi', 'opa', 'teste', 'João', 'a', 'bom dia']

for i, msg in enumerate(test_messages):
    print(f'\n📝 TESTE {i+1}: "{msg}"')
    # Cada mensagem é processada independentemente (como no Vercel)
    response = bot.process_message('user_test', msg)
    print(f'🤖 Resposta: {response[:80]}...')
    
print('\n✅ Teste concluído!')