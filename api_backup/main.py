"""
Vercel Entry Point para botK
Este arquivo garante que o Vercel encontre a aplicação Flask corretamente
"""

# Importa a aplicação Flask do módulo principal
from index import app

# Esta linha é necessária para o Vercel
application = app

if __name__ == "__main__":
    app.run(debug=True)