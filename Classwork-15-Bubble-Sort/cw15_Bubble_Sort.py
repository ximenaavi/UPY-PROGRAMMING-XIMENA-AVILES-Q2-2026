import random
import stddraw

from color import Color

def selection_sort(numbers):
    n = len(numbers)

#For the list
'''
def bubble_sort(numbers):
    #get the lenght of the array
    n = len(numbers)
    for sweep in range(n):
        for pair in range( 0, n-1 - sweep):
            if numbers[pair] > numbers[pair + 1]:
                numbers[pair], numbers[pair + 1] = numbers [pair+1], numbers[pair]
'''
'''
def selection_sort(numbers):
    #get the lenght of the array
    n = len(numbers)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if numbers[j] < numbers[min_index]:
                min_index = j
        numbers[i], numbers[min_index] = numbers[min_index], numbers[i]
'''

'''
def insertion_sort(numbers):
    #get the lenght of the array
    n = len(numbers)
    for i in range(1, n):
        key = numbers[i]
        j = i - 1
        while j >= 0 and numbers[j] > key:
            numbers[j + 1] = numbers[j]
            j -= 1
        numbers[j + 1] = key
'''

def draw_bars (numbers, selected=()):
    stddraw.clear()
    n = len(numbers)
    bar_width = 10.0 / n
    
    for i, number in enumerate(numbers):
        x= i * bar_width + bar_width / 2
        color = Color(255, 90, 90) if i in selected else Color(70, 130, 220)
        stddraw.setPenColor(color)
        stddraw.filledRectangle(x - bar_width / 2, 0, bar_width * 0.9, number)
    stddraw.show(500)


# ANIMATED bubble sort
'''
def bubble_sort_animated(numbers):
    # CONIG - Canvas
    stddraw.setXscale(-0.1, 10)
    stddraw.setYscale(-0.5, max(numbers) + 1)
    #get the lenght of the array
    n = len(numbers)
    
    for sweep in range(n):
        for pair in range( 0, n-1 - sweep):
            #DRAW the rectangles before the swap
            draw_bars(numbers, selected= (pair, pair +1))
            if numbers[pair] > numbers[pair + 1]:
                numbers[pair], numbers[pair + 1] = numbers [pair+1], numbers[pair]
                #DRAW the rentangles after the swap
                draw_bars(numbers, selected= (pair, pair +1))

    draw_bars(numbers)
    stddraw.show()
'''
'''
    def selection_sort_animated(numbers):
    # CONFIG - Canvas
    stddraw.setXscale(-0.1, 10)
    stddraw.setYscale(-0.5, max(numbers) + 1)
    n = len(numbers)

    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            # DRAW comparando el actual minimo contra el numero
            draw_bars(numbers, selected=(min_index, j))
            if numbers[j] < numbers[min_index]:
                min_index = j
        # SWAP el minimo encontrado a su posicion
        numbers[i], numbers[min_index] = numbers[min_index], numbers[i]
        draw_bars(numbers, selected=(i, min_index))

    draw_bars(numbers)
    stddraw.show()
'''

def insertion_sort_animated(numbers):
    # CONFIG - Canvas
    stddraw.setXscale(-0.1, 10)
    stddraw.setYscale(-0.5, max(numbers) + 1)
    n = len(numbers)

    for i in range(1, n):
        key = numbers[i]
        j = i - 1
        # DRAW el elemento que se va a insertar
        draw_bars(numbers, selected=(i, j))
        while j >= 0 and numbers[j] > key:
            numbers[j + 1] = numbers[j]
            # DRAW despues de mover el elemento
            draw_bars(numbers, selected=(j, j + 1))
            j -= 1
        numbers[j + 1] = key
        draw_bars(numbers, selected=(j + 1,))

    draw_bars(numbers)
    stddraw.show()
             
numbers = [random.randint(0,100) for x in range(10)]
print(f"Before sort: {numbers}")
#bubble_sort(numbers)
insertion_sort_animated(numbers)
#print(f"After bubble sort: {numbers}")
