# Crie um programa que leia um número e calcule o fatorial desse número. O
# fatorial de um número é o produto de todos os números inteiros de 1 até ele.


print(4*'-', 'Calculadora de Fatorial', 4*'-')

numero = int(input('Digite um número: '))
resultado = 1

for n in range(2, numero+1):
    resultado *= n

mensagem = ''

for n in range(numero, 0, -1):
    if n == 1:
        mensagem += f'{n} = {resultado}'
    else:
        mensagem += f'{n} * '

print(mensagem)
