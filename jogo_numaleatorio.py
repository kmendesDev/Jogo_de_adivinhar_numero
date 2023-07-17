import os
import random
os.system("cls")
num_jog = ""
erros = 0
sorteado = random.randrange(0, 1000)
nome = input("Digite seu nome: ")
tentativas = []
print("O jogo consiste em adivinhar um número escolhido aleatoriamente pela IA de 0 a 1000 em até 11 tentativas")
os.system("pause")
os.system("cls")
while (sorteado != num_jog and erros < 11):
    num_jog = ""
    while (num_jog == "" or num_jog.isnumeric() == False):
        num_jog = input("Digite seu número: ")
    num_jog = int(num_jog)
    tentativas.append(num_jog)
    os.system('cls')
    print(str(len(tentativas))+" tentativas: ")
    print(tentativas)
    if (sorteado > num_jog):
        print("ERRO, o numero é maior")
    elif (sorteado < num_jog):
        print("ERRO, o numero é menor")
    erros += 1
if erros < 12 and num_jog == sorteado:
    print("Parabéns "+nome+", você acertou o número " +
          str(num_jog)+" em "+str(erros)+" tentativas.")
else:
    print("Você perdeu por errar 11 vezes. Mais sorte na próxima, " +
          nome+"\nO número aleatório era: "+str(sorteado))
os.system("pause")
