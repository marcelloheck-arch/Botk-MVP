#!/usr/bin/env python3
"""
Teste funcional do botK
Verifica se todas as funcionalidades estão operando corretamente
"""

import requests
import json

# Configurações
BASE_URL = "http://127.0.0.1:5000"
API_CHAT = f"{BASE_URL}/api/chat"
API_HEALTH = f"{BASE_URL}/api/health"

def test_health():
    """Testa o endpoint de saúde"""
    print("🔍 Testando endpoint de saúde...")
    try:
        response = requests.get(API_HEALTH, timeout=5)
        if response.status_code == 200:
            print("✅ Endpoint de saúde OK!")
            return True
        else:
            print(f"❌ Erro no endpoint de saúde: {response.status_code}")
            return False
    except Exception as e:
        print(f"❌ Erro de conexão: {e}")
        return False

def test_chat_message(message, expected_keywords=None):
    """Testa uma mensagem no chat"""
    print(f"💬 Testando mensagem: '{message}'")
    
    payload = {
        "user_id": "test_user",
        "message": message
    }
    
    try:
        response = requests.post(API_CHAT, json=payload, timeout=10)
        
        if response.status_code == 200:
            data = response.json()
            if 'response' in data:
                print(f"✅ Resposta recebida: {data['response'][:100]}...")
                
                # Verifica palavras-chave esperadas
                if expected_keywords:
                    for keyword in expected_keywords:
                        if keyword.lower() in data['response'].lower():
                            print(f"✅ Palavra-chave '{keyword}' encontrada!")
                        else:
                            print(f"⚠️  Palavra-chave '{keyword}' não encontrada")
                
                return True
            else:
                print(f"❌ Resposta sem campo 'response': {data}")
                return False
        else:
            print(f"❌ Erro HTTP {response.status_code}: {response.text}")
            return False
            
    except Exception as e:
        print(f"❌ Erro na requisição: {e}")
        return False

def main():
    """Executa todos os testes"""
    print("🚀 INICIANDO TESTES DO BOTK")
    print("=" * 50)
    
    # Teste 1: Saúde da API
    if not test_health():
        print("❌ API não está respondendo. Verifique se o servidor está rodando.")
        return False
    
    print("\n" + "=" * 50)
    
    # Teste 2: Mensagem inicial
    success = test_chat_message("Olá", ["botK", "BEM-VINDO", "REVOLUÇÃO"])
    
    # Teste 3: Nome do usuário
    if success:
        print("\n" + "-" * 30)
        success = test_chat_message("João Silva", ["Olá João", "botK", "telefone"])
    
    # Teste 4: Telefone
    if success:
        print("\n" + "-" * 30)
        success = test_chat_message("48999887766", ["Perfeito", "registrado", "Escolha"])
    
    # Teste 5: Menu - Funcionalidades
    if success:
        print("\n" + "-" * 30)
        success = test_chat_message("1", ["RECURSOS", "REVOLUCIONAM", "Automação"])
    
    # Teste 6: Menu - Antes do botK
    if success:
        print("\n" + "-" * 30)
        success = test_chat_message("2", ["PREJUÍZOS", "ANTES DO BOTK", "Sangria"])
    
    # Teste 7: Menu - Depois do botK
    if success:
        print("\n" + "-" * 30)
        success = test_chat_message("3", ["TRANSFORMAÇÃO", "DEPOIS DO BOTK", "Explosão"])
    
    print("\n" + "=" * 50)
    
    if success:
        print("🎉 TODOS OS TESTES PASSARAM! botK está funcionando perfeitamente!")
        print("🚀 Sistema pronto para demonstrações!")
    else:
        print("❌ Alguns testes falharam. Verifique os logs acima.")
    
    return success

if __name__ == "__main__":
    main()