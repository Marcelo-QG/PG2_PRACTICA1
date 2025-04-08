# PG2_PRACTICA1
# **Practica_1  calculadora en Python**

En esta práctica se implementa una **Calculadora en Python** que permite realizar operaciones aritmeticas basicas como:

-Suma
-Resta
-Multiplicacion
-Division

Del mismo modo, se implementa una **Calculadora de Factorial** que aplica principios de:

- Herencia 
- Polimorfismo

---

##Preparacion del entorno

---

##Implementacion de la calculadora

from calculadora_poo import Calculadora

# Instanciación
calculadora_1 = Calculadora()

# Operaciones básicas
print(f"2 + 5 = {calculadora_1.sumar(2, 5)}")          # ➡️ 7
print(f"10 - 9 = {calculadora_1.restar(10, 9)}")       # ➡️ 1 
print(f"5 × 9 = {calculadora_1.multiplicar(5, 9)}")    # ➡️ 45
print(f"150 ÷ 6 = {calculadora_1.dividir(150, 6)}")    # ➡️ 25.0

---

#Implementacion de la Calculadora Factorial

from calculadora_poo import CalculadoraFactorial

# Cálculo de factorial
```Python
calculadora_factorial = CalculadoraFactorial(numero=5)
print(f"5! = {calculadora_factorial.calcular()}")  # ➡️ 120
```

