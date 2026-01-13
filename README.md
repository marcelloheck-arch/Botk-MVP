# botK - Simulador de Chat WhatsApp

## Sobre o Projeto

Simulador de chat WhatsApp interativo para demonstração comercial de soluções de atendimento automatizado. O sistema oferece uma experiência completa onde leads podem testar o fluxo de automação em uma interface que simula o WhatsApp real.

###  *Objetivo*
- *Demo Comercial*: Apresentar capacidades de automação de atendimento
- *Experiência Completa*: Simular todo o fluxo de um atendimento real
- *Interface Web*: Demonstração através de navegador
- *Fluxo Interativo*: 5 etapas de conversação simulada

---

##  Funcionalidades

### *Interface Web Profissional*
-  Demonstração via navegador (localhost:5000)
-  Interface limpa e intuitiva
-  Chat em tempo real simulado
-  Design responsivo

### *Fluxo de Conversação Completo*
1. *Boas-vindas* - Recepção personalizada
2. *Identificação* - Coleta de dados do cliente
3. *Tipo de Serviço* - Seleção de categoria
4. *Menu Principal* - 3 opções de navegação
5. *Finalização* - Protocolo e confirmação

### *Sistema de Validação*
-  Validação de CPF com algoritmo oficial
-  Validação de formato de e-mail
-  Validação de número de telefone
-  Respostas em tempo real

---

##  Tecnologias Utilizadas

### *Backend*
- *Python 3.13.7*: Runtime principal
- *Flask*: Framework web para interface
- *HTML5/CSS3/JavaScript*: Interface frontend

### *Funcionalidades Técnicas*
-  Sistema de sessões para múltiplos usuários
-  Validações automáticas de dados
-  Interface web responsiva
-  Logging completo do sistema
-  Simulação de fluxo WhatsApp completo

---

##  Instalação e Configuração

### *1. Clone o Repositório*
git clone https://github.com/marcelloheck-arch/botK
cd botK

### *2. Configure o Ambiente Python*
# Instalar Flask (se necessário)
pip install flask

### *3. Execute a Aplicação*
# Iniciar o bot via interface web
python web_demo.py

### *4. Acesse a Interface*
- *URL*: http://localhost:5000
- *Navegador*: Chrome, Firefox, Edge, Safari

---

##  Como Usar a Demo

### *1. Inicialização*
- Execute python web_demo.py
- Acesse http://localhost:5000 no navegador
- Clique em Iniciar Conversa

### *2. Fluxo de Demonstração*
 Boas-vindas
 Digite qualquer mensagem para começar

 Identificação (Etapa 2/5)
 Nome completo
 CPF (validação automática)
 E-mail (validação de formato)
 Telefone

 Tipo de Serviço (Etapa 3/5)
 1 - Informações Gerais
 2 - Agendamento de Atendimento  
 3 - Suporte Técnico

 Menu Principal (Etapa 4/5)
 Opção específica baseada na escolha anterior

 Finalização (Etapa 5/5)
 Protocolo gerado + Resumo completo

### *3. Recursos da Demo*
- *Validação em Tempo Real*: CPF, e-mail e telefone
- *Navegação Intuitiva*: Menu numerado
- *Protocolo Único*: Geração automática
- *Sessão Completa*: Dados mantidos durante a conversa

---

## Estrutura do Projeto

botK/
├── index.html          # Simulador de chat WhatsApp (frontend)
├── api/index.py       # Backend Flask (lógica do bot)
├── config_python.py   # Configurações do sistema
├── README.md          # Documentação
└── package.json       # Configurações do projeto

### *Arquivos Principais*

#### *web_demo.py*
- Interface web completa
- Servidor Flask integrado
- HTML/CSS/JavaScript embutido
- Chat em tempo real

#### *api/index.py*
- Classe BotKProfessional principal
- Sistema de sessões e validações
- Lógica de fluxo conversacional
- Geração de protocolos únicos

#### *config_python.py*
- Configurações centralizadas
- Personalização de mensagens
- Parâmetros do sistema

---

##  Casos de Uso

### *Para Empresas*
- Demonstrar capacidades de automação
- Apresentar soluções de atendimento
- Simular fluxos personalizados
- Validar conceitos antes da implementação

### *Para Desenvolvedores*
- Base para projetos WhatsApp
- Exemplo de validações em Python
- Interface web integrada
- Sistema de sessões completo

### *Para Apresentações*
- Demo ao vivo para clientes
- Apresentações comerciais
- Validação de conceitos
- Prototipagem rápida

---

##  Personalização

### *Modificar Mensagens*
Edite o arquivo config_python.py:
MENSAGENS = {
    'boas_vindas': 'Sua mensagem personalizada...',
    'solicitar_nome': 'Personalize a solicitação...',
    # ... outras mensagens
}

### *Ajustar Validações*
No simulador de chat (index.html), modifique as funções:
- validar_cpf(): Algoritmo de validação de CPF
- validar_email(): Regex para formato de e-mail
- validar_telefone(): Padrão de telefone brasileiro

### *Personalizar Interface*
No arquivo web_demo.py, ajuste:
- Cores e estilos CSS
- Layout da interface
- Comportamento do chat

---

##  Contato e Suporte

### *Desenvolvedor*
- *Nome*: Marcelo Heck
- *GitHub*: [@marcelloheck-arch](https://github.com/marcelloheck-arch)
- *Repositório*: [botK](https://github.com/marcelloheck-arch/botK)

### *Contribuições*
- Fork o projeto
- Crie sua feature branch
- Commit suas mudanças
- Push para a branch
- Abra um Pull Request

---

##  Licença

Este projeto é uma demonstração comercial desenvolvida para showcases e apresentações de soluções de automação de atendimento.

*Desenvolvido com  para demonstrações comerciais*

---

##  Próximos Passos

- [ ] Integração com WhatsApp Business API
- [ ] Dashboard administrativo
- [ ] Relatórios de conversas
- [ ] Integração com CRM
- [ ] Múltiplos idiomas
- [ ] Webhook para notificações

*botK* - *Simulador de Chat WhatsApp para Demonstração*
