#While , laço
'''
contador = 0

while contador <10:
    contador = contador + 1
    #contador += 1
    print(contador) 


#operadores de atribuição com operadores aritmeticos

+=, -= ,/= *=, //=, %=


contador = 0

while contador <= 10:
    contador += 1

    if contador == 4:
        print(contador)
        break

    print(contador)

print('Acabou')



nome = 'Joao Pedro'

indice = 0
novo_nome =''

while indice < len(nome): 
    letra = nome[indice]
    novo_nome += f'*{letra}'

    indice += 1

print(novo_nome)

'''

#sair
'''sair = input('quer sair? [s]im: ')lower().startswith('s')


  if sair is true:
  break
'''
from random import randint

print('''Escolha a dificuldade:
      [1] - Fácil (1 a 50)
      [2] - Médio (1 a 100)
      [3] - Difícil(1 a 500)''')

dificuldade = int(input("Digite a dificuldade: "))
if dificuldade == 1:
   numero_secreto = randint(1,50)

elif dificuldade == 2:
   numero_secreto = randint(1,100)

elif dificuldade == 3:
   numero_secreto = randint(1,500)
      

numero = 0

tentativas = 0
while numero != numero_secreto: 
      numero = int(input(f"Tentativa {tentativas + 1} - Adivinhe o número: "))
      if numero > numero_secreto:
        print("Muito alto, tente novamente.")
   
      elif numero < numero_secreto:
       print("Muito baixo, tente novamente.")
      tentativas += 1
                         

else:
  print(f"Número correto: {numero}. Você acertou em {tentativas} tentativas.")
   
