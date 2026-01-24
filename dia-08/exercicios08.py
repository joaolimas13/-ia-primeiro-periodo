
'''texto = 'Python'

i=0
tamanho_string = len(texto)

while i < tamanho_string:
    print(texto[i],i)

    i+=1



texto = 'Python'

novo_texto = ''

for letra in texto:
    novo_texto += f'*{letra}'
    print(letra)

print(novo_texto + '*')


#Range -> (start,stop, step)

i = int(input('Início: '))
f = int(input('fim: '))
p = int(input('passo: '))

for c in range(i,f+1,p):
    print(c)

print("Fim")


s = 0
for c in range(0,5):
   n=int(input("Digite um valor: "))
   s+= n
   print(f"fim, somatório dos números:{s}")
  

for c in range (0,100):
     if c % 2 == 0: 
       print(c)

        
n = 1

par = impar = 0

while n != 0:
    n = int(input('Digite um valor: '))
    if n % 2 == 0:
        par += 1
    else:
        impar += 1

print(f'par:{par} e impar:{impar}')
    

sexo = input("Digite seu sexo [M] ou [F] ").strip().upper()[0]
 
while sexo != 'M' and sexo != 'F':
     print(f'Dado inválido: {sexo}')


print(f'Sexo selecionado {sexo}')



from random import randint
computador = randint(0,10)
certo = False

contador = 1
while not certo:
    jogador = int(input("Adivinhe o número: "))
    if jogador != computador:
        print(f"você errou!")
        contador +=1 
    else:
        print(f"voce acertou! demorou {contador} tentativas.")
       
        certo = True
    
     
n1 = int(input("Digite um número: "))
n2 = int(input("Digite outro número: "))
opcao = 0
while opcao != 5:
   
    #print([1]Somar
    #[2] Multiplicar
    #[3] Maior
    #[4] Novos números
    #[5] sair do programa)
    opcao = int(input("Qual sua opção?"))
    if opcao ==1:
        soma=n1+n2
        print(f"A soma dos números é: {soma}")

    elif opcao == 2:
        multiplicacao=n1*n2
        print(f"a multiplicação deles é: {multiplicacao}") 
    
    elif opcao ==3:
        if n1>n2:
            print(f"{n1} é maior que {n2}")
        else:
          print(f"{n2} é maior que {n1}.")
    elif opcao == 4:
        n1=int(input("digite um número: "))
        n2=int(input("digite outro número: "))  

    elif opcao == 5:
      print('Fim do programa.')

    else:
        print("Opção invalida")


numero = int(input("Digite um número: "))
c = numero
f = 1

while c > 0:
    f *= c
    print(f)
    c -= 1  # ← ESSA LINHA ESTAVA FALTANDO!
 

num1 = int(input("Digite o número inicial: "))
pos = int(input("Digite a posição: "))
razao = int(input("digite a razão: "))

Pa = num1 +((pos -1) *razao)

print(Pa)


n= int(input("quantos termos de fibonacci voce quer?"))

a=1
b=1
contador = 3
print("1")
print("1")
while contador <= n:
     f = a + b
     print(f)
     a = b
     b = f
     contador +=1
print ("fim")


palavra_secreta ='perfume'
letras_acertadas = ''

while True:

    if len(letra_digitada) >1:
        print("digite apenas uma letra.")
        continue

    if letra_digitada in palavra_secreta:
        letras_acertadas += letra_digitada

frutas = ['Maça','Laranja','Limão']

fruta = input("Digite uma fruta: ")

if fruta not in frutas:
  print("fruta não disponível. ") 
else:
  print("Fruta disponível.")


numero = int(input("digite um número: "))

for c in range (2, numero -1):
     if numero % c == 0:
          print(" não é primo")
          break

else:
  print("é primo")

   if numero > 10:
      print("número inválido, somente menores que 10.")
    continue
  
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
   


usuario = 'wylla'
senha = 12345




tentativas = 3

while tentativas >0:
    user = input("Digite o úsuario: ")
    senha_digitada = int(input("Digite a senha: "))
    if usuario == user and senha == senha_digitada:
        print("Acesso permitido.")
        break

    elif usuario != user or senha != senha_digitada:
       tentativas -=1
       print (f"Acesso negado,você tem mais, {tentativas} tentativas. ")
       

else:
 print("Acesso negado, tente mais tarde.")

 '''

'''
dinheiro = 0
print("----------CAIXA ELETRONICO---------")

login = input("Digite o usuário: ").strip()
senha = int(input("Digite a senha: "))

logincerto = 'Joao'
senha_certa = 12345

if login == logincerto and senha == senha_certa:
   print("acesso permitido.")
   

else: 
 print("acesso negado, tente novamente")


print("------MENU DE OPERAÇÕES------")
print('''Escolha uma opção:
     # [1]Saldo inicial
      #[2]Sacar dinheiro
      #[3]Depositar dinheiro
      #[4]Sair

      ''')


menu = 0
saldo = 1000

while menu != 4:
    menu = int(input("Digite sua opção: "))
    if menu == 1:
      print (f"Seu saldo é:{saldo} ")

    elif menu ==2:
       dinheiro = int(input("Qual valor você quer sacar? "))
       saldo -= dinheiro 
       print(f"dinheiro sacado, seu saldo é {saldo}")

    elif menu ==3:
       dinheiro = int(input("Qual valor você quer depositar? "))
       saldo += dinheiro 
       print(f"dinheiro depositado, seu saldo é {saldo}")

else:
   print("obrigado e até logo")

       




