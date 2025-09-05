"""
Analizar la función
set() es una función que no permite elementos repetidos y crea un conjunto
for c in expresion es el bucle que recorre la cadena carácter por carácter
isalpha() método que devuelve true si el carácter es una letra
.add() es un método de los conjuntos (set) para añadir un elemento.
sorted(variables) ordena el conjunto y lo convierte en una lista.
".join(...) une todos los elementos de la lista en una sola cadena, separados por comas.
len() devuelve la longitud (cuántos elementos hay) en listas, cadenas, conjuntos, etc
"""

expresion = input("Ingresa una función matemática: ")

variables = set()        # para guardar letras distintas
operaciones = 0

for c in expresion:
    if c.isalpha():      # si es letra, es variable
        variables.add(c)
    elif c in "+-":      # si es + o -, lo contamos
        operaciones += 1

print("\n--- RESULTADOS ---")
print("Variables encontradas:", ", ".join(sorted(variables)))
print("Número de variables:", len(variables))
print("Número de sumas/restas:", operaciones)