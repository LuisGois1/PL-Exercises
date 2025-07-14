##Receba o raio de um círculo e calcule a área (π * r²).
import math
raio = float(input("Insira o Raio do Círculo: "))
area = math.pi * (raio**2)
print(f"A Área do Círculo é: {"{:.2f}".format(area)}!")