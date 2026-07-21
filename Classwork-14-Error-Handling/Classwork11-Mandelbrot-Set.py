# Classwork #11 - The Mandelbrot Set (Math)
#INPUT
config = {}
try:
    with open("config", "r") as file:
        for line in file:
            parameter, value = line.strip().split("=")
            config[parameter] = float(value) if "." in value else int(value)
except FileNotFoundError:
    print("No se encontró el archivo config.txt")
    exit()
except ValueError:
    print("El archivo config.txt está mal formado.")
    exit()

try:
    width, height, max_iter = config["ancho"], config["alto"], config["max_iter"]
except KeyError as error:
    print(f"Falta el parámetro {error} en config.txt")
    exit()

if not isinstance(width, int) or not isinstance(height, int):
    print("Los parámetros 'ancho' y 'alto' deben ser números enteros.")
    exit()

with open("mandelbrot.csv", "w") as output:
    output.write("row,column,iterations\n")
    for row in range(height):
        for column in range(width):
            real = config["real_min"] + (column / (width - 1)) * (config["real_max"] - config["real_min"])
            imag = config["imag_max"] - (row / (height - 1)) * (config["imag_max"] - config["imag_min"])
            c = complex(real, imag)
            
            z = 0 + 0j
            iterations = 0
            
            while (abs(z) <=2) and (iterations < max_iter):
                z = z * z + c
                iterations += 1
            
            output.write(f"{row},{column},{iterations}\n")