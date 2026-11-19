# ACESSI

**Mais autonomia e mais segurança pra quem precisa**

Plataforma de navegação interna que conecta visitantes e gestores de estabelecimentos por meio de rotas passo a passo dentro de ambientes públicos fechados, como shoppings.

Este repositório contém o desenvolvimento inicial do **Acessi** em Python puro, aplicando conceitos de Fundamentos de Programação, persistência em arquivos `.txt`, controle de versão com Git e colaboração no GitHub.

*Projeto acadêmico em desenvolvimento. O escopo atual contempla o fluxo de usuários gerais e gestores de estabelecimentos para validação da lógica de navegação.*

---

## Sobre o projeto

O **Acessi** nasceu como um projeto acadêmico com o propósito de solucionar a dificuldade de locomoção em ambientes públicos internos sem sinalização adequada — pensando originalmente na autonomia de pessoas cegas.

Nesta primeira versão do sistema, o foco está na validação da estrutura de cadastro, criação de rotas internas e registro de acessos, atendendo dois perfis: **usuários gerais** (que buscam chegar a uma loja ou ponto específico) e **gestores de locais** (inicialmente shoppings, responsáveis por mapear e gerenciar os trajetos).

---

## Objetivos

- Facilitar a localização de lojas e pontos internos em estabelecimentos fechados.
- Padronizar instruções de deslocamento em passos simples e diretos.
- Oferecer aos gestores um painel para cadastrar, atualizar e monitorar rotas e acessos.
- Construir uma base lógica modular em Python que possa evoluir futuramente para recursos voltados a pessoas com deficiência visual.

---

##  Área do usuário — funcionalidades implementadas

- Cadastro e login por e-mail.
- Listagem das lojas disponíveis com identificação do estabelecimento e andar.
- Visualização da rota dividida passo a passo.
- Confirmação de chegada ao destino.
- Registro automático de acesso concluído na data atual.

---

##  Área do gestor — funcionalidades implementadas

- Cadastro e login vinculados ao estabelecimento (shopping) onde trabalha.
- Cadastro de novas lojas com andar e instruções de rota separadas por etapas.
- Consulta de todas as lojas e rotas cadastradas do seu estabelecimento.
- Atualização de nome, andar e trajeto de lojas existentes.
- Exclusão de lojas do sistema.
- Relatório diário de quantidade de acessos concluídos por loja.

---

##  Como a navegação funciona

1. O gestor cadastra o estabelecimento e registra as lojas com seus respectivos andares e rotas passo a passo.
2. O usuário realiza o cadastro e acessa o menu de navegação.
3. O usuário escolhe a loja de destino na lista disponível.
4. O sistema exibe o trajeto dividido em instruções sequenciais (ex.: *em frente, direita, esquerda, subir, descer*).
5. Ao finalizar o percurso, o usuário confirma a chegada e o sistema contabiliza o acesso para o relatório do gestor.

---

##  Acessibilidade e escopo atual

Embora a visão de longo prazo do **Acessi** seja guiar pessoas cegas em ambientes internos sem sinalização tátil ou sonora, esta etapa acadêmica prioriza o fluxo de **usuários gerais** e **gestores**.

A estruturação das rotas em comandos curtos e textuais (`DIRECOES`) já prepara a lógica do sistema para futuras integrações com leitores de tela, comandos de voz e feedback auditivo.

---

##  Tecnologias e ferramentas

| Tecnologia | Finalidade |
| :--- | :--- |
| **Python** | Lógica principal, estruturas de dados (listas, tuplas, dicionários) e menus no terminal |
| **Arquivos `.txt`** | Persistência simples dos dados (`cadastros.txt`, `lojas.txt` e `acessos.txt`) sem bibliotecas externas |
| **Git** | Controle de versão e histórico de alterações |
| **GitHub** | Hospedagem do código, organização de tarefas e trabalho em equipe |

---

##  Etapas de desenvolvimento

- [x] Definir a proposta e o recorte inicial do Acessi.
- [x] Implementar leitura e escrita de dados em arquivos `.txt`.
- [x] Implementar cadastro e autenticação de usuários e gestores.
- [x] Implementar CRUD completo de lojas e rotas para gestores.
- [x] Implementar visualização passo a passo de rotas e confirmação de chegada.
- [x] Implementar relatório diário de acessos por estabelecimento.
- [ ] Modularizar o código em arquivos separados (`menu`, `usuarios`, `lojas`, `arquivos`).
- [ ] Adicionar validações extras de entrada e tratamento de erros.
- [ ] Evoluir a interface e recursos de acessibilidade para pessoas com deficiência visual.

---

##  Execução

1. Certifique-se de ter o **Python 3** instalado na máquina.
2. Clone este repositório:
   ```bash
   git clone [https://github.com/seu-usuario/APP-ACESSI.git](https://github.com/seu-usuario/APP-ACESSI.git)
