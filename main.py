casos = int(input())
cont = int(0)
dentro = int(0)
fora = int(0)
while cont < casos:
    numero = int(input())
    if numero >= 10 and numero <= 20:
        dentro = dentro + 1
    else:
        fora = fora + 1
    cont = cont + 1
print("{} in".format(dentro))
print("{} out".format(fora))