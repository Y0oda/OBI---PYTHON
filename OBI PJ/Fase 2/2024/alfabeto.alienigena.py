k, n = [int(x) for x in input().split()]
e1 = input()
e2 = input()
ans = "S"
alfabeto = []
for caractere in e1:
    alfabeto.append(caractere)
for caractere in e2:
    if caractere not in alfabeto:
        ans = "N"
print(ans)