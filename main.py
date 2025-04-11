from calculadora_poo import calculadora2
from Factorial import CalculadoraCientifica

print("Calculadora estandar")
 
calc = calculadora2()
print(calc._sumar(10, 5))
print(calc._resta(10, 5))
print(calc._multiplicacion(10, 5))
print(calc._division(10, 5))


print("Calculadora Factorial")
calcF = CalculadoraCientifica(5)
print(calcF.calcular())

