import random

sorted_value = random.randint(0, 20)
entry_value = sorted_value - 1 #Deve ser diferente do valor sorteado

while (entry_value != sorted_value):
    entry_value = int(input("Digite um valor!\n"))

    if entry_value == sorted_value:
        print("Você acertou! :D")
        break

    heat = "Maior" if entry_value > sorted_value else "Menor"
    print("O valor " + str(entry_value) + " é " + str(heat) + "!\n")