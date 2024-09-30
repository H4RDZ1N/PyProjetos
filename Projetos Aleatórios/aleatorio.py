soma = 1 + 1
multiplicacao = 4 * 4
divisao = 30 / 4
potencia = 7 ** 2

print("soma", soma)
print("multiplicacao", multiplicacao)
print("divisao", divisao)
print("potencia", potencia)

nome = (input("Digite seu nome: ") )
idade = int (input("Digite sua idade: ") )
peso = float (input("Digite seu peso: ") )

print(nome)
print(idade)
print(peso)

salario = float(input("Informe seu salário: "))

if salario <=3000:
    print("Programador Junior")
elif salario > 3000 and  salario <= 6000:
    print ("Programador Pleno")
elif salario > 6000 and salario <= 15000:
    print ("Programador Senior")
else:
    print("Gerente de Projetos")


lista_numeros = [1,2,3]

lista_numeros[0] = 5

print(lista_numeros[0])
print(lista_numeros[1])
print(lista_numeros[2])