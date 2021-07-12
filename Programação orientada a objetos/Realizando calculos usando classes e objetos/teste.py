def eh_armstrong(n):
    transforma = str(n)
    contador = 0
    for i in range(len(transforma)):
        contador = contador + (int(transforma[i]) ** len(transforma))
    if contador == n:
        return True
    else:
        return False


def lista_armstrong(n):
    arms = []
    x = 0
    while x < n:
        if eh_armstrong(x):
            arms.append(x)
        x = x + 1
    return arms


armstrong = lista_armstrong(10000)
print(armstrong)
