#Problema a se resolver: elabore um programa que leia 4 valores INTEIROS e retorne ao usuário a média simples.
#A função "int" no começo é pra converter toda a entrada para inteiro já que input retorna string.
#A função input() recebe como parâmetro uma string que será mostrada como auxílio ao usuário, geralmente o informando que tipo de dado o programa está aguardando receber.
# A função "\n" é para quebra de linhas, ou seja, o programa lerá a variável "num2" na linha de baixo.
num1= int(input("Insira a nota 1 \n"))
num2= int(input("Insira a nota 2 \n"))
num3= int(input("Insira a nota 3 \n"))
num4= int(input("Insira a nota 4 \n"))
media=float(num1+num2+num3+num4)/4
#Como o programa lerá números inteiros e a operação de divisão pode retornar decimais, é preciso converter o "int" para "float".
print("A média das NOTAS inseridas é: \n", "%.2f" % media) # A função "%.2f" seguida de "%" define quantas casas decimais serão apresentadas na tela