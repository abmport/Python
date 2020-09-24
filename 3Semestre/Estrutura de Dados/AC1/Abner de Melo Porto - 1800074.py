import unittest
import hashlib

"""
Leia atentamente as instruções:
	- Renomeie o arquivo com o padrão: "Seu Nome Completo - Seu RA", com a extensão .py.
	- O arquivo deve estar no formato de código/arquivo texto. Arquivos que não rodam terão nota 0 (zero)!
	- Coloque o seu nome completo como string na variável NOME_COMPLETO (abaixo).
	- Coloque o seu RA como string na variável RA_ALUNO (abaixo).
	- IMPORTANTE: Casos de plágio terão a nota de TODOS OS ENVOLVIDOS cortada pela metade.
	- IMPORTANTE: Casos reincidentes de plágio receberão nota 0 (zero)!!!
"""

# OBRIGATÓRIO: coloque o seu nome COMPLETO e RA como string nas variáveis abaixo:
NOME_COMPLETO = 'Abner de Melo Porto/'
RA_ALUNO = '1800074'


"""
Questão 1: Dada uma lista, implemente a função troca_dois_a_dois(lista) que percorre
toda a lista e troca os elementos em lista[i-1] e lista[i] caso lista[i-1] > lista[i].

Dica: utilize uma estrutura de repetição (while ou for, de acordo com a sua preferência) que percorre
os índices da lista de 1 (o segundo elemento da lista) até len(lista)-1 (o último elemento da lista).

Restrições: esta tarefa deve ser realizada sem o uso de funções auxiliares. Está proibido
o uso das funções/métodos: list(), min(), max(), sum(), list.index(), list.reverse(),
list.sort().

Entrada:
	- lista: parâmetro que contém uma lista

Saída:
	- a função deve retornar (devolver) a lista após o fim do processamento. Você não precisa criar
uma nova lista vazia. Basta utilizar a própria lista enviada por parâmetro.

Exemplos de entrada e saída:
	Exemplo 1:
		Entrada: 	[95, 76, 65, 88, 10]
		Saída: 		[76, 65, 88, 10, 95]

	Exemplo 2:
		Entrada: 	[90, 69, 15, 16, 5, 70]
		Saída: 		[69, 15, 16, 5, 70, 90]
"""

lista = []
i = 1
def troca_dois_a_dois(lista):
    for i in range(1,len(lista)):
        if lista[i-1] > lista[i]:
            var_aux = lista[i-1]
            lista[i-1] = lista[i]
            lista[i] = var_aux

    # Você não precisa chamar a função, pois o código de teste faz isso para você.
    return lista  # A função deve devolver a lista ao final da execução.


# ================================================================================================ #
# ================================================================================================ #
# ================================================================================================ #
"""
		>>> NÃO EDITE O CÓDIGO A PARTIR DESTE PONTO ATÉ O FINAL <<<
"""
# ================================================================================================ #
# ================================================================================================ #
# ================================================================================================ #


class RestrictedList(list):

    def __init__(self, sequence):
        for item in sequence:
            self.append(item)

    def reverse(self):
        raise AttributeError('Proibido o uso do método reverse()')

    def sort(self, reverse=False):
        raise AttributeError('Proibido o uso do método sort()')

    def index(self, value):
        raise AttributeError('Proibido o uso do método index()')


def min(x):
    raise NameError('Proibido o uso da função min()')


def max(x):
    raise NameError('Proibido o uso da função max()')


def sum(x):
    raise NameError('Proibido o uso da função sum()')


def list(x):
    raise NameError('Proibido o uso da função list()')


class TesteAtividade01(unittest.TestCase):
    def test_01(self):
        resp = troca_dois_a_dois(RestrictedList([73]))
        self.assertEqual(hashlib.sha224(str(resp).encode('utf8')).hexdigest(
        ), '3beb68991a935395556e08b5ff500c7a27cf70720abf88a8b97878bf')

    def test_02(self):
        resp = troca_dois_a_dois(RestrictedList([22, 50]))
        self.assertEqual(hashlib.sha224(str(resp).encode('utf8')).hexdigest(
        ), 'cdc41071eb60a6e1d84a22c13f2e8506f4fd9ed79e04382fd0c3d9f7')

    def test_03(self):
        resp = troca_dois_a_dois(RestrictedList([53, 76, 65]))
        self.assertEqual(hashlib.sha224(str(resp).encode('utf8')).hexdigest(
        ), '296913b553f4a4ef307ed9733413e11cfedd20023c61cdec0ec14634')

    def test_04(self):
        resp = troca_dois_a_dois(RestrictedList([17, 58, 54, 37]))
        self.assertEqual(hashlib.sha224(str(resp).encode('utf8')).hexdigest(
        ), '855fee0a8538e65144afed727229dd3d066b5b8f8ffeffb6a7980ac1')

    def test_05(self):
        resp = troca_dois_a_dois(RestrictedList([71, 65, 95, 2, 20]))
        self.assertEqual(hashlib.sha224(str(resp).encode('utf8')).hexdigest(
        ), '3ee6fb7b8c0162da20fcddc858ab15e2e7ed3bc994638a8ab2f884e1')

    def test_06(self):
        resp = troca_dois_a_dois(RestrictedList([62, 81, 27, 57, 21, 83, 24, 94, 94, 80, 57, 61, 34, 56, 83, 89, 17, 72, 40, 87,
                                                 45, 41, 85, 44, 13, 54, 24, 52, 34, 32, 87, 55, 50, 3, 91, 48, 89, 52, 93, 47, 74, 96, 96, 66, 20, 73, 82, 92, 4, 35]))
        self.assertEqual(hashlib.sha224(str(resp).encode('utf8')).hexdigest(
        ), '924bf3a2a7879d3d5d4c7899ae7b47dcfe00123db92036d92565e504')


if __name__ == '__main__':
    input(' ATENÇÃO: casos de plágio terão a nota de TODOS OS ENVOLVIDOS cortada pela metade. Casos reincidentes receberão nota 0 (zero). \n\t >>> PRESSIONE ENTER PARA CONTINUAR <<<')
    unittest.main()
