# Programação Orientada a Objetos
# AC01 ADS-EaD - Números especiais
#
# Email Impacta: fernando.macedo@aluno.faculdadeimpacta.com.br

def eh_primo(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


def lista_primos(n):
    # Foi usada a função eh_primo para compor esta função.
    primos = []
    x = 2
    while x < n:
        if eh_primo(x):
            primos.append(x)
        x = x + 1
    return primos


def conta_primos(s):
    # Foi usada a função eh_primo para compor esta função.
    import collections
    entrada = []
    primos = []
    for x in s:
        entrada.append(x)
    for i in entrada:
        if eh_primo(i):
            primos.append(i)
        i = i + 1
    primos = sorted(primos)
    saida = collections.Counter(primos)
    return dict(saida)


def eh_armstrong(n):
    transforma = str(n)
    contador = 0
    for i in range(len(transforma)):
        contador = contador + (int(transforma[i]) ** len(transforma))
    if contador == n:
        return True
    else:
        return False


def eh_quase_armstrong(n):
    transforma = str(n)
    contador = 0
    for i in range(len(transforma)):
        contador = contador + (int(transforma[i]) ** len(transforma))
    if contador == n + 1:
        return True
    elif contador == n - 1:
        return True
    else:
        return False


def lista_armstrong(n):
    # Foi usada a função eh_armstrong para compor esta função.
    arms = []
    x = 0
    while x < n:
        if eh_armstrong(x):
            arms.append(x)
        x = x + 1
    return arms


def eh_perfeito(n):
    limite = n // 2
    total = 0
    if n != 0 and n != 1:
        total = 1
    if n % 2 == 0:
        total += limite + 2
    for i in range(3, limite):
        if n % i == 0:
            total += i
    if n == total:
        return True
    else:
        return False


def lista_perfeitos(n):
    perfeitos = []
    x = 0
    while x < n:
        if eh_perfeito(x):
            perfeitos.append(x)
        x = x + 1
    return perfeitos
