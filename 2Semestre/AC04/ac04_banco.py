# Linguagem de Programação II
# AC04 - Banco
#
# Nome Aluno 1: Vinicius Tertuliano
# Nome Aluno 2: Abner de Melo Porto
# Nome Aluno 3: nome


class Cliente():
    """
    Classe Cliente.
    possui os atributos PRIVADOS:
    - nome,
    - telefone,
    - email.
    caso o email não seja válido (verificar se contém o @) gera um ValueError
    (deve apenas gerar a exceção com raise ValuError,
    nao precisa fazer o try-except),
    caso o telefone não seja um número inteiro gera um TypeError
    """

    def __init__(self, nome: str, telefone: int, email: str):
        self.__nome = nome
        self.__telefone = telefone
        self.__email = email

    def get_nome(self):
        """Retorna o atributo nome."""
        return self.__nome

    def get_telefone(self):
        """Retorna o atributo telefone."""
        return self.__telefone

    def set_telefone(self, novo_telefone: int):
        """
        Altera o atributo telefone.
        Caso não receba um número inteiro, gera um TypeError
        """

        if isinstance(novo_telefone, int):
            self.__telefone = novo_telefone
        else:
            raise TypeError('Valor informado não é inteiro')

    def get_email(self):
        """Retorna o atributo Email."""
        return self.__email

    def set_email(self, novo_email: str):
        """
        Altera o atributo Email.
        Caso não receba um email válido (contendo o @), gera um ValueError.
        """
        if '@' in novo_email:
            self.__email = novo_email
        else:
            raise ValueError('E-mail invalido')


class Banco:
    """
    Os atributos devem ser privado
    A classe Banco deverá receber em seu construtor o nome do banco e deverá
    implementar os métodos:
    - abrir_conta(): abre uma nova conta, atribuindo AUTOMATICAMENTE o numero
    da conta em ordem crescente, a partir de 1 para a primeira conta aberta.
    - listar_contas(): retorna uma lista com todas as contas do banco

    DICA: utilize o atributo __lista_contas para armazenar as contas do banco
    DICA2: utilize o atributo __numero_conta para gerar automaticamente o
    número das contas do banco (incrementar sempre que uma conta é aberta)
    """

    def __init__(self, nome: str):
        self.__nome = nome
        self.__lista_contas = []
        self.__numero_conta = 1
        pass

    def get_nome(self):
        """Retorna o Atributo Nome."""
        return self.__nome

    def abrir_conta(self, cliente: Cliente, saldo: float):
        """
        Método para abertura de nova conta
        Recebe um objeto cliente e o saldo inicial da conta.
        Cria um objeto da classe Conta e armazena na lista de contas
        Caso o saldo inicial seja menor que 0 gera um ValueError
        Armazena todas as contas abertas na lista self.__lista_contas
        """
        if saldo < 0:
            raise ValueError('Conta não pode ser aberta com saldo negativo.')
        else:
            i = len(self.__lista_contas)
            id_con = i + 1
            conta = Conta(cliente, id_con, saldo)
            self.__lista_contas.append(conta)
        pass

    def listar_contas(self):
        """Retorna lista com todas as contas abertas no banco"""
        return self.__lista_contas


class Conta:
    """
    Classe Conta: os atributos devem ser privados
    - Caso o saldo inicial seja menor que zero deve gerar um ValueError
    - Todas as operações (saldo inicial, saque e deposito) devem aparecer
      no extrato como tuplas.
      Exemplo: (saldo_inicial, 500), ('saque', 100), ('deposito', 200).
    - A criação da conta deve aparecer no extrato com o valor
      do saldo_inicial, exemplo: ('saldo_inicial', 1000)

    DICA: Utilize a lista __operacoes para guardar as operações feitas na conta
    """

    def __init__(self, cliente: Cliente, numero: int, saldo: float):
        self.__cliente = cliente
        self.__numero = numero
        self.__saldo = saldo
        self.__operacoes = []
        self.__operacoes.append(["saldo_inicial", saldo])

    def get_cliente(self):
        """Retorna o atributo cliente."""
        return self.__cliente

    def get_saldo(self):
        """Retorna o atributo saldo"""
        return self.__saldo

    def get_numero(self):
        """Retorna o atributo numero"""
        return self.__numero

    def sacar(self, valor: float):
        """
        Realiza saque na classe Conta, operação deve aparecer no extrato
        Caso o valor do saque seja maior que o saldo da conta,
        deve gerar um ValueError, e não efetuar o saque
        """
        if valor > self.__saldo:
            raise ValueError('Valor maior que o saldo atual.')
        else:
            self.__saldo -= valor
            return self.__operacoes.append(["saque", valor])

    def depositar(self, valor: float):
        """Realiza depósito na Conta, operação deve aparecer no extrato"""
        self.__saldo += valor
        return self.__operacoes.append(["deposito", valor])

    def extrato(self):
        """
        Retorna uma lista de tuplas com todas as operações realizadas na Conta
        (saldo inicial, saque e deposito),
        exemplo: [('saldo_inicial', 500), ('saque', 100), ('deposito', 200)]
        """
        return self.__operacoes
