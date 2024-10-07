d = int(input())
intervalo = d // 400 + 1
if d % 400 == 0:
    print(0)
else:
    if d - (intervalo-1)*400 < intervalo*400 - d:
        print(d - (intervalo-1)*400)
    else:
        print(intervalo*400 - d)
