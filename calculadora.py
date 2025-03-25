class calculadora:
    def __init__(self):
        self._resultado = 0
    def sumar(self, a, b):
        self._resultado = a + b
        return self._resultado
calculadora_1 = calculadora()

print(calculadora_1.sumar(10, 5))
        