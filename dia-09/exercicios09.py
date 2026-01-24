lista_de_frutas = 0 
nome_da_fruta = 0
for num in range (0,10,2):
    print(num)
   

for num2 in range(11):
    if num2 % 2 == 0:
     print(num2)
lista_de_frutas.append(nome_da_fruta)
c = 0
lista_de_frutas = []
while c < 5:

  frutas = input("Digite o nome de 1 fruta: ")
  lista_de_frutas.append(frutas)
  c +=1



for frutas in lista_de_frutas:
    print(f"Minha fruta favorita é: {frutas}")

lista_de_frutas =[]

for c in range(5):
    fruta = input("Escolha uma fruta: ")
    lista_de_frutas.append(fruta)
   

listas_de_numeros =[]

for c in range(5):
    num = 0
    num = int(input("Digite um número: "))
    listas_de_numeros.append(num) 

if num % 2 == 0:
    print(f"Números pares: {num}")


   
    print(listas_de_numeros)


lista = [10,20,30,40,]

lista.append(50)
lista.pop()
lista.append(70)
ultimo_valor = lista.pop(3)
lista.insert(-1,5)
print(lista)

lista_a =['Luiz', 'Maria']
lista_b = lista_a

lista_a[0] = 'qualquer coisa'
print(lista_b)

contador = 0
num = 0
decisao = ''
media = 0
soma_total = 0
while decisao != 'n':
       
       num = int(input("Digite um número: "))
       decisao=input("Gostaria de continuar? [s][n]").strip().lower()
       contador +=1
       soma_total += num
     
       if decisao == 'n':
        media = soma_total / contador
       
        print(f'você tentou {contador} vezes. A média dos números digitados foi {media:.2f}')
       



print("finalizou")
    

print('''***Seja bem vindo***
      Crie uma senha que contenha:
      letra maiúscula
      letra minúscula
      1 número.
    *****************************
      ''')


opcao = ""

# Loop principal para permitir que o usuário digite várias senhas
while opcao.lower() != 'sair': # Usamos .lower() para aceitar 'Sair', 'sair', 'SAIR'
    senha = input("Digite a senha (ou 'sair' para finalizar): ")

    if senha.lower() == 'sair': # Se o usuário digitar 'sair', quebra o loop
        break

    
    tem_maiuscula = False
    tem_minuscula = False
    tem_digito = False
  

   
    if len(senha) < 8:
        print("Erro: A senha deve ter no mínimo 8 caracteres.")
        continue 

    for caractere in senha:
        if caractere.isupper():
            tem_maiuscula = True
        if caractere.islower():
            tem_minuscula = True
        if caractere.isdigit():
            tem_digito = True

        
        if tem_maiuscula and tem_minuscula and tem_digito:
            break

   
    if tem_maiuscula and tem_minuscula and tem_digito:
        print("Senha correta! Atende a todos os critérios.")
    else:
        print("Erro: A senha não atende a todos os critérios:")
        if not tem_maiuscula:
            print("- Deve conter pelo menos uma letra maiúscula.")
        if not tem_minuscula:
            print("- Deve conter pelo menos uma letra minúscula.")
        if not tem_digito:
            print("- Deve conter pelo menos um número.")
   

print("Programa finalizado.")

import os

lista = []

while True:
    print('Selecione uma opção')
    opcao = input('[i]nserir [a]pagar [l]istar: ')

    if opcao == 'i':
        os.system('clear')
        valor = input('Valor: ')
        lista.append(valor)
    elif opcao == 'a':
        indice_str = input(
            'Escolha o índice para apagar: '
        )

        try:
            indice = int(indice_str)
            del lista[indice]
        except ValueError:
            print('Por favor digite número int.')
        except IndexError:
            print('Índice não existe na lista')
        except Exception:
            print('Erro desconhecido')
    elif opcao == 'l':
        os.system('clear')

        if len(lista) == 0:
            print('Nada para listar')

        for i, valor in enumerate(lista):
            print(i, valor)
    else:
        print('Por favor, escolha i, a ou l.')