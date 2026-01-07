# Exercício 1: imprimir um texto
print("Hello, mundo")

print("\n" + "-"*40 + "\n")

# Exercício 2: ler um número e mostrar o dobro
numero_texto = input("Digite um número: ")
numero = float(numero_texto)
dobro = numero * 2
print("O dobro é:", dobro)

print("\n" + "-"*40 + "\n")

# Exercício 3: cálculo de IMC
peso_texto = input("Digite seu peso (ex: 77.5): ")
altura_texto = input("Digite sua altura em metros (ex: 1.68): ")

peso = float(peso_texto)
altura = float(altura_texto)

imc = peso / (altura ** 2)
print("Seu IMC é:", imc)

print("\n" + "-"*40 + "\n")

# Exercício 4: laço que imprime de 1 a 20
for i in range(1, 21):
    print(i)