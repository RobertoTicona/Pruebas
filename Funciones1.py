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

variables = set()
operaciones = 0

for i, c in enumerate(expresion):
    if c.isalpha():
        variables.add(c)

    elif c in "+-*/^":
        operaciones += 1

    # Detectar multiplicación implícita
    if i < len(expresion) - 1:  # mientras no sea el último carácter
        siguiente = expresion[i+1]
        # caso: número + letra  (ej: 5x)
        if c.isdigit() and siguiente.isalpha():
            operaciones += 1
        # caso: letra + letra (ej: xy)
        elif c.isalpha() and siguiente.isalpha():
            operaciones += 1

print("\n--- RESULTADOS ---")
print("Variables encontradas:", ", ".join(sorted(variables)))
print("Número de variables:", len(variables))
print("Número de operaciones registradas:", operaciones)
