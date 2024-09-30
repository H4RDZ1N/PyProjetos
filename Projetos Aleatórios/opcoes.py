#codigo sem funcao

fluxo_caixa = []

print("-----------")
print("@fluxo do caixa")
print("-----------")
print("1 - Adicionar Receita")
print("2 - Adicionar Despesa")
print("\n# Digite outro numero para encerrar #\n")

while True:
    opcao = int( input("Digite a opcao: ") )
    
    if opcao == 1:
        nome = input("Nome: ")
        valor = float(input("Valor: ") )
        fluxo_caixa.append({
            "nome": nome,
            "valor": valor
        })
    elif opcao == 2:
        nome = input("Nome: ")
        valor = float( input("Valor: ") )
        fluxo_caixa.append({
            "nome": nome,
            "valor": valor
        })
    else:
        break

# nota fiscal
total = 0
for fc in  fluxo_caixa:
    print("Nome: ", fc['nome'], ", Valor: R$", fc['valor'])
    total = total + fc['valor']

print("Saldo atual: R$", total)