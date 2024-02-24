import random


print("**********************************")
print ("****Bem-vindo ao jogo da forca***")
print("**********************************")

palavras = ["uva", "abacaxi", "acerola", "banana", "mamao", "melancia"]

numero = random.randrange(0, len(palavras))
palavra_secreta = palavras[numero].upper()

letras_acertada = ["_" for letra in palavra_secreta]

#OU LETRAS_ACERTADA = ["_" FOR LETRA IN PALAVRA_SECRETA]

enforcou = False
acertou = False
erros = 0

print(palavra_secreta)
print(letras_acertada)

while(not enforcou and not acertou):

    chute = input("Qual a letra? ")
    chute = chute.strip().upper()

    if(chute in palavra_secreta):
        index = 0
        for letra in palavra_secreta:
            if(chute == letra):
                letras_acertada[index] = letra
                index += 1
    else:
        erros += 1
    enforcou = erros == 6
    acertou = "_" not in letras_acertada

    print(letras_acertada)

if(acertou):
    print("Você ganhou!")
else:
    print("VocÊ perdeu!")