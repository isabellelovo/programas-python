# Um número perfeito é um número que é igual à soma de seus divisores,
# excluindo ele mesmo. Crie um programa que verifique se um número
# informado pelo usuário é perfeito.


print(4*'-', 'Verifique se o Número é Perfeito', 4*'-')
numero = int(input('Digite um número: '))
soma_divisor = 0

for divisor in range(1, numero):
    if numero % divisor == 0:
        soma_divisor += divisor

print('Sim, este número é perfeito.') if soma_divisor == numero else print(
    'Não, este número não é perfeito.')
