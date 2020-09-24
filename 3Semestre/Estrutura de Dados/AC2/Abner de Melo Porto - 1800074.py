import random
import base64
import urllib.request
import ssl


# Coloque o seu nome completo e RA como strings.
NOME_COMPLETO = 'Abner de Melo Porto'
RA = '1800074'

"""
ANTES DE COMEÇAR, LEIA ATENTAMENTE AS INSTRUÇÕES:
Nesta atividade você deve ordenar algumas listas numéricas de acordo com o enunciado.
Para ter acesso ao enunciado, complete as variáveis NOME_COMPLETO e RA.
Atenção: caso o seu nome completo e RA esteja diferente do cadastrado no sistema, sua nota será 0 (zero)!
Atenção: você deve entregar ESTE código .py como resposta. Caso entregue em outro formato e caso o seu código não rode, sua nota será 0 (zero)!


Antes de começar, observe os problemas resolvidos nos exemplos abaixo. Eles vão te ajudar a resolver o problema.

Exemplo resolvido 1):
Considere a questão hipotética: Ordene a lista [24, 76, 59, 84, 63] de acordo com o algoritmo de seleção.

Na resposta, você deve fazer o passo a passo do algoritmo de seleção (ou outro algoritmo pedido na questão).
Na primeira linha da resposta, repita a lista do enunciado da questão.
No passo 1 do algoritmo de seleção, você deve procurar o menor elemento e trocá-lo com o elemento na primeira posição da lista.
No passo 2 do algoritmo de seleção, você deve procurar o menor elemento da lista a partir do índice 1 e trocá-lo com o elemento no índice 1.
Os demais passos são análogos. Observe o exemplo resolvido abaixo:

questao1_exemplo = [
[24, 76, 59, 84, 63],    # Na primeira linha da resposta, repita a lista original.
[24, 76, 59, 84, 63],    # A partir desta linha, comece a ordenar a lista (passo 1 do algoritmo de seleção).
[24, 59, 76, 84, 63],    # Passo 2 do algoritmo de seleção.
[24, 59, 63, 84, 76],    # Passo 3 do algoritmo de seleção.
[24, 59, 63, 76, 84]     # Repita o processo até a sua lista estar totalmente ordenada.
]


Exemplo resolvido 2):
Considere a questão hipotética: Ordene a lista [92, 10, 85, 95, 62, 24, 17] de acordo com o método da bolha.

questao2_exemplo = [
[92, 10, 85, 95, 62, 24, 17],     # Copie a lista original aqui.
[10, 85, 92, 62, 24, 17, 95],     # "Borbulhe" o maior elemento até o fim da lista
[10, 85, 62, 24, 17, 92, 95],     # "Borbulhe" o segundo maior elemento até a penúltima posição da lista
[10, 62, 24, 17, 85, 92, 95],     # os próximos passos são análogos...
[10, 24, 17, 62, 85, 92, 95],
[10, 17, 24, 62, 85, 92, 95]      # ... até que a lista esteja ordenada!
]


Exemplo resolvido 3):
Considere a questão hipotética: ordende a lista [7, 70, 92, 4, 30, 58, 80, 26, 22] de acordo com o método de inserção.

questao3_exemplo = [
[7, 70, 92, 4, 30, 58, 80, 26, 22],   # Copie a lista original aqui.
[7, 70, 92, 4, 30, 58, 80, 26, 22],   # Considere que o elemento L[0] está ordenado. Encaixe o elemento L[1] na posição correta na sublista L[0:2].
[7, 70, 92, 4, 30, 58, 80, 26, 22],   # Considere a sublista L[0:2] está ordenada. Encaixe o elemento L[2] na posição correta  na sublista L[0:3].
[4, 7, 70, 92, 30, 58, 80, 26, 22],   # Considere que a sublista L[0:3] está ordenada. Encaixe o elemento L[3] na posição correta  na sublista L[0:4].
[4, 7, 30, 70, 92, 58, 80, 26, 22],   # os próximos passos são análogos...
[4, 7, 30, 58, 70, 92, 80, 26, 22],
[4, 7, 30, 58, 70, 80, 92, 26, 22],
[4, 7, 26, 30, 58, 70, 80, 92, 22],
[4, 7, 22, 26, 30, 58, 70, 80, 92]    # ... até que a lista esteja ordenada!
]
"""

# Coloque aqui as respostas da QUESTÃO 1
questao_1 = [
[53, 93, 19, 90, 12],
[12, 93, 19, 90, 53],
[12, 19, 93, 90, 53],
[12,19, 53, 90, 93]
]

# Coloque aqui as respostas da QUESTÃO 2
questao_2 = [
[98, 32, 19, 26, 73, 63],
[19, 32, 98, 26, 73, 63],
[19, 26, 98, 32, 73, 63],
[19, 26, 32, 98, 73, 63],
[19, 26, 32, 63, 73, 98]
]

# Coloque aqui as respostas da QUESTÃO 3
questao_3 = [
[0, 74, 80, 15, 54, 59, 20],
[0, 74, 15, 54, 59, 20, 80],
[0, 15, 54, 59, 20, 74, 80],
[0, 15, 54, 20, 59, 74, 80],
[0, 15, 20, 54, 59, 74, 80]
]

# Coloque aqui as respostas da QUESTÃO 4
questao_4 = [

[47, 31, 76, 35, 11, 47, 52, 75],
[47, 31, 35, 11, 47, 52, 75, 76],
[31, 35, 11, 47, 47, 52, 75, 76],
[31, 11, 35, 47, 47, 52, 75, 76],
[11, 31, 35, 47, 47, 52, 75, 76]

]

# Coloque aqui as respostas da QUESTÃO 5
questao_5 = [

[81, 90, 87, 79, 97, 35, 99, 9, 90],
[81, 90, 87, 79, 97, 35, 99, 9, 90],
[81, 87, 90, 79, 97, 35, 99, 9, 90],
[79, 81, 87, 90, 97, 35, 99, 9, 90],
[79, 81, 87, 90, 97, 35, 99, 9, 90],
[35, 79, 81, 87, 90, 97, 99, 9, 90],
[35, 79, 81, 87, 90, 97, 99, 9, 90],
[9, 35, 79, 81, 87, 90, 97, 99, 90],
[9, 35, 79, 81, 87, 90, 90, 97, 99]
]

# Coloque aqui as respostas da QUESTÃO 6
questao_6 = [
[51, 53, 0, 88, 5, 38, 84, 13, 3, 40],
[51, 53, 0, 88, 5, 38, 84, 13, 3, 40],
[0, 51, 53, 88, 5, 38, 84, 13, 3, 40],
[0, 51, 53, 88, 5, 38, 84, 13, 3, 40],
[0, 5, 51, 53, 88, 38, 84, 13, 3, 40],
[0, 5, 38, 51, 53, 88, 84, 13, 3, 40],
[0, 5, 38, 51, 53, 84, 88, 13, 3, 40],
[0, 5, 13, 38, 51, 53, 84, 88, 3, 40],
[0, 3, 5, 13, 38, 51, 53, 84, 88, 40],
[0, 3, 5, 13, 38, 40, 51, 53, 84, 88]
]

















# ================================================================================================ #
# ================================================================================================ #
# ================================================================================================ #
"""
		NÃO EDITE O CÓDIGO A PARTIR DESTE PONTO
"""
# ================================================================================================ #
# ================================================================================================ #
# ================================================================================================ #

def testa_ordenada(lista):
	for i in range(1, len(lista)):
		if lista[i-1] > lista[i]:
			return False
	return True

def mistura_lista(lista):
	for i in range(1, len(lista), 3):
		lista[i-1], lista[i] = lista[i], lista[i-1]

def lista_aleatoria(seed, tamanho, testaOrdenada=True):
	random.seed(seed)
	lista = []
	i = 1
	while i <= tamanho:
		lista.append(random.randint(0, 99))
		i += 1
	if testa_ordenada(lista) and testaOrdenada:
		mistura_lista(lista)
	return lista

def calcula_semente(texto):
	s = 0
	for i in range(len(texto)-1, -1, -1):
		s += ord(texto[i])**(i+1)
	seed = s % 433494437
	return seed

def obter_listas_aluno(nome, tamanhos_listas=[5, 6, 7, 8, 9, 10]):
	listas = []
	seed = calcula_semente(nome)
	for tamanho in tamanhos_listas:
		lista = lista_aleatoria(seed+tamanho+1, tamanho)
		listas.append(lista)
	return listas

def obter_questao(questao):
	if questao.upper() == 'Q1':
		return 'algoritmo de seleção'
	elif questao.upper() == 'Q2':
		return 'algoritmo de seleção'
	elif questao.upper() == 'Q3':
		return 'algoritmo da bolha'
	elif questao.upper() == 'Q4':
		return 'algoritmo da bolha'
	elif questao.upper() == 'Q5':
		return 'algoritmo de inserção'
	elif questao.upper() == 'Q6':
		return 'algoritmo de inserção'

def main(questoes):
	if NOME_COMPLETO.strip().upper() and str(RA).strip().upper():
		print('\nAluno (RA): {0} ({1})'.format(NOME_COMPLETO, RA))
		listas = obter_listas_aluno(NOME_COMPLETO.upper() + str(RA))
		print('\nListas que você deve ordenar:')
		for i in range(1, len(listas)+1):
			alg = obter_questao('q{0}'.format(i))
			print('QUESTÃO {0}: {1}, usando o {2}.'.format(i, listas[i-1], alg))
		print('\n======== NOTAS PARCIAIS ===============')
		try:
			b64listas = base64.b64encode(str(listas).encode('ascii')).decode('ascii')
			b64questoes = base64.b64encode(str(questoes).encode('ascii')).decode('ascii')
			req = urllib.request.urlopen('http://www.ime.usp.br/~rwill/tarefa/estdados_ac2/index.php?lists={0}&answers={1}&classid={2}'.format(b64listas, b64questoes, 'ads3asi3a193240'), context=ssl._create_unverified_context())
			str_notas = req.read().decode('utf-8')
			notas = eval(str_notas)
			media = 0.0
			for i in range(1, len(notas)+1):
				media += notas[i-1]/len(notas)
				print('Nota da questão {0}: {1:5.2f}'.format(i, notas[i-1]))
			print('Nota final: {0:5.2f}'.format(media))
			return (notas, media)
		except:
			print('Erro ao executar o corretor automático.')
			return -1
	else:
		print('Para iniciar a atividade você deve preencher o seu nome completo na variável NOME_COMPLETO e o seu número de matrícula na variável RA.')
		print('\nATENÇÃO: A atividade é vinculada ao seu nome completo e ao seu RA. Preste muita atenção ao preencher esses campos para não ficar com nota zero.')
	print('')
if __name__ == '__main__':
	main([questao_1, questao_2, questao_3, questao_4, questao_5, questao_6])
	input(' --- Pressione <ENTER> para encerrar ---')

