# Solicite ao usuário para informar um número inteiro positivo e, em seguida,
# conte quantos números ímpares existem entre 1 e o número informado.


numero_int = int(input('Informe um número positivo: '))
qtd_impares = 0

for n in range(1, numero_int, 2):
    qtd_impares += 1

print(f'Há {qtd_impares} número(s) ímpar(es) entre 1 e {numero_int}.')
