'''
nome=input("Digite seu nome: ")
sobrenome = input("Digite seu sobrenome: ")

if not nome.strip() or not sobrenome.strip():
    print("Cadastro vazio.")

else:
    print(f"Cadastro ok: {nome.strip()}  {sobrenome.strip()}")




num1 = input("Digite um número: ")
print(type(num1))

print(type(int(num1)))



idade = int(input("Digite sua idade: "))

if idade >= 18:
    print("Maior de idade.")

else:
    print("Menor de idade.")


usuario_correto = input("Digite usuário: ")
senha_correta = int(input("Digite a senha: "))

usuario = "joao"
senha = 12345

if usuario_correto == usuario and senha_correta == senha: 
    print("acesso permitido.")

else:
    print("Acesso negado.")

    
email = input("Digite um email: ")

if "@" in email and " " not in email and "." in email:
    print("Email correto.")

else:
    print("email incorreto.")

cupom=input("Digite Cupom: ")

if ("OFF" in cupom or "DESC" in cupom) and " " not in cupom:
    print("cupom aceito")

else:
    print("cupom negado.")  

    

email = input("Digite um email: ")

if "@" in email and "." in email and " " not in email and email[0] != "@" and email[-1] != "@":
    print("ok")

else:
    print("email com erro.")

nome_usuario = input("Nome de usuário: ")
senha_usuario= int(input("digite a senha em números: "))

nome = "Joao"
senha= 1618



if nome_usuario == nome and senha_usuario == senha:
    print("Acesso autorizado.")

else:
    print("tente novamente, 2 tentativas restantes")


nome_usuario = input("Nome de usuário: ")
senha_usuario= int(input("digite a senha em números: "))

nome = "Joao"
senha= 1618

if nome_usuario == nome and senha_usuario == senha:
    print("Acesso autorizado.")

else:
    print("tente novamente, 1 tentativas restantes")

nome_usuario = input("Nome de usuário: ")
senha_usuario= int(input("digite a senha em números: "))

nome = "Joao"
senha= 1618

if nome_usuario == nome and senha_usuario == senha:
    print("Acesso autorizado.")

else:
    print("Acesso bloqueado tente novamente mais tarde.")
    
    


nome = 'Joao'
preco = 1000.83732

variavel = '%s, o preço é R$%f' % (nome,preco)   #2F PRA TER DUAS CASAS DECIMAIS
print(variavel)

cpf =(input("Digite seu CPF: "))


if len(cpf) == 11:
    print("cpf correto.")

else:
    print("cpf errado.")

    
  
'''
'''
palavra1 = input("digite uma palavra: ")
palavra2 = input("digite outra palavra: ")

if palavra1 == palavra2:
    print("As palavras são exatamente iguais.")
elif len(palavra1) == len(palavra2):
    print("As palavras têm o mesmo tamanho, mas são diferentes.")
elif len(palavra1) > len(palavra2):
    print("As palavras não são iguais.")
    print("A palavra 1 é maior.")
else:
    print("As palavras não são iguais.")
    print("A palavra 2 é.")

    
 '''   

nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))

print(f"Seu nome é {nome}")

if nome and idade:
   print(f"seu nome é{nome}")
   print(f"seu nome invertido é {nome[::-1]}")
    
   if ' ' in nome:
      print("seu nome contem espaços")
   else:
      print("seu nome não contem espaços.")

    
   print(f'Seu nome tem {len(nome)}letras')
   print(f'a primeira letra do seu nome é {nome[0]}')
   print(f'a ultima letra do seu nome é {nome[-1]}')
else:
    print("você deixou campos vazios.")

'''
 #Try e except

numero_str = input('Vou dobrar o número que voce digitar: ')

try:
    numero_float = float(numero_str)
    print("Float: ", numero_float)
    print(f"O dobro de {numero_str} é {numero_float * 2}")

except:
   print('isso não é um número.')

'''
