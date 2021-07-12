# Programação Orientada a Objetos
# AC02 ADS-EaD - Criando classes
#
# Email Impacta: fernando.macedo@aluno.faculdadeimpacta.com.br


class Cliente:

    def __init__(self, nome, telefone, email):
        self._nome = nome  # atributo não público
        self.telefone = telefone  # usando o setter de telefone aqui
        self.email = email

    @property
    def nome(self):
        return self._nome

    @property
    def telefone(self):
        return self._telefone

    @telefone.setter
    def telefone(self, novo_telefone):
        if not isinstance(novo_telefone, str):
            raise TypeError

        # se chegou aqui, sabemos que é string
        caracteres_permitidos = [' ', '-', '(', ')']

        # vamos criar uma nova string sem incluir os caracteres permitidos
        apenas_numeros = ''
        for caractere in novo_telefone:
            if caractere not in caracteres_permitidos:
                apenas_numeros += caractere

        # essa nova string deve conter apenas dígitos
        if not apenas_numeros.isdigit():
            raise ValueError

        # se chegou aqui, sabemos que é válido, e fazemos a atribuição
        self._telefone = novo_telefone

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, novo_email):
        if not isinstance(novo_email, str):
            raise TypeError
        contagem = 0
        for c in novo_email:
            if c == "@":
                contagem += 1
        if contagem != 1:
            raise ValueError
        self._email = novo_email


class Conta:
    def __init__(self, clientes, numero, saldo_inicial):
        self._clientes = clientes
        self._numero = numero
        self._saldo = saldo_inicial
        self._operacoes = [('saldo inicial', saldo_inicial)]

    #  property da lista de clientes
    @property
    def clientes(self):
        return self._clientes

    #  property do numero da conta
    @property
    def numero(self):
        return self._numero

    #  property do saldo da conta
    @property
    def saldo(self):
        return self._saldo

    def sacar(self, valor):
        while valor > self._saldo:
            raise ValueError
        else:
            self._saldo = self._saldo - valor
            self._operacoes.append(('saque', valor))

    def depositar(self, valor):
        self._saldo = self._saldo + valor
        self._operacoes.append(('deposito', valor))

    def tirar_extrato(self):
        return self._operacoes


class Banco:
    def __init__(self, nome):
        self._nome = nome
        self._contas = []

    @property
    def nome(self):
        return self._nome

    @property
    def contas(self):
        return self._contas

    def abrir_conta(self, clientes, saldo_inicial):
        if saldo_inicial < 0:
            raise ValueError
        else:
            numero = len(self._contas) + 1
            self._contas.append(Conta(clientes, numero, saldo_inicial))
