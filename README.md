# PG2_PRACTICA1
# **Practica_1 Calculadora en Python**

En esta práctica se implementa una **Calculadora en Python** que permite realizar operaciones aritmeticas basicas como:

- Suma
- Resta
- Multiplicacion
- Division

Del mismo modo, se implementa una **Calculadora de Factorial** que aplica principios de:

- Herencia 
- Polimorfismo

---

## Preparacion del entorno

Pasos a realizar:

1. Clonar el repositorio

```
git clone https://github.com/Marcelo-QG/PG2_PRACTICA1.git
cd PG2_PRACTICA1 
``` 

2. Crear un entorno virtual

```
python -m venv venv
```

3. Activar el entorno virtual

- Windows:

```
.\venv\Scripts\activate
```

4. Ejecutar el script:

```
python main.py
```

5. Desactivar el entorno virtual:
 
```
deactivate
```


---

## Implementacion de la calculadora

Este módulo implementa una calculadora estándar con operaciones básicas:

```Python

from calculadora_poo import calculadora2

Instanciación

calc = calculadora2()

Operaciones básicas

print(calc._sumar(10, 5))
print(calc._resta(10, 5))
print(calc._multiplicacion(10, 5))
print(calc._division(10, 5))

```

---

# Implementacion de la Calculadora Factorial

Este módulo extiende la funcionalidad mediante herencia:

```Python

from Factorial import CalculadoraCientifica

 Cálculo de factorial

calcF = CalculadoraCientifica(5)
print(calcF.calcular())

```


