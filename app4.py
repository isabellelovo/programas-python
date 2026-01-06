# Solicite ao usuário para inserir um número inteiro e calcule quantos dígitos
# esse número possui.


numero = int(input('Digite um número inteiro: '))
qtd_digitos = len(str(numero))

print(f'Este número tem {qtd_digitos} dígito(s).')
