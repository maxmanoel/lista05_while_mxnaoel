#EXE 001 . - Faça um programa que leia os números digitados pelo usuario, a cada número digitado ele deve ser somado ao anterior digitado e a cada soma exibida na tela,
#  quando a soma for superior a 50 deve exibir a mensagem “ O total é... [total] ” e parar o programa

num1 = int(input("Digite um número: "))
num2 = int(input("Digite um número: "))
soma = num1+num2

while (soma) < 50:
    numero = int(input("Insira números maiores: "))
soma2 = num1+num2+numero
print("MAX MANOEL")
if soma2 >= 50:
            print('O total é {}'.format(soma2))