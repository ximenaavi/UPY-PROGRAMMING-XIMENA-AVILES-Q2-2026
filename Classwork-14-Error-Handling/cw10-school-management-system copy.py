# Classwork #10 - School Management System
#INPUT
#usuarios con nombre y rol (diccionario)
usuarios = {
    'jperez':  {'password': '1234', 'rol': 'alumno',      'nombre': 'Juan Pérez'},
    'amartin': {'password': '1234', 'rol': 'alumno',      'nombre': 'Ana Martín'},
    'csilva':  {'password': '1234', 'rol': 'alumno',      'nombre': 'Carlos Silva'},
    'lhdez':   {'password': '1234', 'rol': 'alumno',      'nombre': 'Laura Hernández'},
    'dgomez':  {'password': '1234', 'rol': 'alumno',      'nombre': 'Diego Gómez'},
    'fcruz':   {'password': '1234', 'rol': 'alumno',      'nombre': 'Fernanda Cruz'},
    'mlopez':  {'password': '1234', 'rol': 'maestro',     'nombre': 'María López'},
    'rgarcia': {'password': '1234', 'rol': 'coordinador', 'nombre': 'Rosa García'}
}
#Tupla con materias
materias = ('Matematicas', 'Programacion', 'Ingles')
calificaciones = {
    'jperez':  {'Matematicas': 8.5, 'Programacion': 9.0, 'Ingles': 7.5},
    'amartin': {'Matematicas': 9.0, 'Programacion': 8.0, 'Ingles': 8.5},
    'csilva':  {'Matematicas': 6.5, 'Programacion': 7.0, 'Ingles': 8.0},
    'lhdez':   {'Matematicas': 9.5, 'Programacion': 9.5, 'Ingles': 9.0},
    'dgomez':  {'Matematicas': 7.0, 'Programacion': 6.5, 'Ingles': 7.0},
    'fcruz':   {'Matematicas': 8.0, 'Programacion': 8.5, 'Ingles': 6.0}
}
#PROCESS
#Acceso al programa con usurio y contraseña
acceso = False
while not acceso:
    usuario = input('Usuario: ')
    clave = input('Contraseña: ')
    if usuario in usuarios and usuarios[usuario]['password'] == clave:
        acceso = True
    else:
        print('Usuario o contraseña incorrectos. Intenta de nuevo.\n')
rol = usuarios[usuario]['rol']
nombre = usuarios[usuario]['nombre']
print(f'\nBienvenid@!, {nombre} ({rol})\n')
#PROCESS
#Menu que se va entregar 
if rol == 'alumno':
    print(f'Boleta de {nombre}')
    aprobadas = set()
    for materia in materias:
        calif = calificaciones[usuario][materia]
        print(f'{materia}: {calif}')
        if calif >= 7.0:
            aprobadas.add(materia)
    pendientes = set(materias) - aprobadas        
    if aprobadas:
        print(f'Materias aprobadas: {aprobadas}')
    else:
        print("Materias aprobadas: Ninguna")  
    if pendientes:
        print(f"Materias pendientes: {pendientes}")  
    else:
        print("Materias pendientes: Ninguna")        
   
elif rol == 'maestro':
    print('Lista de alumnos:')
    for clave_usuario in usuarios:
        if usuarios[clave_usuario]['rol'] == 'alumno':
            print(f"- {clave_usuario}: {usuarios[clave_usuario]['nombre']}")

    while True:
        alumno = input('\nAlumno (usuario): ')
        materia = input('Materia: ')
        nueva_calificacion = input('Nueva calificación: ')

        try:
            calificacion_anterior = calificaciones[alumno][materia]
        except KeyError:
            if alumno not in calificaciones:
                print('Ese usuario no existe.')
            else:
                print('Esa materia no existe.')
            continue

        confirmar = input('¿Confirmas el cambio? (yes/no): ')
        print(f'{materia}: {calificacion_anterior} ==> {nueva_calificacion}')

        if confirmar == 'yes':
            calificaciones[alumno][materia] = float(nueva_calificacion)
            print('Calificación actualizada.')
        elif confirmar == 'no':
            print('Cambio cancelado.')
        else:
            break

elif rol == 'coordinador':
    print('Profesores:')
    for clave_usuario in usuarios:
        if usuarios[clave_usuario]['rol'] == 'maestro':
            print(f"- {clave_usuario}: {usuarios[clave_usuario]['nombre']}")

    print('\nAlumnos:')
    for clave_usuario in usuarios:
        if usuarios[clave_usuario]['rol'] == 'alumno':
            print(f"- {clave_usuario}: {usuarios[clave_usuario]['nombre']}")

    print('\nRegistros:')
    for alumno in calificaciones:
        print(f"\n{usuarios[alumno]['nombre']} ({alumno}):")
        for materia in materias:
            print(f'  {materia}: {calificaciones[alumno][materia]}')