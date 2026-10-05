from calculo import calcular_media_ponderada

print("Programa para tirar a média de alguns valores.")
print()

nota1 = float(input("Digite a nota da primeira avaliação: "))
nota2 = float(input("Digite a nota da segunda avaliação: "))
nota3 = float(input("Digite a nota da terceira avaliação: "))

media = calcular_media_ponderada(nota1, nota2, nota3)

print("Média ponderada:", media)