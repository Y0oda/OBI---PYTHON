n, k = [int(x) for x in input().split()]

numeros = input().split()

lista_de_participantes = []

for numero in numeros:
    lista_de_participantes.append(int(numero))

lista_de_participantes = sorted(lista_de_participantes)

print(lista_de_participantes[n-k])