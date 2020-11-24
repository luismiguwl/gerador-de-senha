import random
import string_utils

def solicitar_tamanho_da_senha():
	quantidade_maxima_de_caracteres = 64
	quantidade_minima_de_caracteres = 8

	while True:
		print('Quantidade de caracteres da tua senha: ', end = '')
		quantidade_inserida = int(input())

		if quantidade_inserida > quantidade_maxima_de_caracteres:
			print('Sua senha deve ter no máximo',quantidade_maxima_de_caracteres,'caracteres')
			continue

		if quantidade_inserida < quantidade_minima_de_caracteres:
			print('Sua senha deve ter no mínimo',quantidade_minima_de_caracteres,'caracteres')
			continue

		return quantidade_inserida

def solicitar_tipo_de_senha():
	tipos_de_senha = ['Somente letras', 'Somente números', 'Letras e números']

	print('\nUse números para selecionar um estilo de senha\n')

	for i in tipos_de_senha:
		print(tipos_de_senha.index(i)+1, end = '')
		print('.',i)

	while True:
		print('\nTua escolha: ', end = '')
		numero_da_senha_selecionada = int(input())

		if numero_da_senha_selecionada > len(tipos_de_senha) or numero_da_senha_selecionada < 1:
			print('\nInforme um número entre',1,'e',len(tipos_de_senha))
			continue	

		numero_da_senha_selecionada -= 1

		return tipos_de_senha[numero_da_senha_selecionada]

def sortear_senha(tamanho_da_senha, tipo_de_senha):
	alfabeto = 'abcdefghijklmnopqrstuvwxyz'
	numerais = '1234567890'
	senha = ''

	for i in range(tamanho_da_senha):
		indice_randomico = random.randint(0,len(alfabeto)-1)

		if tipo_de_senha == 'Somente letras':
			senha += alfabeto[indice_randomico]
			continue

		if tipo_de_senha == 'Somente números':
			indice_randomico = random.randint(0,len(numerais)-1)
			senha += numerais[indice_randomico]
			continue

		break

	if tipo_de_senha == 'Letras e números':
			merge = alfabeto + numerais

			while len(senha) < tamanho_da_senha:
				merge = string_utils.shuffle(merge)
				indice_randomico = random.randint(0,len(merge)-1)
				senha += merge[indice_randomico]

	return senha


def decidir_continuidade():
	while True:
		print('\nDeseja gerar mais senhas? (S/N): ', end = '')
		escolha = input()

		if escolha[0].lower() == 's':
			return True
		if escolha[0].lower() == 'n':
			return False

		print('\nDigite S ou N para continuar')

while True:
	tamanho_da_senha = solicitar_tamanho_da_senha()
	tipo_de_senha = solicitar_tipo_de_senha()
	senha_gerada = sortear_senha(tamanho_da_senha, tipo_de_senha)

	print('\nSenha gerada:',senha_gerada)

	if decidir_continuidade():
		print()
		continue

	print('\nObrigado por utilizar!')
	break
