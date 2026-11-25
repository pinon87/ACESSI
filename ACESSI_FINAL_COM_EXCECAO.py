DIRECOES = ("em frente", "direita", "esquerda", "subir", "descer")
lojas = []
DESTINOS_INICIAIS = [
    {"empresa": "Shopping Recife", "nome": "Perfumaria Queen", "andar": "Terreo",
     "rota": "Siga em frente por 10 passos / Vire a direita / Siga em frente por 5 passos / Destino a esquerda"},
    {"empresa": "Shopping Recife", "nome": "C&A", "andar": "Terreo",
     "rota": "Siga em frente por 20 passos / Vire a esquerda / Siga em frente por 8 passos / Destino a direita"},
    {"empresa": "Shopping Recife", "nome": "Renner", "andar": "1o andar",
     "rota": "Vire a direita / Siga ate o elevador / Suba ao primeiro andar / Vire a esquerda / Destino a frente"},
    {"empresa": "Shopping Recife", "nome": "Lojas Americanas", "andar": "Terreo",
     "rota": "Siga em frente por 12 passos / Vire a esquerda / Siga em frente por 6 passos / Destino a direita"},
    {"empresa": "Shopping Recife", "nome": "Banheiro", "andar": "Terreo",
     "rota": "Siga em frente por 8 passos / Vire a direita / Siga em frente por 4 passos / Destino a esquerda"}
]

def ler(arquivo):
    open(arquivo, "a", encoding="utf-8").close()
    dados = []
    with open(arquivo, "r", encoding="utf-8") as f:
        for linha in f:
            if linha.strip() != "":
                dados.append(linha.strip().split("|"))
    return dados

def salvar_lojas():
    with open("lojas.txt", "w", encoding="utf-8") as f:
        for loja in lojas:
            f.write(loja["empresa"] + "|" + loja["nome"] + "|" +
                    loja["andar"] + "|" + loja["rota"] + "\n")

def preparar_demonstracao():
    if len(ler("acessi_carga_completa_v2.txt")) == 0: 
        for destino in DESTINOS_INICIAIS:
            existe = False
            for loja in lojas:
                if (loja["nome"].lower() == destino["nome"].lower()
                        and loja["empresa"].lower() == destino["empresa"].lower()):
                    existe = True
            if not existe:
                lojas.append(destino)
        salvar_lojas()
        gestor_existe = False
        for pessoa in ler("cadastros.txt"):
            if pessoa[0] == "G" and pessoa[2].lower() == "gestor@exemplo.com":
                gestor_existe = True
        if not gestor_existe:
            with open("cadastros.txt", "a", encoding="utf-8") as f:
                f.write("G|Gestor Acessi|gestor@exemplo.com|Shopping Recife\n")
        with open("acessi_carga_completa_v2.txt", "w", encoding="utf-8") as f:
            f.write("ok\n")

def cadastrar(tipo):
    nome = input("Nome: ")
    email = input("E-mail: ")
    empresa = ""
    if tipo == "G":
        empresa = input("Estabelecimento onde trabalha: ")
    for pessoa in ler("cadastros.txt"):
        if pessoa[0] == tipo and pessoa[2] == email:
            print("E-mail ja cadastrado.")
            return
    with open("cadastros.txt", "a", encoding="utf-8") as f:
        f.write(tipo + "|" + nome + "|" + email + "|" + empresa + "\n")
    print("Cadastro realizado!")

def escolher_loja(empresa):
    opcoes = []
    for loja in lojas:
        if empresa == "" or loja["empresa"].lower() == empresa.lower():
            opcoes.append(loja)
    if len(opcoes) == 0:
        print("Nenhuma loja cadastrada.")
        return None
    for i in range(len(opcoes)):
        print(i + 1, "-", opcoes[i]["nome"], "-", opcoes[i]["empresa"],
              "- andar", opcoes[i]["andar"])
    numero = input("Numero da loja: ")
    try:
        numero = int(numero)
    except ValueError:
        print("Erro! Digite apenas numeros.")
        return None
    if 1 <= numero <= len(opcoes):
        return opcoes[numero - 1]
    print("Opcao invalida.")
    return None

def preencher_loja(loja):
    loja["nome"] = input("Nome da loja: ")
    loja["andar"] = input("Andar: ")
    print("Direcoes que voce pode usar:", DIRECOES)
    print("Exemplo: Siga em frente por 15 passos / Vire a direita")
    loja["rota"] = input("Escreva a rota, separando passos com /: ")

def menu_usuario():
    if len(lojas) == 0:
        print("\nNenhuma loja cadastrada.")
        print("Peca ao gestor para cadastrar uma loja primeiro.")
        return
    while True:
        print("\n1 - Pedir rota | 0 - Voltar")
        opcao = input("Opcao: ")
        if opcao == "0":
            return
        elif opcao == "1":
            loja = escolher_loja("")
            if loja is not None:
                print("\nROTA SIMULADA (nao e um caminho real)")
                print("Partida: entrada ficticia do Shopping Recife")
                print("Rota para", loja["nome"], "- andar", loja["andar"])
                for passo in loja["rota"].split("/"):
                    print("-", passo.strip())
                chegou = input("Voce chegou ao destino? (s/n): ")
                if chegou.lower() == "s":
                    print("Voce chegou ao seu destino!")
                    with open("acessos.txt", "a", encoding="utf-8") as f:
                        f.write(HOJE + "|" + loja["empresa"] + "|" + loja["nome"] + "\n")
        else:
            print("Opcao invalida.")

def relatorio(empresa):
    contagem = {}
    for acesso in ler("acessos.txt"):
        if acesso[0] == HOJE and acesso[1].lower() == empresa.lower():
            nome_loja = acesso[2]
            if nome_loja not in contagem:
                contagem[nome_loja] = 0
            contagem[nome_loja] += 1
    print("\nAcessos de", HOJE, "-", empresa)
    if len(contagem) == 0:
        print("Nenhum acesso registrado hoje.")
    for nome_loja in contagem:
        print(nome_loja, ":", contagem[nome_loja], "acesso(s)")

def menu_gestor(empresa):
    while True:
        print("\n1 - Cadastrar loja | 2 - Ver lojas | 3 - Alterar loja")
        print("4 - Excluir loja | 5 - Acessos de hoje | 0 - Voltar")
        opcao = input("Opcao: ")
        if opcao == "0":
            return
        elif opcao == "1":
            loja = {"empresa": empresa, "nome": "", "andar": "", "rota": ""}
            preencher_loja(loja)
            lojas.append(loja)
            salvar_lojas()
            print("Loja cadastrada!")
        elif opcao == "2":
            for loja in lojas:
                if loja["empresa"].lower() == empresa.lower():
                    print(loja["nome"], "- andar", loja["andar"], "-", loja["rota"])
        elif opcao == "3":
            loja = escolher_loja(empresa)
            if loja is not None:
                preencher_loja(loja)
                salvar_lojas()
                print("Loja atualizada!")
        elif opcao == "4":
            loja = escolher_loja(empresa)
            if loja is not None:
                lojas.remove(loja)
                salvar_lojas()
                print("Loja excluida!")
        elif opcao == "5":
            relatorio(empresa)
        else:
            print("Opcao invalida.")

def entrar(tipo):
    email = input("Digite seu e-mail: ")
    for pessoa in ler("cadastros.txt"):
        if pessoa[0] == tipo and pessoa[2] == email:
            print("Bem-vindo(a),", pessoa[1])
            if tipo == "U":
                menu_usuario()
            else:
                menu_gestor(pessoa[3])
            return
    print("Cadastro nao encontrado.")
for dados in ler("lojas.txt"):
    if len(dados) == 4:
        lojas.append({"empresa": dados[0], "nome": dados[1],
                      "andar": dados[2], "rota": dados[3]})
preparar_demonstracao()
HOJE = input("Data de hoje (dia/mes/ano): ")
while True:
    print("\n=== ACESSI ===")
    print("1 - Cadastrar usuario | 2 - Entrar como usuario")
    print("3 - Cadastrar gestor  | 4 - Entrar como gestor | 0 - Sair")
    opcao = input("Opcao: ")
    if opcao == "1":
        cadastrar("U")
    elif opcao == "2":
        entrar("U")
    elif opcao == "3":
        cadastrar("G")
    elif opcao == "4":
        entrar("G")
    elif opcao == "0":
        print("Ate logo!")
        break
    else:
        print("Opcao invalida.")
