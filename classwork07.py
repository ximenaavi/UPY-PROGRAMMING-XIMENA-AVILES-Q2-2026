#Dígito Verificador UTFSM

#INPUT
rol = input("Ingresa el rol sin guión ni dígito verificador: ")

#PROCESS
rol_invertido = rol[::-1]

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
print(f"El rol completo es: {rol}-{digito_verificador}")