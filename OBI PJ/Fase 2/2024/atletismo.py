n = int(input())
d = {}
for i in range(1,n+1):
    d[i] = 0
for i in range(1,n+1):
    c = int(input())
    d[c] = i
for corredor in d.items():
    print(corredor[1])