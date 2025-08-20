#Recebendo dados do usuário

"""
input -> Todo dado recebiod via input é uma String
Em Python, String é tudo que estiver entre:
- Aspas simples ('')
- Aspas duplas (" ")
- Aspas simples triplas (''' ''')
- Aspas duplas triplas (""" """)
"""

#Entrada de dados
#print("Qual o seu nome?")
#nome = input() 

#Simplificando o input em uma linha 
nome = input("Qual o seu nome?\n")

#Exemplo de print 'antigo' versao 2.x
#print("Seja bem-vindo %s!" %nome)

#Exemplo de print 'moderno' versao 3.x
#print("Seja bem-vindo(a) {0}".format(nome))

#Exemplo de print 'mais atual' versao 3.7
print(f"Seja bem-vindo(a) {nome}")

#print("Qual a sua idade?")
#idade = input() #Entrada de dados

#Simplificando o input em uma linha e ja fazendo o cast direto no input
idade = int(input("Qual a sua idade?\n"))

#Processamento

#Saida de dados

#Exemplo de print 'antigo' versao 2.x
#print("%s tem %s anos" % (nome, idade))

#Exemplo de print 'moderno' versao 3.x
#print("{0} tem {1} anos".format(nome, idade))

#Exemplo de print 'mais atual' versao 3.7
print(f"{nome} tem {idade} anos")

#FAzendo um cast dentro do print
#O que é cast é a conversão de um tipo de dado para outro
#Neste tipo de formatacao é possivel fazer calculos dentro do print
print(f"Você nasceu em {2025 - int(idade)}")
