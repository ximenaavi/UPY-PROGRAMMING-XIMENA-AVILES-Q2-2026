from PIL import Image
config = {}
try:
    with open("config", "r") as file:
        for line in file:
            parameter, value = line.strip().split("=")
            config[parameter] = float(value) if "." in  value else int(value)
except FileNotFoundError:
    print("No se encontró el archivo config.txt")
    exit()
except ValueError:
    print("El archivo config.txt está mal formado.")
    exit()
print(config)

try:
    with open('mandelbrot.csv','r') as archivo:
        lineas = archivo.readlines()
except FileNotFoundError:
    print("No se encontró el archivo mandelbrot.csv")
    exit()

#quita los encabezados
lineas.pop(0)
#desempaquetas variables 
max_iter = config ["max_iter"]
ancho, alto = config['ancho'], config["alto"]
img = Image.new('HSV', (ancho,alto))
points_drawn = 0
for linea in lineas:
    try:
        row, column, iterations = linea.strip().split(",")
        iterations = int(iterations)
        row = int(row)
        column = int(column)
    except ValueError:
        print("El archivo mandelbrot.csv está mal formado.")
        exit()
    if row < 0 or row >= alto or column < 0 or column >= ancho:
        print(
            f"CSV point ({row}, {column}) is outside the image size "
            f"{alto}x{ancho}. Run Classwork11-Mandelbrot-Set.py again "
            "after changing config."
        )
        exit()
    if iterations == max_iter:
        color = (0, 0, 0)
    else:
        hue = int((iterations / max_iter) * 255)
        color = (hue, 255, 255)
    img.putpixel((column,row), color)
    points_drawn += 1
expected_points = ancho * alto
if points_drawn != expected_points:
    print(f"WARNING: mandelbrot.csv has {points_drawn} points, but expected {expected_points}. Regenerate the CSV.")
img_rgb = img.convert("RGB")
img_rgb.save("mandelbrot2.png")
print("DONE")