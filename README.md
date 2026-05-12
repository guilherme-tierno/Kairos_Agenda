## Kairos_Agenda

# Descrição do Problema
A falta de organização e consistência nos estudos é uma dificuldade comum entre estudantes. Muitos enfrentam problemas para manter uma rotina estruturada, acompanhar tarefas e visualizar seu progresso ao longo do tempo.
Essa desorganização pode resultar em baixo desempenho acadêmico, procrastinação e sobrecarga mental.
________________________________________

# Proposta de Solução
O Kairos_Agenda CLI é uma aplicação de linha de comando desenvolvida em Python que auxilia estudantes na organização de suas atividades de estudo.

A ferramenta permite registrar tarefas, acompanhar seu status (pendente ou completo) e manter um fluxo simples e consistente de organização.

A escolha por uma interface CLI garante leveza, rapidez e acessibilidade, sem depender de interfaces gráficas complexas.
________________________________________

# Público-Alvo
- Estudantes do ensino médio e superior
- Pessoas com dificuldade em manter rotina de estudos
- Autodidatas que buscam organização
- Usuários que preferem ferramentas simples e diretas
________________________________________

# Funcionalidades
- Adicionar tarefas de estudo
- Listar tarefas cadastradas
- Marcar tarefas como concluídas
- Visualizar status das tarefas (pendente/completo)
________________________________________

# Tecnologias Utilizadas
- Python 3.11
- Pytest (testes automatizados)
- Ruff (linting e análise estática)
- JSON (armazenamento local de dados)
- Git + GitHub
- GitHub Actions (CI/CD)
________________________________________

# Estrutura do Projeto

Kairos_Agenda/
├── src/
│   ├── main.py
│   ├── task_manager.py
│   └── storage.py
├── tests/
├── data/
├── README.md
├── requirements.txt
├── VERSION
└── .github/workflows/ci.yml
________________________________________

# Instalação
1. Clonar o repositório

git clone https://github.com/guilherme-tierno/Kairos_Agenda.git

cd Kairos_Agenda

2. Criar ambiente virtual

python -m venv venv

3. Ativar ambiente

Windows
- venv\Scripts\activate

Linux/Mac
- source venv/bin/activate

4. Instalar dependências
pip install -r requirements.txt
________________________________________

# Execução da Aplicação

- Adicionar tarefa
python src/main.py add "Estudar matemática"

- Listar tarefas
python src/main.py list

- Saída esperada:
0 - Estudar matemática [pendente]

- Marcar como concluída
python src/main.py done 0

-Saída atualizada:
0 - Estudar matemática [completo]
________________________________________

# Testes Automatizados

Para executar os testes:

python -m pytest

Os testes cobrem:
- Adição de tarefas
- Retorno da lista de tarefas
- Tratamento de índice inválido
________________________________________

Lint (Qualidade de Código)
Para verificar o código:

ruff check .
________________________________________

## Execução Online (GitHub Codespaces)

O projeto pode ser executado diretamente no GitHub Codespaces.

Passos:
1. Clique em "Code"
2. Vá em "Codespaces"
3. Clique em "Create codespace on main"
4. Execute:

```bash
pip install -r requirements.txt
python -m src.main list
________________________________________

# Integração Contínua (CI)
O projeto utiliza GitHub Actions para garantir qualidade contínua.

A cada push ou pull request, o sistema executa automaticamente:
- Instalação das dependências
- Análise estática (lint)
- Execução dos testes
________________________________________

# Versionamento
Este projeto segue o padrão de versionamento semântico:
MAJOR.MINOR.PATCH

Versão atual:
1.0.0
________________________________________

# Armazenamento de Dados
Os dados são armazenados localmente em um arquivo JSON:

data/tasks.json

O sistema possui tratamento para:
- Arquivos inexistentes
- Arquivos vazios
- JSON inválido
________________________________________

# Decisões de Design

- Uso de CLI para simplicidade e acessibilidade
- Uso de texto ("pendente" / "completo") em vez de símbolos, visando maior clareza
- Estrutura modular para facilitar manutenção
- Uso de testes automatizados para garantir confiabilidade
________________________________________

## Frases Motivacionais

O projeto consome a API pública ZenQuotes para fornecer frases motivacionais aos estudantes.

bash-
- python src/main.py quote

Nota importante:
- Durante os testes e após o projeto pronto mesmo após sucesso houveram alguns erros SSL / HTTPS ao tentar acessar a API.
- Foram utilizadas as API's: https://api.quotable.io/random e https://zenquotes.io/api/random.
- Em caso de erro constante tente modificar o arquivo "motivacional_api.py" com o conteudo do arquivo "teste_mot_api.txt"
________________________________________

Autor: Guilherme Ortega Tierno
RA: 22509351
________________________________________

Repositório
https://github.com/guilherme-tierno/Kairos_Agenda.git
