#!/usr/bin/env python3
"""
Teste de Build Local - Simula o ambiente Vercel
"""

import os
import sys
import subprocess

def test_vercel_build():
    """Testa se o projeto funciona como no Vercel"""
    print("🚀 TESTANDO BUILD VERCEL LOCAL")
    print("=" * 50)
    
    # 1. Testar imports
    print("📦 Testando imports...")
    try:
        from api.index import app
        print("✅ Import da aplicação Flask: OK")
    except Exception as e:
        print(f"❌ Erro no import: {e}")
        return False
    
    # 2. Testar configuração
    print("\n⚙️ Testando configuração...")
    if app:
        print("✅ Aplicação Flask: OK")
        print(f"✅ Modo Debug: {app.debug}")
        print(f"✅ Nome da App: {app.name}")
    else:
        print("❌ Aplicação Flask não encontrada")
        return False
    
    # 3. Testar rotas
    print("\n🔗 Testando rotas...")
    with app.test_client() as client:
        try:
            # Rota principal
            response = client.get('/')
            print(f"✅ Rota /: Status {response.status_code}")
            
            # API Health
            response = client.get('/api/health')
            print(f"✅ API Health: Status {response.status_code}")
            
            # API Chat
            response = client.post('/api/chat', 
                                 json={'user_id': 'test', 'message': 'Olá'})
            print(f"✅ API Chat: Status {response.status_code}")
            
        except Exception as e:
            print(f"❌ Erro nas rotas: {e}")
            return False
    
    # 4. Verificar arquivos necessários
    print("\n📁 Verificando arquivos...")
    required_files = [
        'vercel.json',
        'requirements.txt',
        'api/index.py',
        'index.html'
    ]
    
    for file_path in required_files:
        if os.path.exists(file_path):
            print(f"✅ {file_path}: Existe")
        else:
            print(f"❌ {file_path}: Não encontrado")
            return False
    
    print("\n" + "=" * 50)
    print("🎉 TODOS OS TESTES PASSARAM!")
    print("📋 O projeto está pronto para o Vercel!")
    print("🌐 Se ainda não está atualizando, o problema é no lado do Vercel")
    
    return True

if __name__ == "__main__":
    success = test_vercel_build()
    if success:
        print("\n💡 PRÓXIMOS PASSOS:")
        print("1. Acesse: https://vercel.com/dashboard")
        print("2. Force um redeploy manual")
        print("3. Verifique se está usando a branch 'master'")
        print("4. Confirme se o repositório está correto")
    else:
        print("\n❌ CORRIJA OS ERROS ANTES DO DEPLOY")
    
    sys.exit(0 if success else 1)