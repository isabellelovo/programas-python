# Peça ao usuário para inserir três números e verifique se eles estão em ordem
# crescente (do menor para o maior). Informe ao usuário se a sequência está
# ordenada corretamente ou não.


def inserir_numero(n):
    return float(input(f'Insira o {n}º número: '))


print('Verifique se a sua sequência está ordenada!')

numero1 = inserir_numero(1)
numero2 = inserir_numero(2)
numero3 = inserir_numero(3)

resultado = 'A sequência está ordenada corretamente.' if numero1 < numero2 < numero3 else 'A sequência não está ordenada corretamente.'
print(resultado)
