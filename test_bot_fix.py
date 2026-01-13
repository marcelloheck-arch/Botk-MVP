#!/usr/bin/env python3
"""
Teste específico para verificar a correção do bot
"""

import sys
import os

# Adiciona o diretório api ao path
current_dir = os.path.dirname(os.path.abspath(__file__))
api_dir = os.path.join(current_dir, 'api')
sys.path.insert(0, api_dir)

from whatsatende_python import WhatsAtendeBot

def test_bot_initial_logic():
    """Testa se o bot aceita qualquer entrada inicial"""
    
    print("🧪 TESTE ESPECÍFICO DA CORREÇÃO DO BOT")
    print("=" * 50)
    
    # Teste 1: Nome válido como primeira entrada
    print("\n📝 TESTE 1: Entrada 'João' (válida)")
    bot1 = WhatsAtendeBot()
    response1 = bot1.process_message('test_joao', 'João')
    print("Resposta:", response1[:100] + "...")
    
    # Verificar se aceitou como nome
    session1 = bot1.sessions.get('test_joao', {})
    print("Nome capturado:", session1.get('name', 'NÃO CAPTURADO'))
    print("Estado atual:", session1.get('state', 'DESCONHECIDO'))
    
    success1 = session1.get('name') == 'João' and session1.get('state') == 'collecting_phone'
    print("✅ SUCESSO" if success1 else "❌ FALHOU")
    
    # Teste 2: Nome válido diferente
    print("\n📝 TESTE 2: Entrada 'Maria' (válida)")  
    bot2 = WhatsAtendeBot()
    response2 = bot2.process_message('test_maria', 'Maria')
    print("Resposta:", response2[:100] + "...")
    
    session2 = bot2.sessions.get('test_maria', {})
    print("Nome capturado:", session2.get('name', 'NÃO CAPTURADO'))
    print("Estado atual:", session2.get('state', 'DESCONHECIDO'))
    
    success2 = session2.get('name') == 'Maria' and session2.get('state') == 'collecting_phone'
    print("✅ SUCESSO" if success2 else "❌ FALHOU")
    
    # Teste 3: Entrada inválida (muito curta)
    print("\n📝 TESTE 3: Entrada 'a' (inválida)")
    bot3 = WhatsAtendeBot()
    response3 = bot3.process_message('test_a', 'a')
    print("Resposta:", response3[:100] + "...")
    
    session3 = bot3.sessions.get('test_a', {})
    print("Nome capturado:", session3.get('name', 'NÃO CAPTURADO'))
    print("Estado atual:", session3.get('state', 'DESCONHECIDO'))
    
    success3 = session3.get('name') == '' and session3.get('state') == 'collecting_name'
    print("✅ SUCESSO" if success3 else "❌ FALHOU")
    
    # Resultado final
    print("\n" + "=" * 50)
    all_success = success1 and success2 and success3
    if all_success:
        print("🎉 TODOS OS TESTES PASSARAM! Bot corrigido com sucesso!")
    else:
        print("❌ ALGUNS TESTES FALHARAM. Correção não foi aplicada corretamente.")
        print(f"Teste 1 (João): {'✅' if success1 else '❌'}")
        print(f"Teste 2 (Maria): {'✅' if success2 else '❌'}")
        print(f"Teste 3 (a): {'✅' if success3 else '❌'}")
    
    return all_success

if __name__ == "__main__":
    test_bot_initial_logic()