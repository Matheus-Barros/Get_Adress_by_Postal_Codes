import os
import requests

os.system('cls')

def main():
	
	while True:
		cep_input = input('Type te postal code: ')
		#cep_input = '24730230'

		if len(cep_input) != 8:
			print('Postal code invalid')
			continue

		request = requests.get('https://viacep.com.br/ws/{cep}/json/'.format(cep = cep_input))

		adress = request.json()

		if 'erro' in adress:
			print('Postal code Invalid')
		else:
			print('\n----------- ADRESS FOUND -----------')
			print('\nPostal Code: '  + adress['cep'])
			print('Logradouro: '  + adress['logradouro'])
			print('Bairro: '  + adress['bairro'])
			print('Localidade: '  + adress['localidade'])
			print('Complemento: '  + adress['complemento'])

		resp = input('\nWanna search something more? (Y/N)')


		if resp.strip() != 'Y' and resp.strip() != 'y':
			break


if __name__ == '__main__':
	main()