"""
LOS COMENTARIOS PARA CORREGIR EL CÓDIGO ESTÁN DENTRO DEL MISMO. CORRIGEN Y COMITEEEN PARA QUE ME APAREZCAN LOS CAMBIOS, ME AVISAN ASÍ ENTRO A MIRAR.
Alumnas: Ascurra, Micaela; Bianchi, Emiliana; Caro Boldrini, Victoria; Guzman, Dana

Análisis Matemático II - Ingeniería en Sistemas de Información - 2024

--------------- LABORATIORIO EN PYTHON - MÉTODO DE EULER ----------------

El método de Euler constituye sólo una de muchas formas en que es posible aproximar una solución de una ecuación diferencial.
Propone empezar en el punto dado por el valor inicial y avanzar en la dirección indicada por el campo direccional.

"""
//faltaría agregar que el método avanza hasta el punto donde quiero obtener la aproximación, que aproxima un PVI...
def metodo_Euler(f, x0, y0, h, n):
    """
    Implementación del método de Euler para resolver una EDO:

    f: La función que define la EDO dy/dx = f(x, y).
    x0: El valor inicial de x.
    y0: El valor inicial de y en x0.
    """
    acá vamos a tener un problema, porque como el método de Euler nos aproxima la solución a un PVI, entonces, y0(x0) debería ser dato, 
    no que sea proporcionado por el usuario (traten de razonar qué sería la SPVI en términos gráficos... una familia? una curva de una familia?
    en ese caso pueden x0 e y0 ser valores cualesquiera?)
    """
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

# Definir la función que representa la EDO dy/dx = f(x, y)
def f(x, y):
    return x + y

# Pedir las condiciones iniciales y los parámetros al usuario
x0 = float(input("Ingrese el valor inicial de 'x0': "))
y0 = float(input("Ingrese el valor inicial de 'y0': "))
h = float(input("Ingrese el tamaño del paso 'h': "))
n = int(input("Ingrese el número total de pasos 'n': "))

# Resolver la EDO usando el método de Euler
solucion = metodo_Euler(f, x0, y0, h, n)
print("\nSolución aproximada utilizando el método de Euler:\n")
for valor in solucion:
    x_redondeado = round(valor[0], 3)
    y_redondeado = round(valor[1], 3)
    print(f"x = {x_redondeado}, y = {y_redondeado}")
    """
    Otro cuestión es, fíjense que las ecuaciones proporcionadas en el ejercicio no son la que ustedes han usado. Dejando de lado eso, 
    su script lo que hace es aproximar la solución en un punto que va a depender del paso que le pongan y el número de iteraciones.
    Lo que deben obtener como resultado es el valor de la EDO en un punto cercano al punto origen de la aporximación. 
    Usen los ejemplos dados porque los pueden resolver analíticamente, y así verificar lo que obtienen con el código
    """
    
