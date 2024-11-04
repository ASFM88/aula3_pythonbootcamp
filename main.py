### Exercício 1: Verificação de Qualidade de Dados

quantidade = int(input('Insira quantidade vendida: '))
preco = float(input('Insira preço de venda: '))

if quantidade > 0 and preco > 0:
    print('Dados válidos')
else:
    print('Dados inválidos')

### Exercício 2: Classificação de Dados de Sensor

temperatura = int(input('Insira uma temperatura: '))
if temperatura < 18:
    print('Temperatura Baixa')
elif 18 <= temperatura >= 26:
    print('Temperatura Normal')
else:
    print('Temperatura Alta')

### Exercício 3: Filtragem de Logs por Severidade

log = {'timestamp': '2021-06-23 10:00:00', 'level': 'ERROR', 'message': 'Falha na conexão'}
if log['level'] == 'ERROR':
    print(log['message'])

### Exercício 4: Validação de Dados de Entrada

idade = int(input('Insira sua idade: '))
email = str(input('Insira o seu e-mail: '))

if not 18 <= idade <= 65:
    print('Idade fora do intervalo permitido')
elif '@' not in email or '.' not in email:
    print('Email inválido')
else:
    print('Dados válidos')

### Exercício 5: Detecção de Anomalias em Dados de Transações

transacao = {'valor': 12000, 'hora': 20}
if transacao['valor'] > 10000 or transacao['hora'] < 9 or transacao['hora'] > 18:
    print('Transação suspeita')
else:
    print('Transação normal')

### Exercício 6. Contagem de Palavras em Textos

texto = "a raposa marrom salta sobre o cachorro preguiçoso"
palavras = texto.split()
contagem_palavras = {}

for palavra in palavras:
    if palavra in contagem_palavras:
        contagem_palavras[palavra] += 1
    else:
        contagem_palavras[palavra] = 1

print(contagem_palavras)

### Exercício 7. Normalização de Dados

numeros = [10, 20, 30, 40, 50]
minimo = min(numeros)
maximo = max(numeros)
normalizados = [(x - minimo) / (maximo - minimo) for x in numeros]

print(normalizados)

### Exercício 8. Filtragem de Dados Faltantes

usuarios = [
    {"nome": "Alice", "email": "alice@example.com"},
    {"nome": "Bob", "email": ""},
    {"nome": "Carol", "email": "carol@example.com"}
]

usuarios_validos = [usuario for usuario in usuarios if usuario["email"]]

print(usuarios_validos)

### Exercício 9. Extração de Subconjuntos de Dados

numeros = range(1, 11)
pares = [x for x in numeros if x % 2 == 0]

print(pares)

### Exercício 10. Agregação de Dados por Categoria

vendas = [
    {"categoria": "eletrônicos", "valor": 1200},
    {"categoria": "livros", "valor": 200},
    {"categoria": "eletrônicos", "valor": 800}
]

total_por_categoria = {}
for venda in vendas:
    categoria = venda["categoria"]
    valor = venda["valor"]
    if categoria in total_por_categoria:
        total_por_categoria[categoria] += valor
    else:
        total_por_categoria[categoria] = valor

print(total_por_categoria)

### Exercícios com WHILE

### Exercício 11. Leitura de Dados até Flag

dados = []
entrada = ""
while entrada.lower() != "sair":
    entrada = input("Digite um valor (ou 'sair' para terminar): ")
    if entrada.lower() != "sair":
        dados.append(entrada)

print("Valores inseridos:", dados)

### Exercício 12. Validação de Entrada

numero = int(input("Digite um número entre 1 e 10: "))
while numero < 1 or numero > 10:
    print("Número fora do intervalo!")
    numero = int(input("Por favor, digite um número entre 1 e 10: "))

print("Número válido!")

### Exercício 13. Consumo de API Simulado

pagina_atual = 1
paginas_totais = 5  # Simulação, na prática, isso viria da API

while pagina_atual <= paginas_totais:
    print(f"Processando página {pagina_atual} de {paginas_totais}")
    # Aqui iria o código para processar os dados da página
    pagina_atual += 1

print("Todas as páginas foram processadas.")

### Exercício 14. Tentativas de Conexão

tentativas_maximas = 5
tentativa = 1

while tentativa <= tentativas_maximas:
    print(f"Tentativa {tentativa} de {tentativas_maximas}")
    # Simulação de uma tentativa de conexão
    # Aqui iria o código para tentar conectar
    if True:  # Suponha que a conexão foi bem-sucedida
        print("Conexão bem-sucedida!")
        break
    tentativa += 1
else:
    print("Falha ao conectar após várias tentativas.")

### Exercício 15. Processamento de Dados com Condição de Parada

itens = [1, 2, 3, "parar", 4, 5]

i = 0
while i < len(itens):
    if itens[i] == "parar":
        print("Parada encontrada, encerrando o processamento.")
        break
    # Processa o item
    print(f"Processando item: {itens[i]}")
    i += 1

### DESAFIO

# Inicializa as variáveis para o controle do loop
nome_valido = False
salario_valido = False
bonus_valido = False

# Loop para verificar o nome
while not nome_valido:
    try:
        nome = input("Digite seu nome: ")
        if len(nome) == 0:
            raise ValueError("O nome não pode estar vazio.")
        elif any(char.isdigit() for char in nome):
            raise ValueError("O nome não deve conter números.")
        else:
            print("Nome válido:", nome)
            nome_valido = True
    except ValueError as e:
        print(e)

# Loop para verificar o salário
while not salario_valido:
    try:
        salario = float(input("Digite o valor do seu salário: "))
        if salario < 0:
            print("Por favor, digite um valor positivo para o salário.")
        else:
            salario_valido = True
    except ValueError:
        print("Entrada inválida para o salário. Por favor, digite um número.")

# Loop para verificar o bônus
while not bonus_valido:
    try:
        bonus = float(input("Digite o valor do bônus recebido: "))
        if bonus < 0:
            print("Por favor, digite um valor positivo para o bônus.")
        else:
            bonus_valido = True
    except ValueError:
        print("Entrada inválida para o bônus. Por favor, digite um número.")

bonus_recebido = 1000 + salario * bonus  # Exemplo simples de cálculo de bônus

# Imprime as informações para o usuário
print(f"{nome}, seu salário é R${salario:.2f} e seu bônus final é R${bonus_recebido:.2f}.")
