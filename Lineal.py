# Programa para graficar dos funciones matemáticas en la consola (ASCII)

# Pedimos las dos funciones al usuario
func1 = input("Ingrese la primera función (ejemplo: 2*x+1): ")
func2 = input("Ingrese la segunda función (ejemplo: -x+3): ")

# Definimos el rango del gráfico (valores de X y Y)
xmin, xmax = -20, 20   # eje X desde -20 hasta 20
ymin, ymax = -20, 20   # eje Y desde -20 hasta 20

# Recorremos los valores de Y de arriba hacia abajo
for y in range(ymax, ymin - 1, -1):
    linea = ""  # cadena vacía para ir dibujando la fila

    # Recorremos los valores de X de izquierda a derecha
    for x in range(xmin, xmax + 1):

        # Calculamos el valor de cada función en este punto X
        try:
            y1 = eval(func1.replace("^", "**"))  # evalúa la primera función
            y2 = eval(func2.replace("^", "**"))  # evalúa la segunda función
        except:
            y1, y2 = None, None  # si hay error, no dibuja nada

        # Revisamos si la función pasa cerca del punto actual (x,y)
        cond1 = (y1 is not None and abs(y - y1) < 0.5)  # primera función
        cond2 = (y2 is not None and abs(y - y2) < 0.5)  # segunda función

        # Elegimos qué dibujar en este punto
        if cond1 and cond2:
            linea += "#"   # intersección de ambas funciones
        elif cond1:
            linea += "*"   # primera función
        elif cond2:
            linea += "o"   # segunda función
        elif x == 0 and y == 0:
            linea += "+"   # origen (0,0)
        elif x == 0:
            linea += "|"   # eje Y
        elif y == 0:
            linea += "-"   # eje X
        else:
            linea += " "   # espacio vacío
    
    # Mostramos la fila completa
    print(linea)
