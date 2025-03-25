class calculadora2:
     def __init__(self, a,b):
         self._resultado = 0
         self.a = a
         self.b = b
         self.operacion = ""
         
     def _mostrar_operacion(self):
         return f"{self.operacion}: {self.a} y {self.b} = {self._resultado}"
     def mostrar_operaciones(self):
         return f"{self._sumar()}\n{self._resta()}\n{self._multiplicacion()}\n{self._division()}\n"
     
     def _sumar(self):
         self.operacion = "Suma"
         self._resultado = self.a + self.b
         return self._mostrar_operacion()
     def _resta(self):
         self.operacion = "Resta"
         self._resultado = self.a - self.b
         return self._mostrar_operacion()
     def _multiplicacion(self):
         self.operacion = "Multiplicar"
         self._resultado = self.a * self.b
         return self._mostrar_operacion()
     def _division(self):
         self.operacion = "dividir"
         self._resultado = self.a / self.b
         return self._mostrar_operacion()

calculadora1 = calculadora2(25, 5)
print(calculadora1.mostrar_operaciones())
     
     
        
         