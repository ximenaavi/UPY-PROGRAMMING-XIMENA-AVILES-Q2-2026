#Dígito Verificador UTFSM
#INPUT
rol = input("Ingresa el rol: ")

valido = True

try:
    sin_digito, digito_ingresado = rol.split("-")
except ValueError:
    print("Rol inválido: No tiene el formato XXXXXXXXX-X")
    valido = False

if valido:
    if not sin_digito.isdigit():
        print("Los digitos del rol deben ser numéricos")
        valido = False

if valido:
    if not digito_ingresado.isdigit() and digito_ingresado != "K":
        print("El digito verificador debe ser numérico")
        valido = False

if valido:
    #PROCESS
    rol_invertido = sin_digito[::-1]
    secuencia = [2, 3, 4, 5, 6, 7]
    suma = 0
    for i in range(len(rol_invertido)):
        digito = int(rol_invertido[i])
        multiplicador = secuencia[i % 6]  # reinicia la secuencia cada 6 pasos
        suma = suma + (digito * multiplicador)

    resultado = 11 - (suma % 11)
    # Casos especiales del algoritmo
    if resultado == 11:
        digito_verificador = "0"
    elif resultado == 10:
        digito_verificador = "K"
    else:
        digito_verificador = str(resultado)

    #OUTPUT
    if digito_ingresado == digito_verificador:
        print(rol)
    else:
        print(f"Error: El dígito verificador no conicide, se esperaba {digito_verificador}")