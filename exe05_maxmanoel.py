
#EXE 005 - Crie uma variável chamada “adivinha” e defina o valor como 50. 
#Peça ao usuário para inserir um número. Embora o palpite não seja o mesmo que o valor do “adivinha”, diga a ele se o palpite é muito baixo ou muito alto e peça que ele dê outro palpite. 
#Se ele inserir o mesmo valor que “adivinha”, exiba a mensagem "Parabéns! Você acertou o número em {} tentativas!".


lista = []
num1 = int(input("Digite um número: "))
num2 = int(input("Digite um número: "))
soma1 = 50
soma2 = num1+num2

while (soma1) < 50:
    numero = int(input("palpite muito baixo: "))
soma2 = num1+num2+numero

if soma2 >= 50:
    print('papilte muito alto {}'.format(soma2))