# Problema 5 - Dispositivos A y B

# Definimos el rango del gráfico
xmin, xmax = -1, 12
ymin, ymax = -1, 7

# Recorremos los valores de Y de arriba hacia abajo
for y in range(ymax, ymin - 1, -1):
    linea = ""

    for x in range(xmin, xmax + 1):

        # Recta de frontera: x + 2y = 10 -> y = (10 - x)/2
        y_line = (10 - x) / 2 if (10 - x) >= 0 else None

        # Condición para estar en la recta
        cond_line = (y_line is not None and abs(y - y_line) < 0.5)

        # Condición para estar en la región factible
        cond_region = (x >= 0 and y >= 0 and (x + 2*y <= 10))

        if cond_line:
            linea += "*"
        elif cond_region:
            linea += "o"
        elif x == 0 and y == 0:
            linea += "+"
        elif x == 0:
            linea += "|"
        elif y == 0:
            linea += "-"
        else:
            linea += " "
    print(linea)

# Leyenda
print("\nLeyenda del gráfico:")
print("  * = Frontera (x + 2y = 10)")
print("  o = Región factible (x + 2y <= 10, x>=0, y>=0)")
print("  | = Eje Y")
print("  - = Eje X")
print("  + = Origen (0,0)")
