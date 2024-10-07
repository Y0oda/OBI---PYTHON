p = int(input()) #pão -> 1 ponto
d = int(input()) #doce -> 2 pontos
b = int(input()) #bolo -> 3 pontos

pontuacao = 1*p + 2*d + 3*b

if pontuacao >= 150:
    print("B")

elif pontuacao >= 120:
    print("D")

elif pontuacao >= 100:
    print("P")

else:
    print("N")