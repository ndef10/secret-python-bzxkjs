# Run `python main.py` in the terminal

# Note: Python is lazy loaded so the first run will take a moment,
# But after cached, subsequent loads are super fast! ⚡️

import platform
# print(f"Hello Python v{platform.python_version()}!")

def sumar_elementos_lista():     
  suma = 0
  for numero in [1, 2, 3, 4, 5]:
    suma += numero         
  return f"La suma de los elementos de la lista es: {suma}" 
print(sumar_elementos_lista())


def calcular_area_rectangulo(base, altura): 
  return f"El área es: {base * altura} unidades cuadradas"
print(calcular_area_rectangulo(5, 3))

def convertir_celsius_a_fahrenheit(celsius):
  return f"{celsius}°C equivalen a {(celsius * 9/5) + 32}°F"
print(convertir_celsius_a_fahrenheit(25))