"""

Alumnas: Ascurra, Micaela; Bianchi, Emiliana; Caro Boldrini, Victoria; Guzman, Dana

Análisis Matemático II - Ingeniería en Sistemas de Información - 2024

--------------- LABORATIORIO EN PYTHON - MÉTODO DE EULER ----------------

El método de Euler constituye sólo una de muchas formas en que es posible aproximar una solución de una ecuación diferencial.
Propone empezar en el punto dado por el valor inicial y avanzar en la dirección indicada por el campo direccional.

"""

def metodo_Euler(f, x0, y0, h, n):
    """
    Implementación del método de Euler para resolver una EDO:

    f: La función que define la EDO dy/dx = f(x, y).
    x0: El valor inicial de x.
    y0: El valor inicial de y en x0.
    h: El tamaño del paso.
    n: El número total de pasos.
    """
    resultado = [(x0, y0)]
    x = x0
    y = y0
    for i in range(1, n + 1):
        y += h * f(x, y)
        x += h
        resultado.append((x, y))
    return resultado

# Definir la función que representa la EDO para el Ejercicio 1
def f_ejercicio1(x, y):
    return 0.2 * x * y

# Definir la función que representa la EDO para el Ejercicio 2
def f_ejercicio2(t, I):
    return 15 - 3 * I

# Resolver el Ejercicio 1
x0_ejercicio1 = 1
y0_ejercicio1 = 1
h1_ejercicio1 = 0.1
h2_ejercicio1 = 0.05
n_ejercicio1 = 5  # Para un paso de 0.1, y 10 para un paso de 0.05

solucion_ejercicio1_h1 = metodo_Euler(f_ejercicio1, x0_ejercicio1, y0_ejercicio1, h1_ejercicio1, n_ejercicio1)
solucion_ejercicio1_h2 = metodo_Euler(f_ejercicio1, x0_ejercicio1, y0_ejercicio1, h2_ejercicio1, n_ejercicio1 * 2)

# Resolver el Ejercicio 2
t0_ejercicio2 = 0
I0_ejercicio2 = 0
h_ejercicio2 = 0.1  # Usaremos un paso de 0.1
n_ejercicio2 = 5  # Para aproximar medio segundo (0.5), necesitamos 5 pasos

solucion_ejercicio2 = metodo_Euler(f_ejercicio2, t0_ejercicio2, I0_ejercicio2, h_ejercicio2, n_ejercicio2)

# Mostrar resultados
print("Resultados del Ejercicio 1:")
print("Aproximación de y(1.5) con un paso de 0.1:")
for valor in solucion_ejercicio1_h1:
    x_redondeado = round(valor[0], 3)
    y_redondeado = round(valor[1], 3)
    print(f"x = {x_redondeado}, y = {y_redondeado}")

print("\nAproximación de y(1.5) con un paso de 0.05:")
for valor in solucion_ejercicio1_h2:
    x_redondeado = round(valor[0], 3)
    y_redondeado = round(valor[1], 3)
    print(f"x = {x_redondeado}, y = {y_redondeado}")

print("\nResultados del Ejercicio 2:")
print("Aproximación de I(0.5):")
for valor in solucion_ejercicio2:
    t_redondeado = round(valor[0], 3)
    I_redondeado = round(valor[1], 3)
    print(f"t = {t_redondeado}, I = {I_redondeado}")
