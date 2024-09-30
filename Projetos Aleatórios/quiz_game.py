print("Bem vindo ao meu quiz sobre computador! ")

playing = input("Você quer jogar? ")

if playing != "sim":
    quit()

print("Beleza! bora jogar então :)")

answer = input("O que significa CPU? ")
if answer == "Central Processing Unit":
    print('Correto!')
else:
    print("Errado!")