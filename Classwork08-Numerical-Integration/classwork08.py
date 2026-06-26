# Integral of a function
# INPUT
import math

a = input("Write the left endpoint of the interval: ")
b = input("Write the right endpoint of the interval: ")
f_x = input("Write the function to integrate: ")
method = input("Write the method to use (RRM, LRM, MRM, T): ")

# Handle 'pi' 
if "pi" in a:
    a = eval(a.replace("pi", str(math.pi)))
else:
    a = float(a)

if "pi" in b:
    b = eval(b.replace("pi", str(math.pi)))
else:
    b = float(b)

# PROCESS
area = 0.0
n = 1000
h = (b - a) / n
shift = 0
constant = 0

if method == "RRM":
    shift = 1
elif method == "MRM":
    constant = h / 2
elif method == "T":
    for i in range(0, n + 1):
        xi = a + i * h
        height = eval(f_x.replace("x", str(xi)))
        if i == 0 or i == n:
            area += height        # endpoints: weight 1
        else:
            area += 2 * height   # middle points: weight 2
    area *= h / 2
if method != "T":
    for i in range(0 + shift, n + shift):
        xi = a + i * h + constant
        height = eval(f_x.replace("x", str(xi)))
        area += height * h

# OUTPUT
print(f"The integration of {f_x} is {area:.2f}") 