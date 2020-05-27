# Módulos
'''
Divisão do código em 1 ou mais arquivos
Organização de código
Reaproveitamento de código

Importação Absoluta:

import <nome do modulo>
import <nome modulo> as <nome curto>

Importação Relativa:
from <nome do modulo> import <funcao1>, <Classe1>
'''

# Padronização de código PEP8
'''
Principais Regras:
- Separas Classes e funções com 2 linhas em branco
- Separar métodos de classe com 1 linha em branco
- Evitar o uso desnecessário de espaços em branco
- utulizar apenas 1 espaço em branco quando necessário
- Limitar tamanho das linhas em 79 caracteres
- Nomes de variáveis e métodos deve utulizar apenas letras minúsculas
- Nomes de Classes deve iniciar com letra maiúscula
- Inserir linha em branco no final do arquivo
'''

# Coleções
'''
Listas
- Heterogênea
- Mutável
- Delimitada por []
- itens acessados pelo índice
    lista = [valor1, vaor2, valor3]
    lista[0] = [novo_valor]

Tuplas
- Heterogênea
- Não Mutável
- Delimitada por ()
- Itens acessados pelo índice
    tupla = (valor1, valor2, valor3)
    print(tupla[0])

Dicionário
- Heterogênea
- Mutável
- Delimitado por {}
- Armazena pares de valores (chave: valor)
- Itens acessados pela chave
    dic = {chave1: valor1, chave2: valor2}
    dic[chave1] = novo_valor
'''

# Testes Automatizados
'''
Teste de unidade

- Testao retorno de uma função, de acordo com a entrada fornecida
- Verifica se o resultado está correto através da instrução assert
    assert valor1 == valor2
- Se a condição for falsa, gera um AssertionError
'''

# Exceções
'''
Lançamento de uma exceção com a instrução raise
- raise TipoExeceção

As exceções podem ter vários tipos
(TypeError, ValueError, AssertionError, etc.)

Tratamento de Exceções

try: tenta executar um bloco de código.
except: caso ocorra uma exceção é executado o bloco except
corresponde ao tipo da exceção gerada.

else: é executado quando não ocorre nenhuma exceção

finally: é executado sempre.
'''

# Programação Orientada a Objetos POO
'''
É um paradigma de progamação

Classe:
- Define a estrutura dos objetos(modelo)

Objeto:
- Instância concreta de uma classe

Atributos:
- Determinam as cacterísticas do objeto

Métodos:
- Determinam o comportamento do objeto
'''

# Pilares da POO
'''
Abstração:
- como modelar uma entidade do mundo real

Encapsulamento:
- protege atributos e métodos de acesso externo à classe
- atributos e métodos público e privados
- métodos get e set

Herança:
- proporciona reaproveitamento de código e especialização
de classes

Polimorfismo:
- comportamento dinâmico do objeto de acordo com a classe a
qual ele pertence
- herança com sobrescrita de métodos
'''

# Classes e métodos abstratos
'''
Classes Abstratas
- Não podem ser instanciadas
- Geralmente são utilizadas para definir uma
estrutura em comum para as classes filhas

Métodos abstratos
- São métodos que não possuem implementação
- É obrigatório que sejam implementados em todas as
classes filhas
- Só podem existir dentro de classes abstratas
'''

# Manipulaçaõ de Arquivos
'''
Três principais modos de leitura:

- modo 'r' (read) - para ler aquivo
- modo 'w' (write) - para criar e escrever no arquivo
- modo 'a' (append) - para escrever no final do arquivo

Principais funções:
- open() - abre o arquivo
- close() - fecha o arquivo
- write() - escreve uma string no arquivo
- read() - retorna todo o conteúdo do arquivo em uma
única string
- um for pode ser utilizado para percorrer as linhas do arquivo
'''
# Conexão com Banco de Dados
'''

Utilizamos o framework SQLAlchemy
'''


class Demo:
    def __init__(self):
        self.x = 1

    def change(self):
        self.x = 10


class Demo_derived(Demo):
    def __init__(self):
        super().__init__()
        self.x = 10

    def change(self):
        self.x = self.x + 1
        return self.x


obj = Demo_derived()

print(obj.change())
