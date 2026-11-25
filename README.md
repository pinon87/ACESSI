# Acessi - Sistema de Navegação Indoor

O **Acessi** é um protótipo de aplicativo em linha de comando (CLI) desenvolvido em Python para auxiliar pessoas com deficiência visual na navegação indoor (ambientes internos como shoppings, centros comerciais e edifícios). O sistema fornece rotas descritivas passo a passo a partir de pontos de referência e contagem de passos, além de oferecer um módulo administrativo para gestores de estabelecimentos.

Projeto desenvolvido como atividade acadêmica para a disciplina de **Fundamentos da Programação** (1º período do curso de Análise e Desenvolvimento de Sistemas - ADS).

---

## Funcionalidades

### Perfil Usuário
* **Cadastro e Login:** Criação de conta e acesso via e-mail.
* **Consulta de Rotas:** Seleção de lojas ou pontos de interesse cadastrados, exibindo o andar e o trajeto detalhado passo a passo (direções e quantidade de passos).
* **Confirmação de Chegada:** Registro de conclusão de trajeto para contabilização no relatório do estabelecimento.

### Perfil Gestor
* **Cadastro e Login:** Acesso administrativo vinculado a um estabelecimento específico.
* **Gerenciamento de Locais (CRUD):** Cadastro, listagem, edição e exclusão de lojas, andares e suas respectivas rotas.
* **Relatório de Acessos:** Consulta da quantidade de visitas concluídas por loja na data informada.

---

## Estrutura do Projeto

O repositório já inclui a base de dados pré-populada para fins de apresentação e avaliação imediata:

* `main.py`: Código-fonte principal contendo toda a lógica de menus, validações, persistência e geração de relatórios.
* `lojas.txt`: Base de dados pré-carregada com cinco destinos de exemplo no **Shopping Recife** (Perfumaria Queen, C&A, Renner, Lojas Americanas e Banheiro), separados por `|`[cite: 4].
* `cadastros.txt`: Base de dados pré-carregada com o registro do gestor de demonstração.
* `acessi_carga_completa_v2.txt`: Arquivo de controle interno que indica que a carga inicial de demonstração já foi realizada, evitando duplicações ao iniciar o programa[cite: 1, 2].
* `acessos.txt`: Arquivo criado automaticamente durante o uso para registrar o histórico de chegadas confirmadas pelos usuários.

---

## Pré-requisitos e Execução

1. Certifique-se de ter o **Python 3** instalado em sua máquina.
2. Clone este repositório ou baixe os arquivos:
   ```bash
   git clone [https://github.com/seu-usuario/acessi-navegacao-indoor.git](https://github.com/seu-usuario/acessi-navegacao-indoor.git)
   cd acessi-navegacao-indoor
