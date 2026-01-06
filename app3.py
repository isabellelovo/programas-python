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


# 7. Solicite ao usuário para inserir um número inteiro e calcule quantos dígitos
# esse número possui.


# numero = int(input('Digite um número inteiro: '))
# qtd_digitos = len(str(numero))

# print(f'Este número tem {qtd_digitos} dígito(s).')


# 8. Um número perfeito é um número que é igual à soma de seus divisores,
# excluindo ele mesmo. Crie um programa que verifique se um número
# informado pelo usuário é perfeito.


# print(4*'-', 'Verifique se o Número é Perfeito', 4*'-')
# numero = int(input('Digite um número: '))
# soma_divisor = 0

# for divisor in range(1, numero):
#     if numero % divisor == 0:
#         soma_divisor += divisor

# print('Sim, este número é perfeito.') if soma_divisor == numero else print(
#     'Não, este número não é perfeito.')
