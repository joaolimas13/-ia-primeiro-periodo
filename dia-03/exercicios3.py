

#concatenacao e soma

concatenacao = 'A' + 'b' +'c'
print(concatenacao)

a_dez_vezes = 'A' * 10
print(a_dez_vezes)

tres_vezes_jp = 'JP' * 3
print(tres_vezes_jp, end='\n')

#precedencia de operadores aritméticos

#  (n+n)  = parenteses
#  ** =  potenciação ou exponenciacao
#  */ //% multiplicação , divisao, divisao inteira ou modulo
#  4. + - adição e subtração

conta_1 = (1+1) **(5+5)
print(conta_1)




#formatação de strings usando F 

nome = 'JP'
altura = 1.68
peso = 95

linha_1 = f'{nome} tem {altura:.2f} de altura'

print(linha_1)

'''   
#Formatação com método format
'''
a = 'A'
b = 'B'
c = 'C'

string ='a={} b={} c={}'. format(a,b,c)
formato = string.format(a,b,c)

print(formato)



nome = "Luiz"
idade = 23
formato = '{n} tem {i} anos'
print(formato.format(n=nome, i=idade))

 
nome = input('Qual o seu nome?')
print(f'O seu nome é {nome}')


numero_1 = input('Digite um número: ')
numero_2 = input('Digite outro número: ')

int_numero1 = int(numero_1)
int_numero2 = int(numero_2)

print(f'A soma dos números é: ', {int_numero1 + int_numero2})

#exercícios extra

nome= input("Digite seu nome: " )
sobrenome= input("Digite seu sobrenome:")

nome_completo = nome + " " + sobrenome

print("Nome completo: ", nome_completo)


texto = input("digite uma palavra: ")


print(texto)
print('-' * len(texto))

a = int(input("Digite um numero: "))
b = int(input("Digite outro numero: "))

equacao_A = a + (b * 2)
equacao_B = (a+b) *2 

print("equaçaõ A: ", equacao_A)
print("Equação B: ", equacao_B)


peso = float(input("qual seu peso? "))
altura = float(input("qual sua altura: "))

imc = peso/altura**2 

print(f"Peso: {peso:.1f} KG | Altura:{altura:.1f} | IMC:{imc:.2f} !!!")


nota = float(input("Qual valor da nota de 0 a 10: "))

if nota >= 7:
    print("aprovado")

elif nota >=5:
    print("Recuperação")

else:
    print("Reprovado")
 

num = int(input("digite um número: "))

if num % 2 == 0:
    print("Acesso permitido.")

else: 
    print("Acesso negado!")



usuario_corrreto ="Joao"
senha_correta = "Lima"

senha1 = input("digite usuário: ")
senha2 = input("digite senha: ")

if usuario_corrreto == senha1  and senha_correta == senha2:
    print("Acesso permitido!")

else:
    print("acesso negado!")

    ''

nome = input("qual seu nome: ")
nota1 = float(input("me de sua primeira nota: "))
nota2 = float(input("me de a outra nota: "))

media = (nota1 + nota2)/2 


print(f"Linha 1: {nome}", sep=" ", end="\n") 
print(f"Linha 2:{nota1, nota2}", sep=" ", end="\n")
print(f"Linha 3:{media}", sep=" ", end="\n")


if media >= 7:
   print("Linha 4:aprovado.")

else:
   print("Linha 4:reprovado.")


idade = int(input("digite sua idade: "))

if idade >= 18:
    print("Maior de idade.")

else:
    print("Menor de idade.")
    

num1 = (input("digite um número: "))

print("Antes: ",type(num1))

print("depois:", type(num1))
