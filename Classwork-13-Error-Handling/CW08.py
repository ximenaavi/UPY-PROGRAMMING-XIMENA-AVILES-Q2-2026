# Integral of a function
import math

# INPUT
a_str = input("Write the left endpoint of the interval: ")
b_str = input("Write the right endpoint of the interval: ")
f_x = input("Write the function to integrate: ")
method = input("Write the method to use (LRM, RRM, MPM, TM): ")

valido = True

# Validar a
try:
    if "pi" in a_str:
        a = eval(a_str.replace("pi", str(math.pi)))
    else:
        a = float(a_str)
except:
    print("El límite inferior debe ser numérico")
    valido = False

# Validar b
if valido:
    try:
        if "pi" in b_str:
            b = eval(b_str.replace("pi", str(math.pi)))
        else:
            b = float(b_str)
    except:
        print("El límite superior debe ser numérico")
        valido = False

# Validar que la función no esté vacía
if valido:
    if f_x.strip() == "":
        print("La función ingresada no es válida")
        valido = False

# Validar que la función esté en términos de x
if valido:
    if "x" not in f_x:
        print("La función debe estar escrita en términos de x")
        valido = False
    else:
        funcion_sin_math = f_x.replace("math.", "")
        letras = ""
        for caracter in funcion_sin_math:
            if caracter.isalpha():
                letras = letras + caracter
        for nombre in ["sin", "cos", "tan", "exp", "sqrt", "log", "pi"]:
            letras = letras.replace(nombre, "")
        if letras != "" and letras != "x" * len(letras):
            print("La función debe estar escrita en términos de x")
            valido = False

# Probar que la función sea válida (un solo punto)
if valido:
    try:
        prueba = eval(f_x.replace("x", str(a)))
    except ZeroDivisionError:
        print("La función no está definida en algún punto del intervalo")
        valido = False
    except:
        print("La función ingresada no es válida")
        valido = False

# Validar que a sea menor que b
if valido:
    if a >= b:
        print("El límite inferior debe ser menor que el límite superior")
        valido = False

# Validar el método
if valido:
    if method != "LRM" and method != "RRM" and method != "MPM" and method != "TM":
        print("El método de integración no es válido. Usa LRM, RRM, MPM o TM")
        valido = False

# PROCESS
if valido:
    area = 0.0
    n = 1000
    h = (b - a) / n

    try:
        if method == "LRM":
            for i in range(0, n):
                xi = a + i * h
                height = eval(f_x.replace("x", str(xi)))
                area += height * h

        elif method == "RRM":
            for i in range(1, n + 1):
                xi = a + i * h
                height = eval(f_x.replace("x", str(xi)))
                area += height * h

        elif method == "MPM":
            constant = h / 2
            for i in range(0, n):
                xi = a + i * h + constant
                height = eval(f_x.replace("x", str(xi)))
                area += height * h

        elif method == "TM":
            for i in range(0, n + 1):
                xi = a + i * h
                height = eval(f_x.replace("x", str(xi)))
                if i == 0 or i == n:
                    area += height
                else:
                    area += 2 * height
            area = area * h / 2
    except ZeroDivisionError:
        print("La función no está definida en algún punto del intervalo")
        valido = False

    # OUTPUT
    if valido:
        print(f"The integration of {f_x} is {area:.3f}")