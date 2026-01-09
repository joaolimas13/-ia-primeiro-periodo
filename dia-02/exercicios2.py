nome = input ("qual seu nome?")
idade = input ("qual sua idade?")
peso = input ("qual seu peso?")
print (nome,idade,peso)


nome = input ("qual seu nome?")
print ("seja bem vindo, {nome}")


num1 = input("escolha 1 numero:")
num2 = input("escolha outro numero:")
soma = int(num1) + int(num2)

print("a soma é" ,soma)

nome = input("qual seu nome?")
print ("seja bem vindo",nome)

print("tipo de nome:", type(nome))
print("quantidade  de letras:",len(nome))


#dia 2 

#aula do curso da UDEMY de tipos str(string)

#aspas simples
print('"oi mundo!"')

#aspas duplas
print("'oi mundo!'")

#escape

print(13, 40, sep='-',end='\n')
print(12, 20, sep='-',end='\n##')
print(12, 20, sep='-',end='\n')
 

 #Int  = numeros inteiros

print(32)

#float = numero com ponto flutuante
print(1.1) 

#type = falando qual o tipo do dado, se string, int ou float

print(type('Jp'))
print(type(12))
print(type(1.1))

#booleano

print(1+1)

num1=input("escolha um número:")
num2=input("escolha outro número:")


print(int(num1)+ int(num2))

nome=input("escreva uma palavra:")

print("voce escolheu:", nome)
print(type(nome))
print(len(nome))

num1 = input(("escolha um numero:"))
num2 = input(("escolha outro numero:"))

soma = (float(num1)+float(num2))

print("o resultado escolhido foi:",soma)

num1=int(input("escolha um número:"))
if num1 > 0:
   print("positivo")
else:
   print("negativo")

nota =float(input("digite a nota:"))

if nota>7:
    print("aprovado")

else:
    print("reprovado")

nota =float(input("digite a nota:"))

if nota>7:
    print("aprovado")

else:
    print("reprovado")



nome= input("Digite seu nome:")
sobrenome= input("Digite seu sobrenome:")
idade= int(input("Digite sua idade:"))
ano_de_nascimento = int(input("Digite seu ano de nascimento:"))
altura_metros= float(input("Qual sua altura em metros:"))

print('Nome:', nome)
print('Sobrenome:', sobrenome)
print('Idade:', idade)
print('ano de nascimento:',ano_de_nascimento)
if idade > 18:
    print("é maior de idade.")
else:
    print("é menor de idade")    
print('altura em metros:',altura_metros)

altura = float(input("digite sua altura em metros:"))
peso = float(input("digite seu peso:"))

imc = peso/(altura*altura)

print("o seu IMC é:",imc)

