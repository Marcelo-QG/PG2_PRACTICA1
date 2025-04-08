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

```Python

from calculadora_poo import calculadora2

# Instanciación

calc = calculadora2()

# Operaciones básicas
print(calc._sumar(10, 5))
print(calc._resta(10, 5))
print(calc._multiplicacion(10, 5))
print(calc._division(10, 5))

```

---

#Implementacion de la Calculadora Factorial

```Python

from Factorial import CalculadoraCientifica

# Cálculo de factorial

calcF = CalculadoraCientifica(5)
print(calcF.calcular())

```

