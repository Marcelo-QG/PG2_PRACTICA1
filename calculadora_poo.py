
class calculadora2:
     def __init__(self):
         self._resultado = 0
         self.operacion = ""
         
     def _mostrar_operacion(self):
         return f"{self.operacion}: {self.a} y {self.b} = {self._resultado}"
     def mostrar_operaciones(self):
         return f"\n{self._sumar()}\n{self._resta()}\n{self._multiplicacion()}\n{self._division()}\n"
     
     def _sumar(self,a ,b):
         self.operacion = "Suma"
         self._resultado = a + b
         return self.mostrar_resultado(a, b)
     def _resta(self,a ,b):
         self.operacion = "Resta"
         self._resultado = a - b
         return self.mostrar_resultado(a, b)
     def _multiplicacion(self,a ,b):
         self.operacion = "Multiplicar"
         self._resultado = a * b
         return self.mostrar_resultado(a, b)
     def _division(self,a ,b):
         self.operacion = "dividir"
         self._resultado = a / b
         return self.mostrar_resultado(a, b)
     def mostrar_resultado(self,a ,b):
         return f"El resultado de {self.operacion} entre {a} , {b} {self._resultado}"