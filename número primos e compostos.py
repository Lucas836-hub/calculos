
#criado por Lucas gabriel
# github : github.com/Lucas836
# instagra : @lucas_git

import os
from random import randint
from time import sleep

def limpar():
	try:
		os.system("clear")
	except:
		os.system("cls")


def fim():
	for c in range(0,10):
		limpar()
		o=randint(2,6)
		print("(• _ •)".center(50))
		print(f"\n\033[3{o}mVolte Sempre\033[m".center(50))
		
		sleep(0.5)
		
		limpar()
		o=randint(2,6)
		print("(• _ -)".center(50))
		print(f"\n\033[3{o}mVolte Sempre\033[m".center(50))
		
		sleep(0.5)
		

def verificar():
	while True:
		try:	
			n = int(input("Digite o número : "))
		except:
			print("\033[31mERRO : Valor inválifo :( tente novamente.\033[m")
		else:
			break
	limpar()
	resul(n)
	
	
def resul(n):
	m = 0
	for c in range(1,n):
		if( n % c == 0):
			m += 1
		if( m > 2):
			break
	
	if( m > 2):
		print(f"\033[33mO número {n} é composto\033[m")
	
	else:
		print(f"\033[36mO número {n} é primo\033[m")
	j = input("\nDigite n para parar ou dê enter para continuar : ")
	if(j.lower() == "n"):
		fim()
	else:
		limpar()
		verificar()
		
verificar()