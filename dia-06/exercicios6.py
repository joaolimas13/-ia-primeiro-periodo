
'''

num1= (input("Digite um número inteiro: "))

try:

     num1 = int(num1)

     if num1 % 2 == 0:
         print("Número par.")


     else:
          print("Número impar.")

except ValueError:
    print("Isso não é número inteiro: ")



hora = int(input("Quantas horas são: "))

if hora >= 0 and hora <=11:
     print("BOM DIA!")

elif hora >= 12 and hora <=17:
     print("Boa taarde!")

elif hora > 24:
     print("Hora inexistente.")

else:
     print("Boa noite")



nome = input("Digite seu nome: ")

"""tamanho = len(nome) 
if tamanho>1:
"""
if len(nome) <= 4:
    print("Nome pequeno: ")

elif len(nome) >= 5 and len(nome) <= 6:
    print("nome médio.")

elif len(nome) >6:
    print("Nome Grande.")

else:
    print("")


#exercicio1

num1 =input("Digite um número: ")
num2 = input("Digite outro número: ")

num1 = float(num1)
num2 = float(num2)

soma = num1 + num2 

print(f"a soma dos dois números é: {soma:.2f}")


#exercicio2

nome = input("digite um nome: ")

letras = len(nome)

if nome[0] == 'A' or nome[0] == 'a':
    print(f"o nome tem {letras} letras, e começa com a letra A")

else:
    print(f"o nome tem {letras} letras e  Não começa com a letra A.")

if " " in nome:
    print("Tem espaço.")

else:
    print("Não tem espaço.")

   

idade = int(input("Digite sua idade: "))
altura = float(input("Digite sua altura: "))

if idade >= 14 and altura >= 1.60:
   print("Pode brincar.")

else:
   print('não pode brincar.')

   

lado1 = int(input("Digite um lado do triangulo: "))
lado2 = int(input("Digite um lado do triangulo: "))
lado3 = int(input("Digite um lado do triangulo: "))

if lado1 < (lado2 + lado3) and lado2 < (lado1 + lado3) and lado3 < (lado1 + lado2):
    print("Triângulo válido.")
else:
    print("Triangulo invalido.")

if lado1 == lado2 and lado2 == lado3:
    print("triângulo equilátero.")

elif lado1 == lado2 and lado2 != lado3:
    print("Triângulo isosceles.")  

elif lado1 == lado3 and lado3 != lado2:
    print("Triângulo isosceles.") 


elif lado2 == lado3 and lado3 != lado1:
    print("Triângulo isosceles.") 

elif lado1 != lado2 and lado2 != lado3:
    print("Triângulo escaleno")




     

ano = int(input("Digite um ano: "))

if ano % 400 == 0:
    print("bissexto.")

elif ano % 100 == 0:
    print(" nao bissexto.")

elif ano % 4 == 0:
    print("bissexto.")

else:
    print("Nao bissexto.")
  '''
'''
Peça ao usuário o valor de uma compra.

Aplique desconto progressivo: • Até R$ 100: sem desconto • R$ 100.01 a R$ 500: 10% de desconto • R$ 500.01 a R$ 1000: 15% de desconto • Acima de R$ 1000: 20% de desconto

Mostre: • Valor original • Percentual de desconto aplicado • Valor do desconto • Valor final

Tudo formatado como dinheiro (R$ X.XX).

'''

valorCompra = float(input("valor da compra: "))

valor = float(valorCompra)

if valor <= 100:
    print(f"{valor} não tem0 desconto.")

elif valor >= 100.01 and valor <= 500:
    valor10 = (valor *10) / 100
    valorfinal = valor - valor10
    print(f"{valor10}, tem 10% de desconto, totalizando {valorfinal}")

elif valor >=500.01 and valor <1000:
    valor15 = (valor *15) / 100
    valorfinal = valor - valor15
    print(f"{valor} R$, tem 15% de desconto, diminuindo assim {valor15} R$, totalizando {valorfinal} R$.")

    