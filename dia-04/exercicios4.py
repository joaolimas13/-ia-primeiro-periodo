
#Descobrindo  se o número é par ou impas, importante lembrar do sinal %

num1 = int(input("digite um número: "))

if num1 % 2 ==0: 
    print("numero é par")

else:
    print("numero é impar!")


#condicao
condicao = 10 ==10
print(condicao)



condicao1 = False
condicao2 = False
condicao3 = True
condicao4 = False

if condicao1:
    print("codigo para condicao 1")
    print("codigo para condicao 1") #pode ter mais de um print pra cada condição

elif condicao2:
    print("codigo para condicao 2")

elif condicao3:
    print("codigo para condicao 3")

    
elif condicao4:
    print("codigo para condicao 4") 

else:
    print("nenhuma condicao foi satisfeita:")


 
   # operadores de comparação

    #>...Maior
    #>=...Maior ou igual
    #<... Menor
    #<=... Menor ou igual
    #==... Igual
    #!=... diferente

    



num1=input("Digite um número: ")
num2=input("Digite outro número: ")

if num1 > num2:
    print(f"o número {num1} é maior que o número {num2}")

elif num1 == num2:
    print("Os números são iguais")

else:
    print(f"o número {num2} é maior que o número {num1}")


    



#operadores lógicos and or not 

entrada = input("[E]ntrar  [S]air: ")
senha_digitada = input("senha: ")

senha_permitida = '12345'

if (entrada == 'E' or entrada == "e") and senha_digitada == senha_permitida:
    print("Entrar")

else:
    print("Sair.")
    

#not
senha = input("senha: ")

if not senha:
    print("voce nao digitou nada")


#in e not in

nome = "joao"
print(nome[3])

print('o' in nome)
print(10 * '-')


nome=input("Digite seu nome: ")
sobrenome=input("Digite seu sobrenome: ")

if nome =="" or sobrenome == "":
    print("nome vazio.")

elif nome =="" or sobrenome == " ":
    print("nome com espaços")

else:
    print(f"Cadastro ok.{nome}  {sobrenome}")
   

altura = float(input("Digite sua altura: "))
peso = float(input("digite seu peso :"))

imc = peso / (altura * altura)

if imc <= 18.5: 
   print(f"{imc:.2f} baixo peso.")

elif imc >18.5 and imc<24.9:
    print(f"{imc:.2f}  peso normal.")

else:
     print(f"{imc:.2f} Sobrepeso.")

     

nota = int(input("Digite a nota: "))
presenca = int(input("Digite a presença: "))

if nota >= 7 and presenca >= 75:
    print("Aprovado.")

elif nota >= 5 and presenca >= 75:
    print("Recuperação.")

else:
    print("Reprovado.")


frase = input("Digite uma frase: ")

erros = ("spam" in frase)

if not erros:
    print("Mensagem aceita.")

else:
    print("Mensagem recusada.")
    
 

