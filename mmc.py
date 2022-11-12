
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
		
# INPUT
def verificar():
	n = str(input("Digite o número : "))
	cont(n)
	
	
def resul(n):
	
	# tratar dados
	
	l =list(n)
	l2=[]
	for i in range(0,len(l)):
		if(l[i] != " "):
			try:
				l2[-1] = l2[-1] + l[i]
				print("passou")
			except:
				print("nao foi")
				l2.append(l[i])
				pass
		else :
			print("\033[32mfoi\033[m")
			l2.append(l[i])
		
				
	c=0
	while (len(l2) > c):
		print(c)
		if(l2[c] == " "):
			del l2[c]
			c -= 1
		else:
			try:
				l2[c] = int(l2[c])
			except:
				print("\033[31mERRO dados incompativeis\033[m")
				break
		c+=1
		
	return l2
	
	
	# cont -> chamar as funcoes e printar
	
def cont(n):
	# tratra os dados	
	l2 = resul(n)
	print(l2)
	
	# calcula o mmc
	res= mmc(l2)
	
	print(f"\033[36m{res}\033[m")
	
	res2=1
	for k in range(len(res[0])):
		res2 *= res[0][k]
	print(f"\nos divisores foram {res[0]} e o resultado foi {res2}\n")
	
	for g in range(0,len(res)-1):
		try:
			print(res[g+1],"    " ,res[0][g])
		except:
			print(res[g+1])
			
	j = input("\nDigite n para parar ou dê enter para continuar : ")
	if(j.lower() == "n"):
		fim()
	else:
		limpar()
		verificar()

		
def mmc(l2):
	valores=[]
	n_valor=[]
	divisor=[]
	
	for n in range(0,len(l2)):
		n_valor.append(l2[n])
	
	i=2
	while (max(n_valor) > 1):
		print(max(n_valor))
		if(i > max(n_valor)):
			i =2
		print(f"\033[32m{n_valor}\033[m")
		print(f"\033[33m{valores}\033[m")
		if(str(n_valor).replace("[","").replace("]","").replace(",","") not in valores):
			valores.append(str(n_valor).replace("[","").replace("]","").replace(",",""))
			i = 2
		dn=0
		for c in range(0,len(l2)):
			
			if(n_valor[c] % i == 0):
				n_valor[c]=int(n_valor[c]/i)
				if(dn == 0):
					divisor.append(i)
					dn=1
			else:
				n_valor[c]=n_valor[c]
		i +=1
				
	valores.insert(0,divisor)
	
	return valores
				
verificar()